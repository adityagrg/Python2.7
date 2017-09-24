from __future__ import absolute_import
from unittest import TestCase
import pyredis.protocol as hiredis
from pyredis.protocol import writer, to_bytes
import sys
from itertools import izip

# The class ReaderTest is more or less copied from the hiredis python package.
# The Licence Terms of hiredis (BSD) appeal to the ReaderTest class!


class ReaderTest(TestCase):
    def setUp(self):
        self.reader = hiredis.Reader()

    def reply(self):
        return self.reader.gets()

    def test_nothing(self):
        self.assertEqual(False, self.reply())

    def test_error_when_feeding_non_string(self):
        self.assertRaises(TypeError, self.reader.feed, 1)

    def test_protocol_error(self):
        self.reader.feed('x')
        self.assertRaises(hiredis.ProtocolError, self.reply)

    def test_protocol_error_with_custom_class(self):
        self.reader = hiredis.Reader(protocolError=RuntimeError)
        self.reader.feed('x')
        self.assertRaises(RuntimeError, self.reply)

    def test_protocol_error_with_custom_callable(self):
        class CustomException(Exception):
            pass

        self.reader = hiredis.Reader(protocolError=lambda e: CustomException(e))
        self.reader.feed('x')
        self.assertRaises(CustomException, self.reply)

    def test_fail_with_wrong_protocol_error_class(self):
        self.assertRaises(TypeError, hiredis.Reader, protocolError=u'wrong')

    def test_error_string(self):
        self.reader.feed('-error\r\n')
        error = self.reply()

        self.assertEqual(hiredis.ReplyError, type(error))
        self.assertEqual((u'error',), error.args)

    def test_error_string_partial(self):
        self.reader.feed('-err')
        self.assertFalse(self.reply())
        self.reader.feed('or\r\n')
        error = self.reply()

        self.assertEqual(hiredis.ReplyError, type(error))
        self.assertEqual((u'error',), error.args)

    def test_error_string_partial_footer(self):
        self.reader.feed('-error')
        self.assertFalse(self.reply())
        self.reader.feed('\r')
        self.assertFalse(self.reply())
        self.reader.feed('\n')
        error = self.reply()

        self.assertEqual(hiredis.ReplyError, type(error))
        self.assertEqual((u'error',), error.args)

    def test_error_string_with_custom_class(self):
        self.reader = hiredis.Reader(replyError=RuntimeError)
        self.reader.feed('-error\r\n')
        error = self.reply()

        self.assertEqual(RuntimeError, type(error))
        self.assertEqual((u'error',), error.args)

    def test_error_string_with_custom_callable(self):
        class CustomException(Exception):
            pass

        self.reader = hiredis.Reader(replyError=lambda e: CustomException(e))
        self.reader.feed('-error\r\n')
        error = self.reply()

        self.assertEqual(CustomException, type(error))
        self.assertEqual((u'error',), error.args)

    def test_fail_with_wrong_reply_error_class(self):
        self.assertRaises(TypeError, hiredis.Reader, replyError=u'wrong')

    def test_errors_in_nested_multi_bulk(self):
        self.reader.feed('*2\r\n-err0\r\n-err1\r\n')

        for r, error in izip((u'err0', u'err1'), self.reply()):
            self.assertEqual(hiredis.ReplyError, type(error))
            self.assertEqual((r,), error.args)

    def test_integer(self):
        value = 2 ** 63 - 1  # Largest 64-bit signed integer
        self.reader.feed((u':{0}\r\n'.format(value)).encode(u'ascii'))
        self.assertEqual(value, self.reply())

    def test_integer_partial_int(self):
        value = 2 ** 63 - 1  # Largest 64-bit signed integer
        strvalue = unicode(value).encode(u'ascii')
        part1, part2 = strvalue[:6], strvalue[6:]
        self.reader.feed(':')
        self.reader.feed(part1)
        self.assertFalse(self.reply())
        self.reader.feed(part2)
        self.reader.feed('\r\n')
        self.assertEqual(value, self.reply())

    def test_integer_partial_footer(self):
        value = 2 ** 63 - 1  # Largest 64-bit signed integer
        self.reader.feed((u':{0}'.format(value)).encode(u'ascii'))
        self.assertFalse(self.reply())
        self.reader.feed('\r')
        self.assertFalse(self.reply())
        self.reader.feed('\n')
        self.assertEqual(value, self.reply())

    def test_status_string(self):
        self.reader.feed('+ok\r\n')
        self.assertEqual('ok', self.reply())

    def test_status_string_partial(self):
        self.reader.feed('+ok')
        self.assertFalse(self.reply())
        self.reader.feed('ok\r\n')
        self.assertEqual('okok', self.reply())

    def test_status_string_partial_footer(self):
        self.reader.feed('+ok')
        self.assertFalse(self.reply())
        self.reader.feed('\r')
        self.assertFalse(self.reply())
        self.reader.feed('\n')
        self.assertEqual('ok', self.reply())

    def test_empty_bulk_string(self):
        self.reader.feed('$0\r\n\r\n')
        self.assertEqual('', self.reply())

    def test_NULL_bulk_string(self):
        self.reader.feed('$-1\r\n')
        self.assertEqual(None, self.reply())

    def test_bulk_string(self):
        self.reader.feed('$5\r\nhello\r\n')
        self.assertEqual('hello', self.reply())

    def test_bulk_string_partial(self):
        self.reader.feed('$5\r\nhel')
        self.assertFalse(self.reply())
        self.assertFalse(self.reply())
        self.reader.feed('lo\r\n')
        self.assertEqual('hello', self.reply())

    def test_bulk_string_partial_footer(self):
        self.reader.feed('$5\r\nhello')
        self.assertFalse(self.reply())
        self.reader.feed('\r')
        self.assertFalse(self.reply())
        self.reader.feed('\n')
        self.assertEqual('hello', self.reply())

    def test_bulk_string_without_encoding(self):
        snowman = '\xe2\x98\x83'
        self.reader.feed('$3\r\n' + snowman + '\r\n')
        self.assertEqual(snowman, self.reply())

    def test_bulk_string_with_encoding(self):
        snowman = '\xe2\x98\x83'
        self.reader = hiredis.Reader(encoding=u'utf-8')
        self.reader.feed('$3\r\n' + snowman + '\r\n')
        self.assertEqual(snowman.decode(u'utf-8'), self.reply())

    def test_bulk_string_with_other_encoding(self):
        snowman = '\xe2\x98\x83'
        self.reader = hiredis.Reader(encoding=u'utf-32')
        self.reader.feed('$3\r\n' + snowman + '\r\n')
        self.assertEqual(snowman, self.reply())

    def test_bulk_string_with_invalid_encoding(self):
        self.reader = hiredis.Reader(encoding=u'unknown')
        self.reader.feed('$5\r\nhello\r\n')
        self.assertRaises(LookupError, self.reply)

    def test_null_multi_bulk(self):
        self.reader.feed('*-1\r\n')
        self.assertEqual(None, self.reply())

    def test_empty_multi_bulk(self):
        self.reader.feed('*0\r\n')
        self.assertEqual([], self.reply())

    def test_multi_bulk(self):
        self.reader.feed('*2\r\n$5\r\nhello\r\n$5\r\nworld\r\n')
        self.assertEqual(['hello', 'world'], self.reply())

    def test_multi_bulk_with_partial_reply(self):
        self.reader.feed('*2\r\n$5\r\nhello\r\n')
        self.assertEqual(False, self.reply())
        self.reader.feed(':1\r\n')
        self.assertEqual(['hello', 1], self.reply())

    def test_nested_multi_bulk(self):
        self.reader.feed('*2\r\n*2\r\n$5\r\nhello\r\n$5\r\nworld\r\n$1\r\n!\r\n')
        self.assertEqual([['hello', 'world'], '!'], self.reply())

    def test_nested_multi_bulk_partial(self):
        self.reader.feed('*2\r\n*2\r\n$5\r\nhello\r')
        self.assertEqual(False, self.reply())
        self.reader.feed('\n$5\r\nworld\r\n$1\r\n!\r\n')
        self.assertEqual([['hello', 'world'], '!'], self.reply())

    def test_nested_multi_bulk_depth(self):
        self.reader.feed('*1\r\n*1\r\n*1\r\n*1\r\n$1\r\n!\r\n')
        self.assertEqual([[[['!']]]], self.reply())

    def test_subclassable(self):
        class TestReader(hiredis.Reader):
            def __init__(self, *args, **kwargs):
                super(TestReader, self).__init__(*args, **kwargs)

        reader = TestReader()
        reader.feed('+ok\r\n')
        self.assertEqual('ok', reader.gets())

    def test_invalid_offset(self):
        data = '+ok\r\n'
        self.assertRaises(ValueError, self.reader.feed, data, 6)

    def test_invalid_length(self):
        data = '+ok\r\n'
        self.assertRaises(ValueError, self.reader.feed, data, 0, 6)

    def test_ok_offset(self):
        data = 'blah+ok\r\n'
        self.reader.feed(data, 4)
        self.assertEqual('ok', self.reply())

    def test_ok_length(self):
        data = 'blah+ok\r\n'
        self.reader.feed(data, 4, len(data) - 4)
        self.assertEqual('ok', self.reply())

    def test_feed_bytearray(self):
        if sys.hexversion >= 0x02060000:
            self.reader.feed(bytearray('+ok\r\n'))
            self.assertEqual('ok', self.reply())


class TestWriter(TestCase):
    def test_encode_0_args(self):
        expected = '*0\r\n'
        self.assertEqual(
            writer(),
            expected)

    def test_encode_1_args(self):
        expected = '*1\r\n$4\r\nPING\r\n'
        self.assertEqual(
            writer(u'PING'),
            expected)

    def test_encode_2_args(self):
        expected = '*2\r\n$4\r\nECHO\r\n$14\r\nTest!!!!111elf\r\n'
        self.assertEqual(
            writer(u'ECHO', u'Test!!!!111elf'),
            expected)

    def test_encode_3_args(self):
        expected = '*3\r\n$3\r\nSET\r\n$8\r\nKey/Name\r\n$19\r\nSomeValue_?#!\xc3\x84\xc3\x9c\xc3\x96\r\n'
        self.assertEqual(
            writer(u'SET', u'Key/Name', u'SomeValue_?#!äüö'),
            expected)


class TestToBytes(TestCase):
    def test_int(self):
        expected = '512'
        result = to_bytes(512)
        self.assertEqual(result, expected)

    def test_float(self):
        expected = '0.815'
        result = to_bytes(0.815)
        self.assertEqual(result, expected)

    def test_str(self):
        expected = '\xc3\xbc\xc3\x9f_blarg'
        result = to_bytes(u'üß_blarg')
        self.assertEqual(result, expected)

    def test_bytes(self):
        expected = '0815'
        result = to_bytes('0815')
        self.assertEqual(result, expected)

    def test_ValueError(self):
        self.assertRaises(ValueError, to_bytes, object())

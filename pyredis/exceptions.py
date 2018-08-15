from __future__ import absolute_import
__author__ = u'adityagrg'


__all__ = [
    u'PyRedisError',
    u'PyRedisURLError',
    u'PyRedisConnError',
    u'PyRedisConnClosed',
    u'PyRedisConnReadTimeout',
    u'ProtocolError',
    u'ReplyError'
]


class PyRedisError(Exception):
    pass


class PyRedisURLError(PyRedisError):
    pass


class PyRedisConnError(PyRedisError):
    pass


class PyRedisConnReadTimeout(PyRedisError):
    pass


class PyRedisConnClosed(PyRedisError):
    pass


try:
    from hiredis import ReplyError, ProtocolError
except ImportError:
    class ReplyError(PyRedisError):
        pass


    class ProtocolError(PyRedisError):
        pass

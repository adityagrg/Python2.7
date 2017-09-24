__author__ = u'schlitzer'

__all__ = [
    u'Connection',
    u'Hash',
    u'HyperLogLog',
    u'Key',
    u'List',
    u'Publish',
    u'Scripting',
    u'Set',
    u'SSet',
    u'String',
    u'Subscribe',
    u'Transaction'
]


class BaseCommand(object):
    def __init__(self):
        self._cluster = False

    def execute(self, *args, **kwargs):
        raise NotImplemented


class Connection(BaseCommand):
    def __init__(self):
        super(Connection, self).__init__()

    def echo(self, *args, shard_key=None, sock=None):
        u""" Execute ECHO Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ECHO', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'ECHO', *args)

    def ping(self, shard_key=None, sock=None):
        u""" Execute PING Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result,exception
        """
        if self._cluster:
            return self.execute(u'PING', shard_key=shard_key, sock=sock)
        return self.execute(u'PING')


class Geo(BaseCommand):
    def __init__(self):
        super(Geo, self).__init__()

    def geoadd(self, *args):
        u""" Execute GEOADD Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'GEOADD', *args, shard_key=args[0])
        return self.execute(u'GEOADD', *args)

    def geodist(self, *args):
        u""" Execute GEODIST Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'GEODIST', *args, shard_key=args[0])
        return self.execute(u'GEODIST', *args)

    def geohash(self, *args):
        u""" Execute GEOHASH Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'GEOHASH', *args, shard_key=args[0])
        return self.execute(u'GEOHASH', *args)

    def georadius(self, *args):
        u""" Execute GEORADIUS Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'GEORADIUS', *args, shard_key=args[0])
        return self.execute(u'GEORADIUS', *args)

    def geopos(self, *args):
        u""" Execute GEOPOS Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'GEOPOS', *args, shard_key=args[0])
        return self.execute(u'GEOPOS', *args)

    def georadiusbymember(self, *args):
        u""" Execute GEORADIUSBYMEMBER Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'GEORADIUSBYMEMBER', *args, shard_key=args[0])
        return self.execute(u'GEORADIUSBYMEMBER', *args)


class Key(BaseCommand):
    def __init__(self):
        super(Key, self).__init__()

    def delete(self, *args):
        u""" Execute DEL Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'DEL', *args, shard_key=args[0])
        return self.execute(u'DEL', *args)

    def dump(self, *args):
        u""" Execute DUMP Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'DUMP', *args, shard_key=args[0])
        return self.execute(u'DUMP', *args)

    def exists(self, *args):
        u""" Execute EXISTS Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'EXISTS', *args, shard_key=args[0])
        return self.execute(u'EXISTS', *args)

    def expire(self, *args):
        u""" Execute EXPIRE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'EXPIRE', *args, shard_key=args[0])
        return self.execute(u'EXPIRE', *args)

    def expireat(self, *args):
        u""" Execute EXPIREAT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'EXPIREAT')
        return self.execute(u'EXPIREAT', *args)

    def keys(self, *args, shard_key=None, sock=None):
        u""" Execute KEYS Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'KEYS', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'KEYS', *args)

    def migrate(self, *args):
        u""" Execute MIGRATE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            raise NotImplemented
        return self.execute(u'MIGRATE', *args)

    def move(self, *args):
        u""" Execute MOVE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'MOVE', *args, shard_key=args[0])
        return self.execute(u'MOVE', *args)

    def object(self, *args, shard_key=None, sock=None):
        u""" Execute OBJECT Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'DEL', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'OBJECT', *args)

    def persist(self, *args):
        u""" Execute PERSIST Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'PERSIST', *args, shard_key=args[0])
        return self.execute(u'PERSIST', *args)

    def pexpire(self, *args):
        u""" Execute PEXPIRE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'PEXPIRE', *args, shard_key=args[0])
        return self.execute(u'PEXPIRE', *args)

    def pexpireat(self, *args):
        u""" Execute PEXPIREAT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'PEXPIREAT', *args, shard_key=args[0])
        return self.execute(u'PEXPIREAT', *args)

    def pttl(self, *args):
        u""" Execute PTTL Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'PTTL', *args, shard_key=args[0])
        return self.execute(u'PTTL', *args)

    def randomkey(self, *args, shard_key=None, sock=None):
        u""" Execute RANDOMKEY Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'RANDOMKEY', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'RANDOMKEY', *args)

    def rename(self, *args):
        u""" Execute RENAME Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'RENAME', *args, shard_key=args[0])
        return self.execute(u'RENAME', *args)

    def renamenx(self, *args):
        u""" Execute RENAMENX Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'RENAMENX', *args, shard_key=args[0])
        return self.execute(u'RENAMENX', *args)

    def restore(self, *args):
        u""" Execute RESTORE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'RESTORE', *args, shard_key=args[0])
        return self.execute(u'RESTORE', *args)

    def scan(self, *args, shard_key=None, sock=None):
        u""" Execute SCAN Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SCAN', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'SCAN', *args)

    def sort(self, *args):
        u""" Execute SORT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SORT', *args, shard_key=args[0])
        return self.execute(u'SORT', *args)

    def ttl(self, *args):
        u""" Execute TTL Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'TTL', *args, shard_key=args[0])
        return self.execute(u'TTL', *args)

    def type(self, *args):
        u""" Execute TYPE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'TYPE', *args, shard_key=args[0])
        return self.execute(u'TYPE', *args)

    def wait(self, *args):
        u""" Execute WAIT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'WAIT', *args, shard_key=args[0])
        return self.execute(u'WAIT', *args)


class String(BaseCommand):
    def __init__(self):
        super(String, self).__init__()

    def append(self, *args):
        u""" Execute APPEND Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'APPEND', *args, shard_key=args[0])
        return self.execute(u'APPEND', *args)

    def bitcount(self, *args):
        u""" Execute BITCOUNT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'BITCOUNT', *args, shard_key=args[0])
        return self.execute(u'BITCOUNT', *args)

    def bitfield(self, *args):
        u""" Execute BITFIELD Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'BITFIELD', *args, shard_key=args[0])
        return self.execute(u'BITFIELD', *args)

    def bitop(self, *args):
        u""" Execute BITOP Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'BITOP', *args, shard_key=args[1])
        return self.execute(u'BITOP', *args)

    def bitpos(self, *args):
        u""" Execute BITPOS Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'BITPOS', *args, shard_key=args[0])
        return self.execute(u'BITPOS', *args)

    def decr(self, *args):
        u""" Execute DECR Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'DECR', *args, shard_key=args[0])
        return self.execute(u'DECR', *args)

    def decrby(self, *args):
        u""" Execute DECRBY Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'DECRBY', *args, shard_key=args[0])
        return self.execute(u'DECRBY', *args)

    def get(self, *args):
        u""" Execute GET Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'GET', *args, shard_key=args[0])
        return self.execute(u'GET', *args)

    def getbit(self, *args):
        u""" Execute GETBIT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'GETBIT', *args, shard_key=args[0])
        return self.execute(u'GETBIT', *args)

    def getrange(self, *args):
        u""" Execute GETRANGE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'GETRANGE', *args, shard_key=args[0])
        return self.execute(u'GETRANGE', *args)

    def getset(self, *args):
        u""" Execute GETSET Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'GETSET', *args, shard_key=args[0])
        return self.execute(u'GETSET', *args)

    def incr(self, *args):
        u""" Execute INCR Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'INCR', *args, shard_key=args[0])
        return self.execute(u'INCR', *args)

    def incrby(self, *args):
        u""" Execute INCRBY Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'INCRBY', *args, shard_key=args[0])
        return self.execute(u'INCRBY', *args)

    def incrbyfloat(self, *args):
        u""" Execute INCRBYFLOAT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'INCRBYFLOAT', *args, shard_key=args[0])
        return self.execute(u'INCRBYFLOAT', *args)

    def mget(self, *args):
        u""" Execute MGET Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'MGET', *args, shard_key=args[0])
        return self.execute(u'MGET', *args)

    def mset(self, *args):
        u""" Execute MSET Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'MSET', *args, shard_key=args[0])
        return self.execute(u'MSET', *args)

    def msetnx(self, *args):
        u""" Execute MSETNX Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'MSETNX', *args, shard_key=args[0])
        return self.execute(u'MSETNX', *args)

    def psetex(self, *args):
        u""" Execute PSETEX Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'PSETEX', *args, shard_key=args[0])
        return self.execute(u'PSETEX', *args)

    def set(self, *args):
        u""" Execute SET Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SET', *args, shard_key=args[0])
        return self.execute(u'SET', *args)

    def setbit(self, *args):
        u""" Execute SETBIT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SETBIT', *args, shard_key=args[0])
        return self.execute(u'SETBIT', *args)

    def setex(self, *args):
        u""" Execute SETEX Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SETEX', *args, shard_key=args[0])
        return self.execute(u'SETEX', *args)

    def setnx(self, *args):
        u""" Execute SETNX Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SETNX', *args, shard_key=args[0])
        return self.execute(u'SETNX', *args)

    def setrange(self, *args):
        u""" Execute SETRANGE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SETRANGE', *args, shard_key=args[0])
        return self.execute(u'SETRANGE', *args)

    def strlen(self, *args):
        u""" Execute STRLEN Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'STRLEN', *args, shard_key=args[0])
        return self.execute(u'STRLEN', *args)


class Hash(BaseCommand):
    def __init__(self):
        super(Hash, self).__init__()

    def hdel(self, *args):
        u""" Execute HDEL Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HDEL', *args, shard_key=args[0])
        return self.execute(u'HDEL', *args)

    def hexists(self, *args):
        u""" Execute HEXISTS Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HEXISTS', *args, shard_key=args[0])
        return self.execute(u'HEXISTS', *args)

    def hget(self, *args):
        u""" Execute HGET Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HGET', *args, shard_key=args[0])
        return self.execute(u'HGET', *args)

    def hgetall(self, *args):
        u""" Execute HGETALL Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HGETALL', *args, shard_key=args[0])
        return self.execute(u'HGETALL', *args)

    def hincrby(self, *args):
        u""" Execute HINCRBY Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HINCRBY', *args, shard_key=args[0])
        return self.execute(u'HINCRBY', *args)

    def hincrbyfloat(self, *args):
        u""" Execute HINCRBYFLOAT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HINCRBYFLOAT', *args, shard_key=args[0])
        return self.execute(u'HINCRBYFLOAT', *args)

    def hkeys(self, *args):
        u""" Execute HKEYS Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HKEYS', *args, shard_key=args[0])
        return self.execute(u'HKEYS', *args)

    def hlen(self, *args):
        u""" Execute HLEN Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HLEN', *args, shard_key=args[0])
        return self.execute(u'HLEN', *args)

    def hmget(self, *args):
        u""" Execute HMGET Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HMGET', *args, shard_key=args[0])
        return self.execute(u'HMGET', *args)

    def hmset(self, *args):
        u""" Execute HMSET Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HMSET', *args, shard_key=args[0])
        return self.execute(u'HMSET', *args)

    def hset(self, *args):
        u""" Execute HSET Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HSET', *args, shard_key=args[0])
        return self.execute(u'HSET', *args)

    def hsetnx(self, *args):
        u""" Execute HSETNX Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HSETNX', *args, shard_key=args[0])
        return self.execute(u'HSETNX', *args)

    def hstrlen(self, *args):
        u""" Execute HSTRLEN Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HSTRLEN', *args, shard_key=args[0])
        return self.execute(u'HSTRLEN', *args)

    def hvals(self, *args):
        u""" Execute HVALS Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HVALS', *args, shard_key=args[0])
        return self.execute(u'HVALS', *args)

    def hscan(self, *args):
        u""" Execute HSCAN Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'HSCAN', *args, shard_key=args[0])
        return self.execute(u'HSCAN', *args)


class List(BaseCommand):
    def __init__(self):
        super(List, self).__init__()

    def blpop(self, *args):
        u""" Execute BLPOP Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'BLPOP', *args, shard_key=args[0])
        return self.execute(u'BLPOP', *args)

    def brpop(self, *args):
        u""" Execute BRPOP Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'BRPOP', *args, shard_key=args[0])
        return self.execute(u'BRPOP', *args)

    def brpoplpush(self, *args):
        u""" Execute BRPOPPUSH Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'BRPOPPUSH', *args, shard_key=args[0])
        return self.execute(u'BRPOPPUSH', *args)

    def lindex(self, *args):
        u""" Execute LINDEX Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'LINDEX', *args, shard_key=args[0])
        return self.execute(u'LINDEX', *args)

    def linsert(self, *args):
        u""" Execute LINSERT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'LINSERT', *args, shard_key=args[0])
        return self.execute(u'LINSERT', *args)

    def llen(self, *args):
        u""" Execute LLEN Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'LLEN', *args, shard_key=args[0])
        return self.execute(u'LLEN', *args)

    def lpop(self, *args):
        u""" Execute LPOP Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'LPOP', *args, shard_key=args[0])
        return self.execute(u'LPOP', *args)

    def lpush(self, *args):
        u""" Execute LPUSH Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'LPUSH', *args, shard_key=args[0])
        return self.execute(u'LPUSH', *args)

    def lpushx(self, *args):
        u""" Execute LPUSHX Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'LPUSHX', *args, shard_key=args[0])
        return self.execute(u'LPUSHX', *args)

    def lrange(self, *args):
        u""" Execute LRANGE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'LRANGE', *args, shard_key=args[0])
        return self.execute(u'LRANGE', *args)

    def lrem(self, *args):
        u""" Execute LREM Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'LREM', *args, shard_key=args[0])
        return self.execute(u'LREM', *args)

    def lset(self, *args):
        u""" Execute LSET Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'LSET', *args, shard_key=args[0])
        return self.execute(u'LSET', *args)

    def ltrim(self, *args):
        u""" Execute LTRIM Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'LTRIM', *args, shard_key=args[0])
        return self.execute(u'LTRIM', *args)

    def rpop(self, *args):
        u""" Execute RPOP Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'RPOP', *args, shard_key=args[0])
        return self.execute(u'RPOP', *args)

    def rpoplpush(self, *args):
        u""" Execute RPOPLPUSH Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'RPOPLPUSH', *args, shard_key=args[0])
        return self.execute(u'RPOPLPUSH', *args)

    def rpush(self, *args):
        u""" Execute RPUSH Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'RPUSH', *args, shard_key=args[0])
        return self.execute(u'RPUSH', *args)

    def rpushx(self, *args):
        u""" Execute RPUSHX Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'RPUSHX', *args, shard_key=args[0])
        return self.execute(u'RPUSHX', *args)


class Set(BaseCommand):
    def __init__(self):
        super(Set, self).__init__()

    def sadd(self, *args):
        u""" Execute SADD Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SADD', *args, shard_key=args[0])
        return self.execute(u'SADD', *args)

    def scard(self, *args):
        u""" Execute SCARD Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SCARD', *args, shard_key=args[0])
        return self.execute(u'SCARD', *args)

    def sdiff(self, *args):
        u""" Execute SDIFF Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SDIFF', *args, shard_key=args[0])
        return self.execute(u'SDIFF', *args)

    def sdiffstore(self, *args):
        u""" Execute SDIFFSTORE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SDIFFSTORE', *args, shard_key=args[0])
        return self.execute(u'SDIFFSTORE', *args)

    def sinter(self, *args):
        u""" Execute SINTER Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SINTER', *args, shard_key=args[0])
        return self.execute(u'SINTER', *args)

    def sinterstore(self, *args):
        u""" Execute SINTERSTORE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SINTERSTORE', *args, shard_key=args[0])
        return self.execute(u'SINTERSTORE', *args)

    def sismember(self, *args):
        u""" Execute SISMEMBER Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SISMEMBER', *args, shard_key=args[0])
        return self.execute(u'SISMEMBER', *args)

    def smembers(self, *args):
        u""" Execute SMEMBERS Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SMEMBERS', *args, shard_key=args[0])
        return self.execute(u'SMEMBERS', *args)

    def smove(self, *args):
        u""" Execute SMOVE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SMOVE', *args, shard_key=args[0])
        return self.execute(u'SMOVE', *args)

    def spop(self, *args):
        u""" Execute SPOP Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SPOP', *args, shard_key=args[0])
        return self.execute(u'SPOP', *args)

    def srandmember(self, *args):
        u""" Execute SRANDMEMBER Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SRANDMEMBER', *args, shard_key=args[0])
        return self.execute(u'SRANDMEMBER', *args)

    def srem(self, *args):
        u""" Execute SREM Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SREM', *args, shard_key=args[0])
        return self.execute(u'SREM', *args)

    def sunion(self, *args):
        u""" Execute SUNION Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SUNION', *args, shard_key=args[0])
        return self.execute(u'SUNION', *args)

    def sunoinstore(self, *args):
        u""" Execute SUNIONSTORE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SUNIONSTORE', *args, shard_key=args[0])
        return self.execute(u'SUNIONSTORE', *args)

    def sscan(self, *args):
        u""" Execute SSCAN Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SSCAN', *args, shard_key=args[0])
        return self.execute(u'SSCAN', *args)


class SSet(BaseCommand):
    def __init__(self):
        super(SSet, self).__init__()

    def zadd(self, *args):
        u""" Execute ZADD Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZADD', *args, shard_key=args[0])
        return self.execute(u'ZADD', *args)

    def zcard(self, *args):
        u""" Execute ZCARD Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZCARD', *args, shard_key=args[0])
        return self.execute(u'ZCARD', *args)

    def zcount(self, *args):
        u""" Execute ZCOUNT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZCOUNT', *args, shard_key=args[0])
        return self.execute(u'ZCOUNT', *args)

    def zincrby(self, *args):
        u""" Execute ZINCRBY Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZINCRBY', *args, shard_key=args[0])
        return self.execute(u'ZINCRBY', *args)

    def zinterstore(self, *args):
        u""" Execute ZINTERSTORE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZINTERSTORE', *args, shard_key=args[0])
        return self.execute(u'ZINTERSTORE', *args)

    def zlexcount(self, *args):
        u""" Execute ZLEXCOUNT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZLEXCOUNT', *args, shard_key=args[0])
        return self.execute(u'ZLEXCOUNT', *args)

    def zrange(self, *args):
        u""" Execute ZRANGE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZRANGE', *args, shard_key=args[0])
        return self.execute(u'ZRANGE', *args)

    def zrangebylex(self, *args):
        u""" Execute ZRANGEBYLEX Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZRANGEBYLEX', *args, shard_key=args[0])
        return self.execute(u'ZRANGEBYLEX', *args)

    def zrangebyscore(self, *args):
        u""" Execute ZRANGEBYSCORE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZRANGEBYSCORE', *args, shard_key=args[0])
        return self.execute(u'ZRANGEBYSCORE', *args)

    def zrank(self, *args):
        u""" Execute ZRANK Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZRANK', *args, shard_key=args[0])
        return self.execute(u'ZRANK', *args)

    def zrem(self, *args):
        u""" Execute ZREM Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZREM', *args, shard_key=args[0])
        return self.execute(u'ZREM', *args)

    def zremrangebylex(self, *args):
        u""" Execute ZREMRANGEBYLEX Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZREMRANGEBYLEX', *args, shard_key=args[0])
        return self.execute(u'ZREMRANGEBYLEX', *args)

    def zremrangebyrank(self, *args):
        u""" Execute ZREMRANGEBYRANK Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZREMRANGEBYRANK', *args, shard_key=args[0])
        return self.execute(u'ZREMRANGEBYRANK', *args)

    def zremrangebyscrore(self, *args):
        u""" Execute ZREMRANGEBYSCORE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZREMRANGEBYSCORE', *args, shard_key=args[0])
        return self.execute(u'ZREMRANGEBYSCORE', *args)

    def zrevrange(self, *args):
        u""" Execute ZREVRANGE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZREVRANGE', *args, shard_key=args[0])
        return self.execute(u'ZREVRANGE', *args)

    def zrevrangebylex(self, *args):
        u""" Execute ZREVRANGEBYLEX Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZREVRANGEBYLEX', *args, shard_key=args[0])
        return self.execute(u'ZREVRANGEBYLEX', *args)

    def zrevrangebyscore(self, *args):
        u""" Execute ZREVRANGEBYSCORE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZREVRANGEBYSCORE', *args, shard_key=args[0])
        return self.execute(u'ZREVRANGEBYSCORE', *args)

    def zrevrank(self, *args):
        u""" Execute ZREVRANK Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZREVRANK', *args, shard_key=args[0])
        return self.execute(u'ZREVRANK', *args)

    def zscore(self, *args):
        u""" Execute ZSCORE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZSCORE', *args, shard_key=args[0])
        return self.execute(u'ZSCORE', *args)

    def zunionstore(self, *args):
        u""" Execute ZUNIONSTORE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZUNIONSTORE', *args, shard_key=args[0])
        return self.execute(u'ZUNIONSTORE', *args)

    def zscan(self, *args):
        u""" Execute ZSCAN Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'ZSCAN', *args, shard_key=args[0])
        return self.execute(u'ZSCAN', *args)


class HyperLogLog(BaseCommand):
    def __init__(self):
        super(HyperLogLog, self).__init__()

    def pfadd(self, *args):
        u""" Execute PFADD Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'PFADD', *args, shard_key=args[0])
        return self.execute(u'PFADD', *args)

    def pfcount(self, *args):
        u""" Execute PFCOUNT Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'PFCOUNT', *args, shard_key=args[0])
        return self.execute(u'PFCOUNT', *args)

    def pfmerge(self, *args):
        u""" Execute PFMERGE Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'PFMERGE', *args, shard_key=args[0])
        return self.execute(u'PFMERGE', *args)


class Publish(BaseCommand):
    def __init__(self):
        super(Publish, self).__init__()

    def publish(self, *args):
        u""" Execute PUBLISH Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            raise NotImplemented
        return self.execute(u'PUBLISH', *args)


class Subscribe(object):
    def write(self, *args):
        raise NotImplemented

    def psubscribe(self, *args):
        u""" Execute PSUBSCRIBE Command, consult Redis documentation for details.

        :return: result, exception
        """
        return self.write(u'PSUBSCRIBE', *args)

    def punsubscribe(self, *args):
        u""" Execute PUNSUBSCRIBE Command, consult Redis documentation for details.

        :return: result, exception
        """
        return self.write(u'PUNSUBSCRIBE', *args)

    def subscribe(self, *args):
        u""" Execute SUBSCRIBE Command, consult Redis documentation for details.

        :return: result, exception
        """
        return self.write(u'SUBSCRIBE', *args)

    def unsubscribe(self, *args):
        u""" Execute UNSUBSCRIBE Command, consult Redis documentation for details.

        :return: result, exception
        """
        return self.write(u'UNSUBSCRIBE', *args)


class Transaction(BaseCommand):
    def __init__(self):
        super(Transaction, self).__init__()

    def discard(self, *args, shard_key=None, sock=None):
        u""" Execute DISCARD Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'DISCARD', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'DISCARD', *args)

    def exec(self, *args, shard_key=None, sock=None):
        u""" Execute EXEC Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'EXEC', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'EXEC', *args)

    def multi(self, *args, shard_key=None, sock=None):
        u""" Execute MULTI Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'MULTI', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'MULTI', *args)

    def unwatch(self, *args, shard_key=None, sock=None):
        u""" Execute UNWATCH Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'UNWATCH', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'UNWATCH', *args)

    def watch(self, *args):
        u""" Execute WATCH Command, consult Redis documentation for details.

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'WATCH', *args, shard_key=args[0])
        return self.execute(u'WATCH', *args)


class Scripting(BaseCommand):
    def __init__(self):
        super(Scripting, self).__init__()

    def eval(self, *args, shard_key=None, sock=None):
        u""" Execute EVAL Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'EVAL', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'EVAL', *args)

    def evalsha(self, *args, shard_key=None, sock=None):
        u""" Execute EVALSHA Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'EVALSHA', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'EVALSHA', *args)

    def script_debug(self, *args, shard_key=None, sock=None):
        u""" Execute SCRIPT DEBUG Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SCRIPT', u'DEBUG', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'SCRIPT', u'DEBUG', *args)

    def script_exists(self, *args, shard_key=None, sock=None):
        u""" Execute SCRIPT EXISTS Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SCRIPT', u'EXISTS', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'SCRIPT', u'EXISTS', *args)

    def script_flush(self, *args, shard_key=None, sock=None):
        u""" Execute SCRIPT FLUSH Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SCRIPT', u'FLUSH', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'SCRIPT', u'FLUSH', *args)

    def script_kill(self, *args, shard_key=None, sock=None):
        u""" Execute SCRIPT KILL Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SCRIPT', u'KILL', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'SCRIPT', u'KILL', *args)

    def script_load(self, *args, shard_key=None, sock=None):
        u""" Execute SCRIPT LOAD Command, consult Redis documentation for details.

        :param shard_key: (optional)
            Should be set to the key name you try to work with.
            Can not be used if sock is set.

            Only used if used with a Cluster Client
        :type shard_key: string

        :param sock: (optional)
            The string representation of a socket, the command should be executed against.
            For example: "testhost_6379"
            Can not be used if shard_key is set.

            Only used if used with a Cluster Client
        :type sock: string

        :return: result, exception
        """
        if self._cluster:
            return self.execute(u'SCRIPT', u'LOAD', *args, shard_key=shard_key, sock=sock)
        return self.execute(u'SCRIPT', u'LOAD', *args)
      

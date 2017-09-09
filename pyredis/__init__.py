__author__ = u'schlitzer'

u"""
Redis Client implementation for Python 3.

Copyright (c) 2015, Stephan Schultchen.

License: MIT (see LICENSE for details)
"""

from __future__ import absolute_import
from pyredis.exceptions import *
from pyredis.client import Client, ClusterClient, HashClient, PubSubClient, SentinelClient
from pyredis.pool import ClusterPool, HashPool, Pool, SentinelHashPool, SentinelPool

__all__ = [
    u'get_by_url',
    u'Client',
    u'ClusterClient',
    u'ClusterPool',
    u'HashClient',
    u'PubSubClient',
    u'SentinelClient',
    u'HashPool',
    u'Pool',
    u'SentinelPool',
    u'SentinelHashPool',
    u'PyRedisConnError',
    u'PyRedisConnReadTimeout',
    u'PyRedisConnClosed',
    u'PyRedisError',
    u'ProtocolError',
    u'ReplyError'
]


def get_by_url(url):
    scheme, rest = url.split(u'://', 1)
    conns = list()
    kwargs = dict()
    if u'?' in rest:
        connect, opts = (rest.split(u'?', 1))
    else:
        connect = rest
        opts = None
    for conn in connect.split(u","):
        conn = conn.rsplit(u':', 1)
        if len(conn) == 2:
            conn[1] = int(conn[1])
        conns.append(conn)
    if opts:
        kwargs = dict()
        for opt in opts.split(u'&'):
            key, value = opt.split(u'=', 1)
            kwargs[key] = _opts_type_helper(key, value)
    try:
        if scheme == u"cluster":
            return ClusterPool(seeds=conns, **kwargs)
        elif scheme == u"redis":
            host = conns[0][0]
            try:
                port = conns[0][1]
            except IndexError:
                port = 6379
            return Pool(host=host, port=port, **kwargs)
        elif scheme == u"sentinel":
            return SentinelPool(sentinels=conns, **kwargs)
        elif scheme == u"pubsub":
            host = conns[0][0]
            try:
                port = conns[0][1]
            except IndexError:
                port = 6379
            return PubSubClient(host=host, port=port, **kwargs)
        else:
            raise PyRedisURLError(u"invalid schema: {0}")
    except TypeError, err:
        raise PyRedisURLError(u"unexpected or missing options specified: {0}".format(err))


def _opts_type_helper(opt, value):
    if opt in [u'database', u'pool_size', u'retries']:
        return int(value)
    elif opt in [u'conn_timeout', u'read_timeout']:
        return float(value)
    elif opt in [u'slave_ok']:
        if value in [u'true', u'True', 1]:
            return True
        else:
            return False
    else:
        return value

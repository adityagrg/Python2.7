Introduction
************
Redis Client implementation for Python. The Client supports Python 2. Implementation of Python 3 already exists https://github.com/schlitzered/pyredis .

Currently implemented Features:
  - Base Redis Client
  - Publish Subscribe Client
  - Sentinel Client
  - Connection Pool
  - Sentinel Backed Connection Pool
  - Client & Pool for Redis Cluster
  - Bulk Mode ( Not supported with Redis Cluster )
  - Client & Pool with Static Hash Cluster (Supports Bulk Mode)
  - Sentinel Backed Client & Pool with Static Hash Cluster (Supports Bulk Mode)


Installing
----------

pyredis can be installed via pip as follows:

.. code::

    pip install python_redis

Author
------

Aditya Garg <adityagrg097@gmail.com>

License
-------

Unless stated otherwise on-file pyredis uses the MIT license,
check LICENSE file.

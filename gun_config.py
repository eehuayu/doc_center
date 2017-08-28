# -*- coding: utf-8 -*-

import pymysql
pymysql.install_as_MySQLdb()

proc_name = 'doc_center'
# sync/gevent
worker_class = 'gevent'
bind = ['0.0.0.0:44123']
workers = 1

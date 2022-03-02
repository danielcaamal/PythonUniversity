from logger_base import log
import psycopg2 as bd
from psycopg2 import pool
from psycopg2.extras import RealDictCursor, DictCursor, NamedTupleCursor, LoggingCursor
import sys

class Connection():
    _PARAMS = {
        'user':'daniel',
        'password':'daniel',
        'host':'192.168.100.32',
        'database':'test',
        'port':'5432'
    }

    _MIN_CONN = 1
    _MAX_CONN = 5
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CONN, cls._MAX_CONN, **cls._PARAMS)
                log.info(f'Connection with Pool Successfully: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Something went wrong when getting the pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def get_connection(cls):
        try:
            conn = cls.get_pool().getconn()
            log.debug(f'Connection Successfully: {conn}')
            return conn
        except Exception as e:
            log.error(f'Something went wrong when connecting to the database: {e}')
            sys.exit()

    @classmethod
    def release_connection(cls, conn):
        try:
            cls.get_pool().putconn(conn)
            log.debug(f'Connection Released: {conn}')
            return conn
        except Exception as e:
            log.error(f'Something went wrong when connecting to the database: {e}')
            sys.exit()

    @classmethod
    def close_connections(cls):
        cls.get_pool().closeall()
        log.info(f'All Connections Closed')


class PoolCursor():
    REAL_DICT_CURSOR = RealDictCursor
    DICT_CURSOR = DictCursor
    NAMED_TUPLE_CURSOR = NamedTupleCursor
    LOGGING_CURSOR = LoggingCursor

    def __init__(self, cursor=DICT_CURSOR):
        self._conn = None
        self._cursor = None
        self._cursor_factory = cursor
    
    def __enter__(self):
        log.debug(f'Starting the cursor')
        self._conn = Connection.get_connection()
        self._cursor = self._conn.cursor(cursor_factory=self._cursor_factory)
        return self._cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Closing the cursor')
        if exc_val:
            self._conn.rollback()
            log.error(f'Something went wrong, doing rollback: {exc_type} {exc_val} {exc_tb}')
        else:
            self._conn.commit()
            log.debug('Committing transaction')
        self._cursor.close()
        Connection.release_connection(self._conn)

if __name__ == '__main__':

    # Creating the first connection
    conn1 = Connection.get_connection()
    
    Connection.release_connection(conn1)

    # Connection released then, the conn1 is assigned again
    conn1 = Connection.get_connection()

    # Creating another connections
    conn2 = Connection.get_connection()
    conn3 = Connection.get_connection()

    # Probing the pool cursor
    with PoolCursor() as cursor:
        cursor.execute('SELECT COUNT(*) as count FROM person')
        print(cursor.fetchall())

    # Release all connections
    Connection.close_connections()

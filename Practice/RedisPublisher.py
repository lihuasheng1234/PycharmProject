import redis


class RedisHelper:

    def __init__(self):
        self.pool = redis.ConnectionPool(host='192.168.205.129',port='6379',password='123456')
        self.__conn = redis.Redis(connection_pool=self.pool)
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub

if __name__ == '__main__':

    obj = RedisHelper()

    obj = RedisHelper()
    obj.public('hello')


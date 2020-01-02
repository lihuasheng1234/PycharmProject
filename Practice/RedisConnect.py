import redis


#连接池
pool=redis.ConnectionPool(host='192.168.205.129',port='6379',password='123456')
r = redis.Redis(connection_pool=pool)

p = r.pipeline(transaction=True)#原子操作 一致性

p.set('key2','value1111')
p.setnx('key1','value111')
p.set('key111','value3')

p.execute()




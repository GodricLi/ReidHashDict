# _*_ coding=utf-8 _*_


import redis

POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=100)

# hash数据类型的字典操作
"""
    redis={
        k1:'123',                                 字符串
        k2:[1,2,3],                               列表
        k3:{1,2,3,4},                             集合    
        k4:{'name':'ric','age':18},               字典
        k5:{('alex',60),('eva-j',80),('rt',70),}, 有序集合
    }
    
    注意：redis操作时，只有第一层的value支持 dict，list...
    
    redis = {
        k3:[1,2,3],
        k4:{
            'id':1,
            'title':"字符串"，
            'price_list' = [
                {字符串},{字符串}
            ]        
        }
    }
    内层的数据使用时需要序列化成字符串
"""

# 1.添加值
conn = redis.Redis(connection_pool=POOL)
conn.hset("k3", "name", "godric")
conn.hset("k3", "age", 18)
conn.hmset("k3", {"name": "alex", "age": 18})

# 2.获取k3的全部值，不推荐直接使用
data = conn.hgetall('k3')

# 3.获取每个值
res = conn.hget('k3', 'age')

# 4.计数器每次自增
conn.hincrby('k3', 'age', amount=1)


# 5.如果redis的k4字典中有100w条数据，请打印所有数据
# 使用hscan_iter每次读取一定数据量，若一次性全部读取，可能会撑爆内存
result = conn.hscan_iter('k4', count=1000)
for item in result:
    print(item)

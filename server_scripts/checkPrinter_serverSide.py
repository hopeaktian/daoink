import time
import redis

"""
    type: python scirpt file
    useway: use supervisor to run this file
    function: receive printer status from redis, and judge useable of printer.  
"""

# set key name of printer in redis.
REDIS_PRINTER_KEY = 'test_printer'

# Redis connect config
class RedisConfig:
    host = "www.yourhostname.com"           # redis服务器主机地址
    password = "your_redis_password"        # redis密码
    port = 6379

    def __init__(self, host, password, port):
        self.host = host
        self.password = password
        self.port = port

def check():
    r = redis.Redis(host=RedisConfig.host,
                    password=RedisConfig.password,
                    port=RedisConfig.port,
                    db=0,
                    decode_responses=True)

    if int(r.lindex(REDIS_PRINTER_KEY, 0)) == 1 and abs(int(time.time()) - int(r.lindex(REDIS_PRINTER_KEY, 1))) <= 5:
        r.lset("test_printer", 2, 1)
        print "Online"
    else:
        r.lset("test_printer", 2, 0)
        print "Offline"
while True:
    check()
    time.sleep(3)

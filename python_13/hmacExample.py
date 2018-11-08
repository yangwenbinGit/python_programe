# hmac
# 我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下
import hmac
import random
import string

salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(salt)

message = b'Hello,World!'
key = bytes(salt,encoding='utf-8')  # 字符串转换为字节bytes类型
h = hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())

# 要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes
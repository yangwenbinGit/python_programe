# 摘要算法简介
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过

# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())   # d26a53750bc40b38b65a520292f69306

# 如果数据量很大的时候,可以多次调用update(),最后计算结果是一样的

hashMd5 = hashlib.md5()
hashMd5.update('how to use md5 in '.encode('utf-8'))
hashMd5.update('python hashlib?'.encode('utf-8'))
print(hashMd5.hexdigest())  # d26a53750bc40b38b65a520292f69306 注意如果是分开的话 下面和上面的格式必须是一样的,包括其中的空格，如果少了空格结果也会导致不一样

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())  # 2c76b57293ce30acef38d98f6046927161b46a44

# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。
# 一般这个加密算法主要是用在数据库方向，给密码进行加密。保证数据的安全
# 当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误
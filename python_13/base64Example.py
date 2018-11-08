# base64
# Base64是一种用64个字符来表示任意二进制数据的方法。
# Python内置的base64可以直接进行base64的编解码：
import base64
# b''前缀代表的就是bytes,使用base64进行编码和解码
print(base64.b64encode(b'binary\x00string'))  # b'YmluYXJ5AHN0cmluZw=='
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw==')) # b'binary\x00string'

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))

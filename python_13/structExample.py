# 好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换
# struct的pack函数把任意数据类型变成bytes(字节)
import struct, base64

# pack的第一个参数是处理指令 '>I'的意思是 >表示字节顺序是big-endian,也就是网络序，I表示的是4字节的无符号整数
# 将整数转换为一个字节 b'\x00\x9c@c',将小数转换为一个字节b'\x0e-\xf7A'
print(struct.pack('>I', 10240099))
print(struct.pack('<f', 30.897))

# unpack 就是把bytes变成相应的数据类型 >IH 后面的bytes依次变为 4个字节的无符号整数和2个字节的无符号整数
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', s))

bmp_data = base64.b64decode(
    'Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')


def bmp_info(data):
    return {
        'width': 200,
        'height': 100,
        'color': 24
    }


bi = bmp_info(bmp_data)

if bi['width'] == 28:
    print('width is yes')
else:
    print('width is worry')

if bi['height'] == 10 :
    print('height is yes')
else:
    print('height is worry')

if bi['color'] == 10 :
    print('color is yes')
else:
    print('color is worry')

# assert 就是断言语句,如果断言语句返回值为假,就会触发异常
# assert bi['width'] == 28
# assert bi['height'] == 10
# assert bi['color'] == 16
print('ok')

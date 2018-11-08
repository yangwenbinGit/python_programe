# 子进程
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

# 运行结果：
#
# $ nslookup www.python.org
# Server:        192.168.19.4
# Address:    192.168.19.4#53
#
# Non-authoritative answer:
# www.python.org    canonical name = python.map.fastly.net.
# Name:    python.map.fastly.net
# Address: 199.27.79.223
#
# Exit code: 0

# 如果子进程还需要输入，则可以通过communicate()方法输入：

print('=='*50)
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print('Exit code:', p.returncode)

# 上面的代码相当于在命令行执行命令nslookup，然后手动输入：

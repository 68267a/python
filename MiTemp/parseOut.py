#!/usr/bin/python3
from datetime import datetime
import subprocess, os

cmd = 'python dummy.py'
# cmd = './LYWSD03MMC.py -p -c 0 > out.txt'

def runcmd(cmd):
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,env={'PATH': os.getenv('PATH')})
	out, err = p.communicate() 
	result = out.decode('utf-8').split('\n')
	for lin in result:
		if not lin.startswith('#'):
			print(lin)

####################################

file = open('out.txt')
content = file.readlines()

results = {'time':datetime.now().replace(microsecond=0).isoformat()}
results.update({'device':content[-8].split()[4]})
results.update({'temp':content[-7].split(':')[1].strip()})
results.update({'humidity':content[-6].split(':')[1].strip()})
results.update({'batvolt':content[-5].split(':')[1].split()[0]})
results.update({'rssi':content[-4].split(':')[1].split()[0]})
results.update({'battery':content[-3].split(':')[1].split()[0]})

### device location
devices = {
	'attic':'A4:C1:38:AB:2A:9A'
}
room = [k for k,v in devices.items() if v == results['device']][0]
results.update({'room':room})
print(results)


# {'time': '2022-05-05T19:13:23', 'Temperature': '70.3', 'Humidity': '58', 'Battery voltage': '2.878 V', 'RSSI': '-69 dBm', 'Battery': '74 %'}
# time, temperature, humidity, battery voltage, rssi, battery

# todo:
		# run command
		# create table
		# update table
		# create cron
		# grafana container, source, dashboard, panel
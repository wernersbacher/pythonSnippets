"""
run a speedtest with speedtest-cli and save the results into a csv file.

"""

import os
import re
import subprocess
import time

# FILE PATH
csv_path = "/home/pi/speedtest"


csv_filename = "speedtest_{}.csv".format(time.strftime('week%V-year%y'))
abs_csv_path = os.path.join(csv_path, csv_filename)

print("Starting up speedtest script...")

os.mkdir(csv_path)

response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
print(response)

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

ping = ping[0].replace(',', '.')
download = download[0].replace(',', '.')
upload = upload[0].replace(',', '.')

#print(ping)
#print(download)
#print(upload)

with open(abs_csv_path, "a+") as f:
	if os.stat(abs_csv_path).st_size == 0:
		f.write('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\r\n')
	# write to file
	f.write('{},{},{},{},{}\r\n'.format(time.strftime('%d/%m/%Y'), time.strftime('%H:%M'), ping, download, upload))

	print("Wrote results to file: "+abs_csv_path)
	

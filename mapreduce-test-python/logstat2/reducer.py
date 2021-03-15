#!/usr/bin/python
from operator import itemgetter
import sys

dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    try:
        num = int(num)
        dict_ip_count[ip] = dict_ip_count.get(ip, 0) + num

    except ValueError:
        pass


sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0))
dic={}
L=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for ip, count in sorted_dict_ip_count:   
    for i in range(24):
       j='0'+str(i)
       if ip[1]==j[-2]&ip[2]==j[-1]&L[i]<4:
          dic[ip]=count
          L[i]=L[i]+1
    
for ip, count in dic:
    print ('%s\t%s' % (ip, count))

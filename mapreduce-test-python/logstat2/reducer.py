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

for key, value in sorted_dict_ip_count.items():   
    for i in range(24):
       j='0'+str(i)
       if (key[1]==j[-2])&(key[2]==j[-1])&(L[i]<3):
          dic[key]=value
          L[i]=L[i]+1
    
for key, value in dic.items():
    print ('%s\t%s' % (key,value))

from netaddr import IPNetwork
import urllib.request
import random
import os.path
import socket
import threading


def method():
    c = input("Enter method number :\n 1-socks4 \n 2-http(80)\n 3-http(8080)\n -> Default is socks4\n  ")
    c=int(c)
    if(c==1):
        return 1
    elif(c==2):
        return 2
    elif(c==3):
        return 3        
    else:
        print('wrong number, using Default method')
        return 1
       

method_chosen = method()

def work_with_ips():
    with open("ips.txt","r") as inp:
      ipranges = inp.readlines()
    random_range = random.choice(ipranges)
    print('selected random range is:',random_range)
    with open("selected_ip_range.txt","a") as inp:
        for ip in IPNetwork(random_range):
            ip = str(ip)
            inp.write((ip))
            inp.write('\n')
    print("ip list created successfully")



def is_ips_port_open(ip):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        print(ip)
        if(method_chosen==1):
            return s.connect_ex((ip,4145)) == 0       
        elif(method_chosen==2):
            return s.connect_ex((ip,80)) == 0
        elif(method_chosen==3):
            return s.connect_ex((ip,8080)) == 0
        else:
            print("eroooooooooooooooooooooooooooooooooooooooor")    


def check_alive_ips(count,ip):
    conn = is_ips_port_open(ip)
    if(conn):
        count+=1
        print ("Port is open for :))))))))))",ip)
        with open("ips_with_open_ports.txt","a") as inp:
            ip=str(ip)
            if(method_chosen==1):
                methdname = 'socks4'
            if(method_chosen==2):
                methdname = 'http(80)'
            if(method_chosen==3):
                methdname = 'http(8080)'        
            inp.write(methdname)
            inp.write('://')            
            inp.write(ip)
            inp.write('\n')
    else:
        print ("Port is not open for ",ip)
        print("======================================")
    return count            


def ips2array():
    f = open('selected_ip_range.txt','r')
    lines = f.read().splitlines()
    f.close()
    return lines

def check_One_By_One(iparray):
    for ips in iparray:
        count_alive = check_alive_ips(0,ips)
    return count_alive 

def multi_ip(iparray):
    splitlen = len(iparray)//8
    print('split len is ', splitlen)
    t1 = threading.Thread(target=check_One_By_One, args=(iparray[:splitlen],))
    t1.start()

    t2 = threading.Thread(target=check_One_By_One, args=(iparray[splitlen:2*splitlen],))
    t2.start()

    t3 = threading.Thread(target=check_One_By_One, args=(iparray[2*splitlen:3*splitlen],))
    t3.start()

    t4 = threading.Thread(target=check_One_By_One, args=(iparray[3*splitlen:4*splitlen],))
    t4.start()

    t5 = threading.Thread(target=check_One_By_One, args=(iparray[4*splitlen:5*splitlen],))
    t5.start()

    t6 = threading.Thread(target=check_One_By_One, args=(iparray[5*splitlen:6*splitlen],))
    t6.start()

    t7 = threading.Thread(target=check_One_By_One, args=(iparray[6*splitlen:7*splitlen],))
    t7.start()

    t8= threading.Thread(target=check_One_By_One, args=(iparray[7*splitlen:8*splitlen],))
    t8.start()
def main():
        if os.path.isfile('selected_ip_range.txt'):
            os.remove("selected_ip_range.txt")
        work_with_ips()
        iparray = ips2array()
        multi_ip(iparray)

print("===========================================================")
print("Iran Proxy BY Nic")
print("===========================================================")
if os.path.isfile('ips_with_open_ports.txt'):
    alive_num = sum(1 for line in open('ips_with_open_ports.txt'))
else:
    alive_num = 0
print('alive num is',alive_num)
while (alive_num<100):
    main()
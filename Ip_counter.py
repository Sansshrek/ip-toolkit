import math
from Converter import convert_bin, bin_to_dec

def normal_address(ip_list):
    print("\nIFORMAZIONI")
    for i in range(len(ip_list)):
        print(f"Rete {str(i+1)}: {str(ip_list[i])} IP")
    
    cont = 0
    print("\nRete | Primo IP      | Ultimo IP     |")
    for i in range(len(ip_list)):
        cont += 1
        #--- Rete
        print(i+1,end="")
        if (i+1)<100:  # if number is less than 100 add a space
            print(" ",end="")
        if (i+1)<10:   # if number is less than 10 add a space
            print(" ",end="")
        #--- Primo IP
        print("  | 192.168.1."+str(cont),end="")
        if cont<100:   # if number is less than 100 add a space
            print(" ",end="")
        if cont<10:    # if number is less than 10 add a space
            print(" ",end="")
        print(" | ",end="")
        #--- Ultimo IP
        cont += (ip_list[i]-1)
        print("192.168.1."+str(cont),end="")
        if cont<100:   # if number is less than 100 add a space
            print(" ",end="")
        if cont<10:    # if number is less than 10 add a space
            print(" ",end="")
        print(" |")

def free_address(ip_list):
    num_free = int(input("\nInserire numero ip liberi: "))
    print("\nIFORMAZIONI")
    for i in range(len(ip_list)):
        print(f"Rete {str(i+1)}: {str(ip_list[i])} IP, {str(num_free)} IP Liberi")
    
    cont = 0
    print("\nRete | Primo IP      | Ultimo IP     | IP Liberi                    |")
    for i in range(len(ip_list)):
        cont += 1
        #--- Rete
        print(i+1,end="")
        if (i+1)<100:  # if number is less than 100 add a space
            print(" ",end="")
        if (i+1)<10:   # if number is less than 10 add a space
            print(" ",end="")
        #--- Primo IP
        print("  | 192.168.1."+str(cont),end="")
        if cont<100:   # if number is less than 100 add a space
            print(" ",end="")
        if cont<10:    # if number is less than 10 add a space
            print(" ",end="")
        print(" | ",end="")
        #--- Ultimo IP
        cont += (ip_list[i]-1)
        print("192.168.1."+str(cont),end="")
        if cont<100:   # if number is less than 100 add a space
            print(" ",end="")
        if cont<10:    # if number is less than 10 add a space
            print(" ",end="")
        print(" | ",end="")
        #--- IP liberi 1
        cont += 1
        print("192.168.1."+str(cont),end="")
        if cont<100 :  # if number is less than 100 add a space
            print(" ",end="")
        if cont<10 :   # if number is less than 10 add a space
            print(" ",end="")
        print(" - ",end="")
        #--- IP liberi 2
        cont += num_free-1
        print("192.168.1."+str(cont),end="")
        if cont<100 :  # if number is less than 100 add a space
            print(" ",end="")
        if cont<10 :   # if number is less than 10 add a space
            print(" ",end="")
        print(" |")

def subnet_address(ip_list):
    print("\nIFORMAZIONI")
    for i in range(len(ip_list)):
        print(f"Rete {str(i+1)}: {str(ip_list[i])} IP")
    
    cont = 0
    print("\nRete | Primo IP      | Ultimo IP    |")
    for i in range(len(ip_list)):
        #--- Rete
        print(i+1,end="")
        if (i+1)<100 :  # if number is less than 100 add a space
            print(" ",end="")
        if (i+1)<10 :   # if number is less than 10 add a space
            print(" ",end="")
        #--- Primo IP
        print(f"  | 172.16.{str(i+1)}.100",end="")
        print("  | ",end="")
        #--- Ultimo IP
        print(f"172.16.{str(i+1)}.{str(ip_list[i]+99)}",end="")
        print(" |")

def binary_address(ip_list):
    exp = []
    for i in range(len(ip_list)):
        e = 0
        while True:
            n = pow(2, e)
            if ip_list[i] < n:
                exp.append(n)
                break
            e += 1
    
    print("\nIFORMAZIONI")
    for i in range(len(ip_list)):
        print(f"Rete {str(i+1)}: {str(ip_list[i])} IP, bin = 2^{str(math.log(exp[i], 2))} = {str(exp[i])}")

    cont=0
    print("\nRete | Primo IP      | Ultimo IP     | IP Liberi                     |")
    for i in range(len(ip_list)):
        cont += 1
        #--- Rete
        print(i+1,end="")
        if (i+1)<100 :  # if number is less than 100 add a space
            print(" ",end="")
        if (i+1)<10 :   # if number is less than 10 add a space
            print(" ",end="")
        #--- Primo IP
        print("  | 192.168.1."+str(cont),end="")
        if cont<100 :  # if number is less than 100 add a space
            print(" ",end="")
        if cont<10 :   # if number is less than 10 add a space
            print(" ",end="")
        print(" | ",end="")
        #--- Ultimo IP
        cont += (ip_list[i]-1)
        print("192.168.1."+str(cont),end="")
        if cont<100 :  # if number is less than 100 add a space
            print(" ",end="")
        if cont<10 :   # if number is less than 10 add a space
            print(" ",end="")
        print(" | ",end="")
        #--- IP liberi 1
        cont += 1
        print("192.168.1."+str(cont),end="")
        if cont<100 :  # if number is less than 100 add a space
            print(" ",end="")
        if cont<10 :   # if number is less than 10 add a space
            print(" ",end="")
        print(" - ",end="")
        #--- IP liberi 2
        left = exp[i] - ip_list[i]
        cont += left-1
        print("192.168.1."+str(cont),end="")
        if cont<100 :  # if number is less than 100 add a space
            print(" ",end="")
        if cont<10 :   # if number is less than 10 add a space
            print(" ",end="")
        print(" |")

def get_netmask_info(subnet):
    # return /number of hosts/bit per host/bit per subnet 
    if subnet == 2:
        return 126, 7, 1
    elif subnet == 4:
        return 62, 6, 2
    elif subnet == 8:
        return 30, 5, 3
    elif subnet == 16:
        return 14, 4, 4
    elif subnet == 32:
        return 6, 3, 5
    elif subnet == 64:
        return 2, 2, 6

def subnet(ip_list):
    net_num = len(ip_list)
    if net_num <= 64:
        e = subnet_max = 0
        while True:
            n = pow(2, e)
            if net_num <= n:
                subnet_max = n
                break
            e += 1
        host_max, host_bit, sub_bit = get_netmask_info(subnet_max)
        check_first = True
        print("\nRete | subnet"+("    "*(sub_bit-2))+"| host  "+("    "*(host_bit-2))+"|       IP      |")
        print("     | 1°| 2°| 3°| 4°| 5°| 6°| 7°| 8°|")
        for i in range(len(ip_list)):
            print()
            first_ip_bin = last_ip_bin = first_ip = last_ip = start_value = 0
            last_value = ip_list[i]-1
            if check_first: # ip host in the first subnet start from 1 and end at *number of ip*
                start_value = 1 # else it start from 0 and end at *number of ip* - 1
                last_value = ip_list[i]
            first_ip_bin = convert_bin(i, sub_bit) + convert_bin(start_value, host_bit) # subnet binary value plus host binary value
            last_ip_bin = convert_bin(i, sub_bit) + convert_bin(last_value, host_bit)
            first_ip = bin_to_dec(int(first_ip_bin))
            last_ip = bin_to_dec(int(last_ip_bin))
            check_first = False
            print("First ip bin = "+first_ip_bin+", to dec = "+str(first_ip))
            print("Last ip bin = "+last_ip_bin+", to dec = "+str(last_ip))
            #--- Rete
            print(f" {str(i+1)} ",end="")
            if (i+1)<100 :  # if number is less than 100 add a space
                print(" ",end="")
            if (i+1)<10 :   # if number is less than 10 add a space
                print(" ",end="")
            #--- binary first ip
            for bin_value in first_ip_bin[:(sub_bit)]:
                print(f"| {bin_value} ",end="")
            for bin_value in first_ip_bin[(sub_bit):]:
                print(f"| {bin_value} ",end="")
            #--- first ip
            print(f"| 192.168.1.{str(first_ip)} ",end="")
            if first_ip < 100:
                print(" ",end="")
            if first_ip < 10:
                print(" ",end="")
            print("|")
            #--- binary last ip
            print("     ",end="")
            for bin_value in last_ip_bin[:(sub_bit)]:
                print(f"| {bin_value} ",end="")
            for bin_value in last_ip_bin[(sub_bit):]:
                print(f"| {bin_value} ",end="")
            #--- last ip
            print(f"| 192.168.1.{str(last_ip)} ",end="")
            if last_ip < 100:
                print(" ",end="")
            if last_ip < 10:
                print(" ",end="")
            print("|")

    else:
        print("\nImpossibile calcolare la subnet mask")
from Converter import dec_to_bin

def separate_subnet(netmask):
    check = True
    num_sub = num_host = 0
    if netmask == 0:
        num_host = 255
    elif netmask == 128:
        num_sub = 2
        num_host = 126
    elif netmask == 192:
        num_sub = 4
        num_host = 62
    elif netmask == 224:
        num_sub = 8
        num_host = 30
    elif netmask == 240:
        num_sub = 16
        num_host = 14
    elif netmask == 248:
        num_sub = 32
        num_host = 6
    elif netmask == 252:
        num_sub = 64
        num_host = 2
    else:
        check = False
    return check, num_sub, num_host

def print_subnet_netmask():
    netmask = [128, 192, 224, 240, 248, 252]
    for i in netmask:
        check, sub, host = separate_subnet(i)
        print(f"\n-255.255.255.{str(i)}:\nSubnet = {str(sub)}\nHost = {str(host)}")
 
def print_subnet_info(subnet_str):
    splitted_sub = subnet_str.split(".")
    if len(splitted_sub) != 4:
        print("\nSubnet mask inserita non riconosciuta")
    else:
        subnet_class = ""
        if int(splitted_sub[3]) >= 0 and int(splitted_sub[3]) < 256:  # check if netmask is possible
            if splitted_sub[0] == "255" and splitted_sub[1] == "0" and splitted_sub[2] == "0":  # 255.0.0.x
                subnet_class = "A"
            elif splitted_sub[0] == "255" and splitted_sub[1] == "255" and splitted_sub[2] == "0":  # 255.255.0.x
                subnet_class = "B"
            elif splitted_sub[0] == "255" and splitted_sub[1] == "255" and splitted_sub[2] == "255":  # 255.255.255.x
                subnet_class = "C"
            else:
                print("\nSubnet mask inserita non riconosciuta")
        else:
            print("\nValore subnet mask errato")
        if subnet_class != "":
            check, n_sub, n_host = separate_subnet( int(splitted_sub[3]) ) # get number of hosts and subnets
            if check:
                print(f"\n-Subnet mask di class {str(subnet_class)}\n-Numero di subnet: {str(n_sub)}\n-Numero di Host: {str(n_host)}")
                print(f"\nSubnet mask binaria: {str( dec_to_bin( int(splitted_sub[0])))}.{str( dec_to_bin( int(splitted_sub[1])))}.{str( dec_to_bin( int(splitted_sub[2])))}.{str( dec_to_bin( int(splitted_sub[3])))}")
            else:
                print("\nValore netmask non riconosciuto")

def print_ip_info(ip_str):
    splitted_ip_str = ip_str.split(".")
    if len(splitted_ip_str) != 4:
        print("\nIp inserito non riconosciuto")
    else:
        splitted_ip = []
        for i in splitted_ip_str:
            splitted_ip.append( int(i) )
        ip_class = start = end = subnet = forma = ""
        if dec_to_bin( splitted_ip[0]) == "00000000" or dec_to_bin( splitted_ip[0]) == "11111111":
            print("\nIp non valido")
        if splitted_ip[0] >=1 and splitted_ip[0] <= 127 and splitted_ip[1] >= 0 and splitted_ip[1] <= 255 and splitted_ip[2] >= 0 and splitted_ip[2] <= 255 and splitted_ip[3] >= 0 and splitted_ip[3] <= 255:
            ip_class = "A"
            start = "1.0.0.0"
            end = "127.255.255.255"
            subnet = "255.0.0.0"
            forma = "1-127.Host.Host.Host"
        elif splitted_ip[0] >=128 and splitted_ip[0] <= 191 and splitted_ip[1] >= 0 and splitted_ip[1] <= 255 and splitted_ip[2] >= 0 and splitted_ip[2] <= 255 and splitted_ip[3] >= 0 and splitted_ip[3] <= 255:
            ip_class = "B"
            start = "128.0.0.0"
            end = "191.255.255.255"
            subnet = "255.255.0.0"
            forma = "128-191.Rete.Host.Host"
        elif splitted_ip[0] >=192 and splitted_ip[0] <= 223 and splitted_ip[1] >= 0 and splitted_ip[1] <= 255 and splitted_ip[2] >= 0 and splitted_ip[2] <= 255 and splitted_ip[3] >= 0 and splitted_ip[3] <= 255:
            ip_class = "C"
            start = "192.0.0.0"
            end = "223.255.255.255"
            subnet = "255.255.255.0"
            forma = "192-223.Rete.Rete.Host"
        elif splitted_ip[0] >=224 and splitted_ip[0] <= 239 and splitted_ip[1] >= 0 and splitted_ip[1] <= 255 and splitted_ip[2] >= 0 and splitted_ip[2] <= 255 and splitted_ip[3] >= 0 and splitted_ip[3] <= 255:
            ip_class = "D"
            start = "224.0.0.0"
            end = "239.255.255.255"
            forma = "224-239.X.X.X"
        elif splitted_ip[0] >=240 and splitted_ip[0] <= 255 and splitted_ip[1] >= 0 and splitted_ip[1] <= 255 and splitted_ip[2] >= 0 and splitted_ip[2] <= 255 and splitted_ip[3] >= 0 and splitted_ip[3] <= 255:
            ip_class = "E"
            start = "240.0.0.0"
            end = "255.255.255.255"
            forma = "240-255.X.X.X"
        else:
            print("\nIp inserito non riconosciuto")
        if ip_class != "":
            print(f"\n-IP di classe {ip_class}\n-Inizio intervallo: {start}\n-Fine intervallo: {end}\n-Forma utilizzo: {forma}")
            if ip_class == "A" or ip_class == "B" or ip_class == "C":
                print(f"\n-Subnet mask classe {ip_class}: {subnet}")
            print(f"\nIp binario: {dec_to_bin( int(splitted_ip[0]))}.{dec_to_bin( int(splitted_ip[1]))}.{dec_to_bin( int(splitted_ip[2]))}.{dec_to_bin( int(splitted_ip[3]))}")


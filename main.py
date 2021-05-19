from Ip_information import *
from Ip_counter import *
from Converter import *

while True:
    print("""
    Opzione 1: Convertire da Binario a Decimale
    Opzione 2: Convertire da Decimale a Binario
    Opzione 3: Informazioni su ip
    Opzione 4: Informazioni su Subnet Mask
    Opzione 5: Informazioni sulla netmask
    Opzione 6: Indirizzamento rete
    Opzione 0: Esci dal programma
    """)
    choice = int(input("\nInserire valore per scegliere opzione: "))
    if choice == 0:
        print("\n---Uscendo dal programma---")
        break
    elif choice == 1:
        check = False
        while check == False:
            bin_str = input("\nInserire stringa binaria: ")
            check = check_bin(bin_str)
        dec = bin_to_dec(int(bin_str))
        print(f"\nIl valore {str(bin_str)} in decimale diventa: {str(dec)}")
    elif choice == 2:
        dec = int(input("\nInserire valore decimale: "))
        bin_value = dec_to_bin(dec)
        print(f"\nIl valore {str(dec)} in binario diventa: {str(bin_value)}")
    elif choice == 3:
        ip = input("\nInserire ip (o 0 se non si vuole inserire): ")
        print_ip_info(ip)
    elif choice == 4:
        subnet_input = input("\nInserire subnet mask (o 0 se non si vuole inserire): ")
        print_subnet_info(subnet_input)
    elif choice == 5:
        print_subnet_netmask()
    elif choice == 6:
        ip_info = []
        num_net = int(input("\nInserire numero reti: "))
        for i in range(num_net):
            print("\nInserire numero ip in rete "+str(i+1))
            ip = int(input())
            ip_info.append(ip)
        while True:
            print("""
            Funzionamento solo con Classe C (tranne le sottoreti che utilizzando Classe D) 
            \nInserire valore per scegliere l'indirizzamento
            Opzione 1: Indirizzamento normale
            Opzione 2: Indirizzamento con ip liberi
            Opzione 3: Indirizzamento con sottoreti
            Opzione 4: Indirizzamento binario
            Opzione 5: Indirizzamento subnet
            Opzione 6: Stampa lista ip
            Opzione 7: Aggiungi rete
            Opzione 8: Elimina rete
            Opzione 9: Modifica ip rete
            Opzione 0: Esci dall'indirizzamento
            """)
            addressing = int(input("Inserire valore: "))
            if addressing == 0:
                print("\n---Uscendo dall'indirizzamento---")
                break
            elif addressing == 1:
                normal_address(ip_info)
            elif addressing == 2:
                free_address(ip_info)
            elif addressing == 3:
                subnet_address(ip_info)
            elif addressing == 4:
                binary_address(ip_info)
            elif addressing == 5:
                subnet(ip_info)
            elif addressing == 6:
                for i in range(len(ip_info)):
                    print(f"Rete {str(i+1)}: {str(ip_info[i])} IP")
            elif addressing == 7:
                ip_num = int(input(f"\nInserire numero ip da aggiungere nella rete {str(len(ip_info))}: "))
                ip_info.append(ip_num)
            elif addressing == 8:
                ip_rem = int(input("\nInserire numero rete da eliminare: "))
                if ip_rem > len(ip_info) or ip_rem < 1:
                    print("\nLa rette inserita non esiste")
                else:
                    del ip_info[ip_rem-1]
            elif addressing == 9:
                net_num = int(input("\nInserire numero rete da modificare: "))
                if net_num > len(ip_info) or net_num < 1:
                    print("\nLa rette inserita non esiste")
                else:
                    print(f"Dati rete {str(net_num)}: {str(ip_info[net_num-1])} IP")
                    ip_num = int(input("\nInserire numero Ip nuovo: "))
                    ip_info[net_num-1] = ip_num
            else:
                print("\nScelta inesistente")
    else:
        print("\nInserire valore corretto")
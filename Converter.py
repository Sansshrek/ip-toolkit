def bin_to_dec(bin_value):
    dec = i = 0
    while bin_value > 0:
        if int(bin_value%10) == 1:
            dec = dec + pow(2, i)
        bin_value = bin_value//10
        i += 1
    return dec

def dec_to_bin(dec_value):
    bin_str = str( bin(dec_value) )
    bin_str = bin_str[2:]
    for i in range(8-len(bin_str)):
        bin_str = "0" + bin_str
    return bin_str

def convert_bin(dec_value, bit_num): # used in subnet counting
    bin_str = str( bin(dec_value) )
    bin_str = bin_str[2:]
    for i in range(bit_num-len(bin_str)):
        bin_str = "0" + bin_str
    return bin_str

def check_bin(bin_str):
    check = True
    for i in bin_str:
        if i != "0" and i != "1":
            check = False
    if not check:
        print("\nInserire valori binari corretti")
    return check
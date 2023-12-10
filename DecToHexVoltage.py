from math import ceil


def hex_out_result(vhexadc, voutaop , vcmd):
    vadc = int(vhexadc)

    return (vadc*vcmd)/voutaop



def main():
#    print(hex(50))  
    vout_aop = input("Tension en sortie de l'aop controle en courant (mV) : ")
    vout_aop = int(vout_aop)

    v_hex_adc = input("Tension en sortie de l'ADC (en hex): ")
    try:
        v_hex_adc = int(v_hex_adc, 16)  # interpret the input as a base-16 number, a hexadecimal.
    except ValueError:
        print("You did not enter a hexadecimal number!")
    

    v_cmd = input("Tension desiree en sortie de l'aop controle en courant (en mV) : ")
    v_cmd = int(v_cmd)

    result_cmd = hex_out_result(v_hex_adc, vout_aop, v_cmd)
    print(ceil(result_cmd))




if __name__ == "__main__":
   main()


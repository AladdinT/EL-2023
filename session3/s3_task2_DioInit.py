'''
Session 3
Task :
    Write python code to generate Init function of GPIO for AVR
'''

print("Choose each pin direction configuration (I/O) ")
in_poss =  ['in','input','i','read','r', '0']
out_poss = ['out', 'output','o','write','w' , '1']
ddr = 0
for i in range(8):
    pinCfg = str(input(f'Port A Pin {i} : ')).lower().strip()
    if pinCfg in in_poss:
        ddr &=  ~(0 << (i))
    elif pinCfg in out_poss:
        ddr |=  1 << (i)
    else:
        #TODO : wanted to i-=1 but didnt work as it is in range list not actually incrementing
        pass

ddr = "{0:b}".format(ddr)

myDriver = "DIO/DIO_Program.c"
port = "PORTA"
with open(myDriver , mode="w") as f:
    f.write(f"void Init_{port}_DIR (void)\n")
    f.write("{")
    f.write(f"\n\tDDR{port[-1].capitalize()} = {ddr};\n")
    f.write("}")
    
    
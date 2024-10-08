kliensek=[]
with open('kliensek.txt','r',encoding='utf-8') as forras, \
    open('kliensek_api.txt','w',encoding='utf-8') as cel:
    halozat=forras.readline()
    for sor in forras:
            adat=sor.strip().split(',')
            pc={'Gép száma':adat[0],'IP cim':adat[1],'MAC Cím':(adat[2]),'Interface':adat[3],'statusz':adat[4]}
            kliensek.append(pc)
            print(pc,file=cel)
print(f'{kliensek}')
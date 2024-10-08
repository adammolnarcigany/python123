konyvek=[]
with open('konyvtar.txt','r',encoding='utf-8') as forras, \
    open('konyvek_api.txt','w',encoding='utf-8') as cel:
    konyvi=forras.readline()
    for sor in forras:
            adat=sor.strip().split(',')
            konyv={'iro':adat[0],'cim':adat[1],'datum':int(adat[2]),'valami sorszam':adat[3],'statusz':adat[4]}
            konyvek.append(konyv)
            print(konyv,file=cel)
print(f'{konyvek}')
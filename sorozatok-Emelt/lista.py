import os
import platform

def torles():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
torles()
sorok = []

if os.path.exists('E:\info-erettsegi felkeszito\sorozatok-Emelt\lista-1.txt'):
    fajl = open('E:\info-erettsegi felkeszito\sorozatok-Emelt\lista-1.txt', 'r')
    sorok = fajl.readlines()

else:
    print('nem talalom a fajlt')
 
#print(sorok)

datumok = []
cimek = []
reszek = []
ossz_reszek = []
latta = []

#print(len(sorok))

otodolo_cikl = 0
osztas_cikl = 5
while otodolo_cikl < len(sorok):
    while osztas_cikl > 0:
        latta.append[sorok[osztas_cikl]]
        osztas_cikl -= 4
        
    



    osztas_cikl += 5
    otodolo_cikl += 5


forrasfajl = open('10.29.txt', 'r')

adatok = []

for sor in forrasfajl:
        print(sor)
        adatok.append(sor)
        


forrasfajl.close()
print(adatok)

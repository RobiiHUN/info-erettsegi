szavak = ['asztal', 'lampa','alma']
talalat = False

for szo in szavak:
    if szo[0] == 'a' and szo[-1] == 'a':
        talalat = True
        print('Van ilyen szo!')
        break
else:
    print('Nincs ilyen szo!')
from snookerek import *

beolvas('snooker.txt')

print(f'3. feladat: A világraglistán {len(snookerek)} versenyző szerepel')

print(f'4. feladat: A versenyzők átlagosan {versenyzo_bevetel():.2f} fontot kerestek')

legjobb=legjobb_versenyzo()
print('5. feladat: A legjobban kereső versenyző:')
print(f'\tHelyezés: {legjobb_versenyzo().helyezes}')
print(f'\tNév: {legjobb_versenyzo().nev}')
print(f'\tOrszág: {legjobb_versenyzo().orszag}')
print(f'\tNyeremény összege: {legjobb_versenyzo().nyeremeny*380:,}'.replace(',',' '))

if versenyzo_keres('norveg'):
    print(f'6. feladat A versenyzők között van norvég versenyző.')
else:
    print(f'6. feladat A versenyzők között nincs norvég versenyző.')

print('7. feladat: Statisztika ')
for key,value in statisztika().items():
    if value>4:
        print(f'\t{key} {value} fő')
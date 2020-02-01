# Init comment
import pyfiglet
import time
import sys
ascii_banner = pyfiglet.figlet_format("N00T");
#https://github.com/chris-schertenlieb/besty-proposal.gii
beep = 'beep'
boop = 'boop'
ellips = '...'

print('Executing startup routine...', flush=True)
time.sleep(1)
print(beep, flush=True)
time.sleep(0.5)
print(boop, flush=True)
print(ellips, flush=True)
time.sleep(1)

print('Startup routine complete', flush=True)

print('Executing asset retrieval algorithm...', flush=True)
time.sleep(0.300)

size = 421
for i in range(size):
    sys.stdout.write("\rLoading asset file %i" % i)
    sys.stdout.flush()
    if i % 25 == 0:
        time.sleep(0.125)
    elif i % 15 == 0:
        time.sleep(0.05)
    elif i % 210 == 0:
        time.sleep(1)
    else:
        time.sleep(0.010)

print('\nDONE')
time.sleep(1)
print('\nENABLING BEST FRIEND MODE,,,', flush=True)
time.sleep(0.75)
print('AUTHORIZING WEDDING PROCEDURES...', flush=True)
time.sleep(1.5)
temp = input('PLEASE CONFIRM RETINAL IDENTITY: ')
print('\nauthorizing...', flush=True)
time.sleep(2)
print('\nAUTHORIZATION COMPLETE: ' + temp, flush=True)
time.sleep(1.5)
input('\nBEEP BEEP. PRESS ENTER TO CONTINUE. BOOP BOP.')


print(ascii_banner)
time.sleep(0.5)
print('THERE CAN BE ONLY TWO...', flush=True)

time.sleep(0.5)
print('YOU HAVE BEEN CHOSEN!', flush=True)

time.sleep(2)
print('...', flush=True)
time.sleep(2)
print('...', flush=True)
time.sleep(0.75)
print('\nWILL YOU BE MY...', flush=True)
time.sleep(0.75)
banner2 = pyfiglet.figlet_format("BEST MAN ?")
print (banner2, flush=True)
time.sleep(3)
input('pls? Y/n: ')

banner3 = pyfiglet.figlet_format('YAY')
print(banner3, flush=True)





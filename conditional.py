a = 6
boss = False
if a > 5:
    print('5 er beshi a er Mann')
    print('koto beshi hobe bolte paro? ')
elif a > 3:
    print('majamaji obosthane ace')
else:
    print('a er man 5 er ceye choto')

if boss is not True:
    print('Tel er bottle niye astece boss re tel dibo')
else:
    print('Lunch er pore asen')

coin = 'head'
# Nested conditions
if boss == True:
    print('Boss you are joss')
    if coin == 'tail':
        print('We will bowl first')
    else:
        print('Then need to bowl first')
        if 5 > 2 or boss != True:
            print('2 is smaller')
            if 8%2 == 0 and 5%2 == 1:
                print('8 is even number')
else:
    print('you are loss not a boss')
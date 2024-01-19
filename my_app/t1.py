# aa = int(input('enter the number'))
# print(aa)

while True:
    try :
        aa = float(input('enter the number'))
        break
    except ValueError:
        print('enter the valid number')


print(aa)
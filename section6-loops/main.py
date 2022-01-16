'''Section 6 Loops in Python'''

def while_loop():
    counter = 0
    while counter < 3:
        print(f'Counter: {counter}')
        counter += 1
    else:
        print('Ending while...')
        
def for_loop():
    arr = 'Hello World'
    for i in arr:
        if i == 'r':
            break
        if i == 'l':
            continue
        print(i)

def homework_6():
    '''Print the natural numbers between 0 and 10 using a while loop'''
    counter = 0
    while counter <= 10:
        print(counter)
        counter += 1

def homework_7():
    '''Print the natural numbers between 5 and 1 desc'''
    counter = 5
    while counter >= 1:
        print(counter)
        counter -= 1

if __name__ == '__main__':
    while_loop()
    homework_6()
    homework_7()
    for_loop()
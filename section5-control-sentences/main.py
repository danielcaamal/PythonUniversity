def homework_5():
    '''
        The goal of the exercise is create a rating system as follows:
        - The user will enter a number between 0 and 10
        - If the number is between 9 and 10: print "A" in the screen
        - If the number is between 8 and less than 9: print "B" in the screen
        - If the number is between 7 and less than 8: print "C" in the screen
        - If the number is between 6 and less than 7: print "D" in the screen
        - If the number is between 0 and less than 6: print "F" in the screen
        - Other values: print "Unknown value"
    '''
    value = int(input('Proporciona un valor entre 0 y 10: '))
    aux = None
    
    if 9 <= value <= 10:
        aux = 'A'
    elif 8 <= value < 9:
        aux = 'B'
    elif 7 <= value < 8:
        aux = 'C'
    elif 6 <= value < 7:
        aux = 'D'
    elif value < 6:
        aux = 'F'
    else:
        aux = 'Valor desconocido'
    
    print(aux)
        

if __name__ == '__main__':
    homework_5()
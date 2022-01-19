from models.Mouse import Mouse
from models.Keyboard import Keyboard
from models.Monitor import Monitor
from models.Computer import Computer
from models.Order import Order

def run():
    print('MOUSE')
    mouse1 = Mouse('USB','Samsung')
    print(mouse1)
    mouse2 = Mouse('Bluetooth','HP')
    print(mouse2)
    
    print('KEYBOARD')
    keyboard1 = Keyboard('USB','Logitech')
    print(keyboard1)
    
    print('MONITOR')
    monitor1 = Monitor('OMEN', '26"')
    print(monitor1)
    monitor2 = Monitor('ACCER', '25"')
    print(monitor2)
    
    print('COMPUTER')
    computer1= Computer('COMPUTER1', monitor1, keyboard1, mouse2)
    print(computer1)
    computer2= Computer('COMPUTER2', monitor2, keyboard1, mouse1)
    print(computer2)
    
    print('ORDERS')
    computers = [computer1,computer2]
    order1 = Order(computers)
    print(order1)
    
    # computer1 = Computer()


if __name__ == '__main__':
    run()
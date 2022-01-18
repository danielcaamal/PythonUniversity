from Figure import *

def run():
    
    # We cannot instance abstract classes
    # figure1 = Figure(20, 10)
    # print(figure1)
    
    triangle1 = Triangle(20, 20, 'Red')
    print(triangle1)


if __name__ == '__main__':
    run()
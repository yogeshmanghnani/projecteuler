""" This is solution to problem 15
    it is easy but requires a bit 
    of understanding. The solution 
    her is very beautifully wirtten """
    
    
def init_dictionary():
    lattice_points = {}
    for row in range(1 , 21):
        lattice_points[(row , 1)] = 1
    for coloumn in range(1, 21):
        lattice_points[(1, coloumn)] = 1
        
    return lattice_points


points = init_dictionary()

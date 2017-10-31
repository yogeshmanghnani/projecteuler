""" This is solution to problem 15
    it is easy but requires a bit 
    of understanding. The solution 
    her is very beautifully wirtten """
    
    
def init_dictionary():
    """This function initializes the dictionary
    It is returns the intialized dictionary
    It does so for 20 X 20 grid"""
    lattice_points = {}
    for row in range(21):
        lattice_points[(row , 0)] = 1
    for coloumn in range(21):
        lattice_points[(0, coloumn)] = 1
    lattice_points[(0 , 0)] = 0
        
    return lattice_points


def find_number_of_ways(lattice_points, curr_point):
    if curr_point in lattice_points.keys():
        return lattice_points[curr_point]
    else:
        print(curr_point)
        z = find_number_of_ways(lattice_points, (curr_point[0]-1, curr_point[1]))+find_number_of_ways(lattice_points, (curr_point[0], curr_point[1]-1))
        lattice_points[curr_point] = z
        return z

points = init_dictionary()
k = find_number_of_ways(points, (20, 20))
print(k)



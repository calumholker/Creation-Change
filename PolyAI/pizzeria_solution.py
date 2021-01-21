import numpy as np
import fileinput

def get_input():
    '''
    Fetch the size of city, the number of pizzerias and the pizzeria info from the input file
    '''
    inputs = [line.rstrip('\n') for line in (fileinput.input())]
    line1 = inputs[0].split()

    size = int(line1[0]) # Get dimensions of the city and validate value
    if size<1 or size>10000:
        raise Exception('Dimension of city not in range')
    
    num_pizzerias = int(line1[1]) # Get number of pizzerias and validate value
    if num_pizzerias<1 or num_pizzerias>10000:
        raise Exception('Number of pizzerias not in range')

    pizzerias = [] # Get the remaining information about each pizzeria as a list, and return as an array
    for i in range(1, num_pizzerias+1):
        pizzeria = [int(n) for n in inputs[i].split()]
        pizzerias.append(pizzeria)

    return size, num_pizzerias, pizzerias #Output array of pizzerias, the size of the city and the number of pizzerias

def get_pizzeria_matrix(size, pizzeria):
    '''
    Generates matrix of same dimensions as the city, with 1s representing locations the pizzeria can deliver to and 0s elsewhere
    '''
    y = size - pizzeria[1] # Converts row index of pizzeria to matrix row index 
    x = pizzeria[0] - 1 # Converts column index of pizzeria to matrix column index
    p_range = pizzeria[2] # Extracts the range the pizzeria can deliver pizzas

    p_matrix = np.zeros((size,size)) 
    p_matrix[y,x] = 1 # The pizza can deliver to its own coordinate

    y_min = max(y-p_range, 0) # Algorithm only checks if it can deliver pizzas in the square of radius p_range around the pizzeria 
    y_max = min(y+p_range+1, size-1)
    x_min = max(x-p_range, 0)
    x_max = min(x+p_range+1, size-1)

    for i in range(y_min, y_max): 
        for j in range(x_min, x_max):
            if (abs(i-y)+abs(j-x)) <= p_range: # For each location inside the square the program checks if it is in range
                p_matrix[i,j] = 1
    return p_matrix

if __name__ == '__main__':
    size, num_pizzerias, pizzerias = get_input() # Retrieves data
    city = np.zeros((size, size))
    for pizzeria in pizzerias:
        p_matrix = get_pizzeria_matrix(size, pizzeria) # Gets individual delivery matrix for each pizzeria
        city = city + p_matrix # Matrices are summed to get the number of delivery options for each location
    print(np.max(city))
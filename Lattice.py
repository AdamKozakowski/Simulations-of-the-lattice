import numpy as np
import copy

class Lattice:
    #Implement a square lattice L×L – the most convenient is to represent it just by an array A[i, j], i, j =
# 1, . . . ,L
    def __init__(self, size: int, p: float):
        self.size = size
        self.p = p
        # Fill up an array: ’1’ (dog) with probability p or ’0’ (empty) with probability 1−p.
        self.lat = np.array(np.random.binomial(1, p, (size,size)))

    #-------- getters -------
    def __getlat__(self):
        return self.lat
        
    def __getsize__(self):
        return self.size
    
    def __getp__(self):
        return self.p
    
    #----------methods---------
    # Use the array from the previous task and now set a flea on the very left dog in the first row on
    # the lattice – you can set ’2’ for a cell visited by the flea.
    def infect(self):
                #initial variables
        infected_lattice = copy.deepcopy(self.lat)
        size = copy.deepcopy(self.size)
        ref_infected_lattice = copy.deepcopy(infected_lattice)

        #step 1) burning top row
        for i in range(self.size):
            if infected_lattice[0][i] == 1:
                infected_lattice[0][i] = 2
        
        return infected_lattice
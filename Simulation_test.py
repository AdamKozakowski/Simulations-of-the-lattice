import Lattice
import Simulation_functions as func


my_lattice = Lattice.Lattice(5,0.5)

print(my_lattice.__getlat__())
print(my_lattice.infect())
func.visualize(my_lattice.lat, my_lattice)

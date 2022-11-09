import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.patches as patches

class particle:
    '''
    Create particle
    init:
        charge = charge of particle
        x = x position of particle
        y = y position of particle
        particles.append: add particle object to list of all particles present
    '''
    def __init__(self, charge, x, y):
        self.charge = charge
        self.x = x
        self.y = y
        particles.append(self)

    def field(self):
        '''Calculate field. X and Y are points in space to find field'''
        r = np.hypot((X-self.x), (Y-self.y))
        electricFieldMag = k*self.charge / (r**2)
        fieldX = electricFieldMag * ((X-self.x)/r)
        fieldY = electricFieldMag * ((Y-self.y)/r)
        return fieldX, fieldY



if __name__ == "__main__":
    fig, ax = plt.subplots()

    # Electric Field Constant
    k = 9e9

    # Used to choose color of circle on plot
    charge_color = {True: 'red', False: 'blue'}

    # Create grid points
    X, Y = np.meshgrid(np.linspace(-15,15,31), np.linspace(-15,15,31))

    # Store all particle objects
    particles = []

    # Create particles
    p1 = particle(charge=1, x=-5, y=-4)
    p2 = particle(charge=-1, x=10, y=-10)
    p3 = particle(charge=1, x=6, y=3)
    p4 = particle(charge=-1, x=-3, y=7)

    # Initialize total electric field
    totalFieldX = 0
    totalFieldY = 0

    # Find field from each particle and add to total
    for particle in particles:
        electricFieldX, electricFieldY = particle.field()
        totalFieldX += electricFieldX
        totalFieldY += electricFieldY
        ax.add_patch(patches.Circle((particle.x, particle.y), radius=0.2, color=charge_color[particle.charge>0]))


    ax.set_aspect('equal', adjustable='box')
    ax.streamplot(X, Y, totalFieldX, totalFieldY, density=2,  arrowsize=1.5, color=np.hypot(totalFieldX, totalFieldY))
    plt.show()



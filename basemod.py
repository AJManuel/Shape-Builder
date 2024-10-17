import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull

class Shape:
    def __init__(self, type, colour, xCoord = 0, yCoord = 0, zCoord = 0):
        self.type = type
        self.colour = colour
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.zCoord = zCoord

    def get_type(self):
        print(f"The shape is a {self.type}")
        return self.type
    
    def get_colour(self):
        print(f"This shape is {self.colour}")
        return self.colour
    
    def set_colour(self, new_colour):
        self.colour = new_colour
        return (f"This shape is now {new_colour}")

    def volume(self):
        return None

    def surfaceArea(self):
        return None
    
    def draw_shape(self):
        return None

class side0Shape(Shape):
    def __init__(self, type, colour, radius, xCoord = 0, yCoord = 0, zCoord = 0):
        super().__init__(type, colour, xCoord = 0, yCoord = 0, zCoord = 0)
        self.type = type
        self.colour = colour
        self.radi = radius
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.zCoord = zCoord
    
    def surfaceArea(self):
        area = 4 * math.pi * self.radi**2
        return area
    
    def volume(self):
        vol = (4/3) * math.pi * self.radi**3
        return vol

    
    def draw_shape(self):
        radius = self.radi
        theta, phi = np.mgrid[0:2 * np.pi:100j, 0:np.pi:50j]

        # Parametric equations for the sphere's coordinates
        x = self.xCoord + radius * np.sin(phi) * np.cos(theta)
        y = self.yCoord + radius * np.sin(phi) * np.sin(theta)
        z = self.zCoord + radius * np.cos(phi)

        # Create a 3D plot for the sphere
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the surface of the sphere
        ax.plot_surface(x, y, z, color=self.colour, alpha=0.6, edgecolors='white')

        # Set plot limits
        # ax.set_xlim([-10, 10])
        # ax.set_ylim([-10, 10])
        # ax.set_zlim([-10, 10])

        # Set labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        
        ax.set_title(f"Volume: {self.volume():0.2f}, Surface Area: {self.surfaceArea():0.2f}")

        plt.show()

class side2Shape(Shape):
    def __init__(self, type, colour, radius, height, xCoord = 0, yCoord = 0, zCoord = 0):
        super().__init__(type, colour, xCoord = 0, yCoord = 0, zCoord = 0)
        self.type = type
        self.colour = colour
        self.radi = radius
        self.height = height
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.zCoord = zCoord

    def surfaceArea(self):
        area = math.pi * self.radi * (self.radi + math.sqrt(self.height**2 + self.radi **2))
        return area
        
    def volume(self):
        volume = math.pi * self.radi**2 * (self.height/3)
        return volume
    
    def draw_shape(self):
        height = self.height
        radius = self.radi
        n_points = 50
        #x_center, y_center, z_center = self.center

        # Generate the grid for the cone
        theta = np.linspace(0, 2 * np.pi, n_points)
        z = np.linspace(self.zCoord, self.zCoord + height, n_points)
        theta, z = np.meshgrid(theta, z)

        # Parametric equations for the cone
        x = self.xCoord + radius * (height - (z - self.zCoord)) / height * np.cos(theta)
        y = self.yCoord + radius * (height - (z - self.zCoord)) / height * np.sin(theta)

        # Create a 3D plot for the cone
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the surface of the cone
        ax.plot_surface(x, y, z, color=self.colour, alpha=0.8, edgecolors='r')

        # Set plot limits
        ax.set_xlim([self.xCoord - radius, self.xCoord + radius])
        ax.set_ylim([self.yCoord - radius, self.yCoord + radius])
        ax.set_zlim([self.zCoord, self.zCoord + height])

        # Set labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_title(f"Volume: {self.volume():0.2f}, Surface Area: {self.surfaceArea():0.2f}")

        plt.show()


class side3Shape(Shape):
    def __init__(self, type, colour, radius, height, xCoord = 0, yCoord = 0, zCoord = 0):
        super().__init__(type, colour, xCoord = 0, yCoord = 0, zCoord = 0)
        self.type = type
        self.colour = colour
        self.radi = radius
        self.height = height
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.zCoord = zCoord

    def volume(self):
        vol = math.pi * self.radi**2 * self.height
        return vol
    
    def surfaceArea(self):
        area = 2 * math.pi * self.radi * self.height + 2 * math.pi * self.radi**2
        return area
    
    def draw_shape(self): 
        # Parameters for the cylinder
        height = self.height
        radius = self.radi
        n_points = 50
        #x_center, y_center, z_center = self.center

        # Generate the grid for the cylinder
        theta = np.linspace(0, 2 * np.pi, n_points)
        z = np.linspace(self.zCoord, self.zCoord + height, n_points)
        theta, z = np.meshgrid(theta, z)

        # Parametric equations for the cylinder
        x = self.xCoord + radius * np.cos(theta)
        y = self.yCoord + radius * np.sin(theta)

        # Create a 3D plot for the cylinder
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the surface of the cylinder
        ax.plot_surface(x, y, z, color=self.colour, alpha=0.7, edgecolors='r')

        # Set plot limits
        ax.set_xlim([self.xCoord - radius, self.xCoord + radius])
        ax.set_ylim([self.yCoord - radius, self.yCoord + radius])
        ax.set_zlim([self.zCoord, self.zCoord + height])

        # Set labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_title(f"Volume: {self.volume():0.2f}, Surface Area: {self.surfaceArea():0.2f}")

        plt.show()

class side4Shape(Shape):
    def __init__(self, type, colour, edge, xCoord = 0, yCoord = 0, zCoord = 0):
        super().__init__(type, colour, xCoord = 0, yCoord = 0, zCoord = 0)
        self.type = type
        self.colour = colour
        self.edge = edge
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.zCoord = zCoord

    def volume(self):
        vol = ((self.edge**3) / (6 * math.sqrt(2)))
        return vol
    
    def surfaceArea(self):
        area = math.sqrt(3) * self.edge**2
        return area
    
    def draw_shape(self):
        theHeight = np.sqrt(2 / 3) * self.edge
    
        # Vertices of a regular tetrahedron with adjustable edge length, centered at the origin
        vertices = np.array([
            [1, 1, 1],
            [-1, -1, 1],
            [-1, 1, -1],
            [1, -1, -1]
        ])
        
        # Scale the vertices by the edge length
        vertices = vertices * (self.edge / np.sqrt(2))

        # Shift the vertices to the specified center (x, y, z)
        vertices = vertices + np.array([self.xCoord, self.yCoord, self.zCoord])
        
        # Compute the convex hull of the vertices (which forms the tetrahedron)
        hull = ConvexHull(vertices)
        
        # Get the faces of the tetrahedron from the hull
        faces = [vertices[simplex] for simplex in hull.simplices]
        
        # Plot the tetrahedron
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        # Create a 3D polygon collection for the faces
        ax.add_collection3d(Poly3DCollection(faces, facecolors=self.colour, linewidths=1, edgecolors='r', alpha=0.7))
        
        # Set plot limits to accommodate the size of the tetrahedron
        ax.set_xlim([self.xCoord - self.edge, self.xCoord + self.edge])
        ax.set_ylim([self.yCoord - self.edge, self.yCoord + self.edge])
        ax.set_zlim([self.zCoord - self.edge, self.zCoord + self.edge])
        
        # Set labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_title(f"Volume: {self.volume():0.2f}, Surface Area: {self.surfaceArea():0.2f}")
        
        plt.show()

class side5ShapePrism(Shape):
    def __init__(self, type, colour, side, length, baseArea, height, xCoord = 0, yCoord = 0, zCoord = 0):
        super().__init__(type, colour, xCoord = 0, yCoord = 0, zCoord = 0)
        self.type = type
        self.colour = colour
        self.side = side
        self.length = length
        self.baseArea = baseArea
        self.height = height
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.zCoord = zCoord

    def volume(self):
        vol = (1/2) * self.side * self.length * self.height
        return vol
    
    def surfaceArea(self):
        area = (((math.sqrt(3) * self.side**2) / 2) + 3 * (self.side * self.height))
        return area
    
    def draw_shape(self):
        half_height = np.sqrt(3) / 2 * self.side
    
        # Define the vertices of the triangular prism, with offset for (x, y, z)
        vertices = np.array([
            [self.xCoord, self.yCoord, self.zCoord],                         # Vertex 1 (bottom triangle)
            [self.xCoord + self.side, self.yCoord, self.zCoord],             # Vertex 2
            [self.xCoord + self.side / 2, self.yCoord + half_height, self.zCoord],  # Vertex 3
            [self.xCoord, self.yCoord, self.zCoord + self.height],           # Vertex 4 (top triangle)
            [self.xCoord + self.side, self.yCoord, self.zCoord + self.height],  # Vertex 5
            [self.xCoord + self.side / 2, self.yCoord + half_height, self.zCoord + self.height]  # Vertex 6
        ])

        # Define the faces of the triangular prism
        faces = [
            [vertices[0], vertices[1], vertices[2]],  # Bottom triangle
            [vertices[3], vertices[4], vertices[5]],  # Top triangle
            [vertices[0], vertices[1], vertices[4], vertices[3]],  # Side 1 (rectangle)
            [vertices[1], vertices[2], vertices[5], vertices[4]],  # Side 2 (rectangle)
            [vertices[2], vertices[0], vertices[3], vertices[5]],  # Side 3 (rectangle)
        ]
    
        # Plot the triangular prism
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        # Create a 3D polygon collection for the faces
        ax.add_collection3d(Poly3DCollection(faces, facecolors=self.colour, linewidths=1, edgecolors='r', alpha=0.7))
        
        # Set plot limits to accommodate the size of the prism
        ax.set_xlim([self.xCoord - 1, self.xCoord + self.side + 1])
        ax.set_ylim([self.yCoord - 1, self.yCoord + half_height + 1])
        ax.set_zlim([self.zCoord - 1, self.zCoord + self.height + 1])
        
        # Set labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_title(f"Volume: {self.volume():0.2f}, Surface Area: {self.surfaceArea():0.2f}")
        
        plt.show()
        
class side5ShapePyramid(Shape):
    def __init__(self, type, colour, baseEdge,height, xCoord = 0, yCoord = 0, zCoord = 0):
        super().__init__(type, colour, xCoord = 0, yCoord = 0, zCoord = 0)
        self.type = type
        self.colour = colour
        self.baseEdge = baseEdge
        self.height = height
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.zCoord = zCoord

    def volume(self):
        vol = self.baseEdge**2 * (self.height / 3)
        return vol
    
    def surfaceArea(self):
        area = (self.baseEdge**2 + 2 * self.baseEdge * math.sqrt(((self.baseEdge**2)/4) + self.height**2))
        return area
    
    def draw_shape(self):
            # Half the length of the base to center the pyramid at the origin
        half_base = self.baseEdge / 2
    
        # Base will be in the XY plane, centered at (x, y) of the given center
        # x_center, y_center, z_center = center
        center = self.xCoord, self.yCoord, self.zCoord
        # Define the vertices of the square base
        base_coords = np.array([
            [self.xCoord - half_base, self.yCoord - half_base, self.zCoord],  # Bottom left corner
            [self.xCoord + half_base, self.yCoord - half_base, self.zCoord],  # Bottom right corner
            [self.xCoord + half_base, self.yCoord + half_base, self.zCoord],  # Top right corner
            [self.xCoord - half_base, self.yCoord + half_base, self.zCoord]   # Top left corner
        ])
        
        # Apex is directly above the center of the base at the specified height
        apex_coords = np.array([self.xCoord, self.yCoord, self.zCoord + self.height])

        vertices = np.vstack([base_coords, apex_coords])
    
        # Number of base vertices
        n_base = len(base_coords)
        
        # Define the faces of the pyramid
        faces = []
        
        # Triangular sides
        for i in range(n_base):
            next_i = (i + 1) % n_base  # Wrap around to the first vertex
            faces.append([base_coords[i], base_coords[next_i], apex_coords])
        
        # Square base
        faces.append(base_coords)
        
        # Plot the pyramid
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        # Create a 3D polygon collection for the faces
        ax.add_collection3d(Poly3DCollection(faces, facecolors=self.colour, linewidths=1, edgecolors='r', alpha=0.7))
        
        # Set plot limits (adjust based on the coordinates)
        ax.set_xlim([np.min(vertices[:, 0]) - 1, np.max(vertices[:, 0]) + 1])
        ax.set_ylim([np.min(vertices[:, 1]) - 1, np.max(vertices[:, 1]) + 1])
        ax.set_zlim([np.min(vertices[:, 2]) - 1, np.max(vertices[:, 2]) + 1])
        
        # Set labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_title(f"Volume: {self.volume():0.2f}, Surface Area: {self.surfaceArea():0.2f}")
        
        plt.show()

class torusShape(Shape):
    def __init__(self, type, colour, majorRadius, minorRadius, xCoord = 0, yCoord = 0, zCoord = 0):
        super().__init__(type, colour, xCoord = 0, yCoord = 0, zCoord = 0)
        self.type = type
        self.colour = colour
        self.majorRadius = majorRadius
        self.minorRadius = minorRadius
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.zCoord = zCoord

    def volume(self):
        vol = (math.pi * self.minorRadius**2) * (2 * math.pi * self.majorRadius)
        return vol
    
    def surfaceArea(self):
        area = (2 * math.pi * self.majorRadius) * (2 * math.pi * self.minorRadius)
        return area
    
    def draw_shape(self):
        # Generate the grid for torus surface
        theta = np.linspace(0, 2 * np.pi, 100)
        phi = np.linspace(0, 2 * np.pi, 100)
        theta, phi = np.meshgrid(theta, phi)

        # Parametric equations for a torus
        X = self.xCoord + (self.majorRadius + self.minorRadius * np.cos(theta)) * np.cos(phi)
        Y = self.yCoord + (self.majorRadius + self.minorRadius * np.cos(theta)) * np.sin(phi)
        Z = self.zCoord + self.minorRadius * np.sin(theta)

        # Plotting the torus
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the surface of the torus
        ax.plot_surface(X, Y, Z, color='cyan', edgecolor='black', linewidth=0.5, alpha=0.8)

        # Set plot limits
        # ax.set_xlim([-R - r, R + r])
        # ax.set_ylim([-R - r, R + r])
        # ax.set_zlim([-r, r])

        # Set labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_title(f"Volume: {self.volume():0.2f}, Surface Area: {self.surfaceArea():0.2f}")
        
        plt.show()
    

# z = side0Shape('ndf', 'blue', 4)
# print(z.volume())
# print(z.surfaceArea())
#z.draw_shape()
b = side5ShapePyramid('asfd', 'blue', 5, 5, 5, 6, 9)
print(b.volume())
print(b.surfaceArea())
#b.draw_shape()

de = side5ShapePrism('dsf', 'blue', 5, 9, 10, 84, 4, 86, 19)
#de.draw_shape()

he = torusShape("rf", "blue", 6, 5, 6, 7, 7)
print(he.surfaceArea())
print(he.volume())
#he.draw_shape()


import math
from decimal import Decimal

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def __add__(self, v):
        new_vector = []
        for i in range(self.dimension):
            new_vector.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_vector)
    
    def __sub__(self, v):
        new_vector = []
        for i in range(self.dimension):
            new_vector.append(self.coordinates[i] - v.coordinates[i])
        return Vector(new_vector)
            
    def __mul__(self, v):
        new_vector = []
        
        for i in range(v.dimension):
            mul_sum = 0
            
            for j in range(self.dimension):
                mul_sum += self.coordinates[j] * v.coordinates[i]
            
            new_vector.append(mul_sum)
            
        return Vector(new_vector)
    	
    def magnitude(self):
    	sum_sq = 0
    	for i in range(self.dimension):
    		sum_sq += self.coordinates[i] ** 2
    	
    	return math.sqrt(sum_sq)
    	
    def direction(self):
        mag = self.magnitude()
        unit_vector = Vector([1 / mag])
        return unit_vector * self

    def dot(self, v):
        dot_sum = Decimal(str(0))
        for i in range(self.dimension):
            dot_sum += Decimal(str(self.coordinates[i])) * Decimal(str(v.coordinates[i]))
        return dot_sum
    	
    def angle(self, v):
        dot_prod = self.dot(v)
        mag_prod = Decimal(str(self.magnitude() * v.magnitude()))
        return math.acos(dot_prod / mag_prod)

    def isParallelTo(self, v):
        for i in range(self.dimension):
            if (Decimal(str(v.coordinates[i])) % Decimal(str(self.coordinates[i])) != 0):
                return False
        return True

    def isOrthogonalTo(self, v):
        return self.dot(v) == 0
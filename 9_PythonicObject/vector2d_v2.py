from array import array
import math

class vector2d:
    typecode = 'd'
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    def __iter__(self):
        return (i for i in (self.x,self.y))

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=''):
            if fmt_spec.endswith('p'):
                fmt_spec = fmt_spec[:-1]
                coords = (abs(self), self.angle())
                outer_fmt = '<{}, {}>'
            else:
                coords = self
                outer_fmt = '({}, {})'
            components = (format(c,fmt_spec) for c in coords)
            return '({}{})'.format(*components)
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)   #4
    
    def __str__(self):
        return str(tuple(self))     #5
    
    def __bytes__(self):
        return(bytes([ord(self.typecode)]) + #Return byte object b'd' for typecode 'd' - instead of giving encoding we give unicode string
               bytes(array(self.typecode,self))) #7
    
    def __eq__(self, value):
        return tuple(self) == tuple(value) #8
    
    def __abs__(self):
        return math.hypot(self.x, self.y) #9
    
    def __bool__(self):
        return bool(abs(self)) #10 
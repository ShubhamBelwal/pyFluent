from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
LatLong = namedtuple('LatLong','Lat Long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889,77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
for key,value in delhi._asdict().items():
    print(key + ':', value)
delhi2 = City(*delhi_data)
print(delhi2)
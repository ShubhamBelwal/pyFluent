from clip import clip
from inspect import signature
from tag import tag

sig = signature(clip)
print(sig)
# print(dir(sig))
for name,param in sig.parameters.items():
    print(param.kind, ': ', name, '= ', param.default)

# sig = signature(tag)
# my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
# bound_args = sig.bind(**my_tag)
# print(bound_args)
# for name,value in bound_args.arguments.items():
#     print(name,' = ',value)
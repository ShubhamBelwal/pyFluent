from mirror import LookingGlass
# with LookingGlass() as what:
#     print('Alice, Kitty and Snowdrop')
#     print(what)
#     print(what)
# print(what)

manager = LookingGlass()
print(manager)
monster = manager.__enter__()
print(monster == 'JABBERWOCKY')
print(monster)
print(manager)
manager.__exit__(None, None, None)
print(monster)
print(manager)
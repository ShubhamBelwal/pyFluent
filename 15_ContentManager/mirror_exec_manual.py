from mirror import LookingGlass

manager = LookingGlass()
print("Manager: ",manager)
monster = manager.__enter__()
print("monster == 'JABBERWOCKY'", monster == "JABBERWOCKY")
print("Monster: ", monster)
print("Manager: ", manager)
manager.__exit__(None, None, None)
print("Monster after __exit__():", monster)

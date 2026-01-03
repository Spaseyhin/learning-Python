name = 'Igor'

# name[0] = 'E'  Error: 'str' object does not support item assignment
print(f'E{name[1:]}') # => 'Egor' (just fun =) )

name = 'Egor' # Reassigning the variable
print(name) # => 'Egor'
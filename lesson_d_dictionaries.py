## HASH
#   Dictionary works on non mutable object

#----------------------------------------------------------------------------------

#Dictionary. Almost always I can turn anything into a number for a dictionary

if False:
    amaterasu = dict() 
    amaterasu['aaa333'] = 'First'
    amaterasu['bbb333'] = 'Yoko'
    amaterasu['bbb334'] = 'Yoko'
    print( amaterasu['bbb334'] )

#----------------------------------------------------------------------------------

#Power of two inside a dictionary
#inside the bracket is the key. the key can be anything that is non-mutable

#create a dictionary
dict_power_of_two = dict()

for cnt in range(10):
    dict_power_of_two[2**cnt] = cnt

#I can also mix other keys
dict_power_of_two['Shaka'] = ['Walls', 'Fell']

print("Content of dictionaries",dict_power_of_two)
print("Dictionaries Keys",dict_power_of_two.keys() )
print("Dictionaries Values",dict_power_of_two.values() )
print("Dictionaries Items",dict_power_of_two.items() )

#i can iterate with for
for keys in dict_power_of_two.keys():
    keys = keys

#----------------------------------------------------------------------------------

#A set is a dictionary without keys. must be immutable
set_fruits = {"apple", "banana", "cherry", "tree" }
set_numbers = {1, 5, 7, 9, 3, "tree"}
print( "sets", set_fruits, set_numbers )

set_numbers.add( "3" )
set_numbers.remove( 5 )
print( "i can add remove elements", set_fruits, set_numbers )

print("set diff. in the first but not the second", set_fruits -set_numbers )
print("set or. in either ", set_fruits |set_numbers )
print("set xor. in either but not both", set_fruits  ^ set_numbers )
print("set and. in both", set_fruits  & set_numbers )

#----------------------------------------------------------------------------------


##  function
#   c only by value
#   python only allows by reference
#   python will search in scope upward from where it's used until it finds it
#   no return is equivalent to return None

def my_mul(a,b):
    return a*b

print("function that multiplies: ", my_mul(10,24) )

#-------------------------------------------------------    
#   default way to define the entry point of the program
#   that's because the interpreter might look at it in different moments

def main():
    return None

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    main()

#-------------------------------------------------------    
#   in python there are no cotant tags. you can have a convention CAPITAL symbols may not be touched

#-------------------------------------------------------    
#I can criss cross, i do not need prototypes. I only need execution to start at the bottom

def criss():
    cross()
    return None

def cross():
    criss()
    return None

#-------------------------------------------------------
#   I can help define what the values should be

def my_function( my_int : int ) -> int:
    return int(my_int)

print("test:", my_function( 0.0 ) )

#-------------------------------------------------------
#   Default arguments. allow to omit arguments

def my_function( my_int : int, my_float = 99.0 ) -> int:
    print("float: ", my_float)
    return int(my_int)

my_function( 10 )
my_function( 10, -10.0 )


#-------------------------------------------------------
#   Pass by reference show I can apped to the caller
#   initializer is ONLY called once. initialization shoudl only be to non mutable values

def my_appender( my_value, my_list = list() ):
    my_list.append(my_value)
    print(my_list)
    return my_list

print('Pass by reference show I can apped to the caller')
my_list = my_appender(10)
my_appender(11, my_list)
my_appender(12, my_list)
print('Weird behaviour. It keeps appending with no given list')
my_appender(40)
my_appender(41)
my_appender(42)

#a better way to handle it is to use immutables
def my_better_appender( my_value, my_list = None ):
    if (my_list == None):
        my_list = list()

    my_list.append(my_value)
    print(my_list)
    return my_list
print('Correct behaviour')

my_list = my_better_appender(10)
my_better_appender(11, my_list)
#i can use name to call default parameters
my_better_appender(12, my_list= my_list)
my_better_appender(40)
my_better_appender(41)
my_better_appender(42)

#-------------------------------------------------------
#   i can make functions inside functions

print('define function inside function')
def shell():
    def nest():
        pass
    nest()
    nest()
    pass


#-------------------------------------------------------
my_string = 'shaka'

print( "show string: ", my_string )
print( "show with repr: ", repr(my_string) )







## sorted function can be provided a key. key is a function

#original set
my_set = { 'Anna' : 13, 'Bee':90, 'Crosta': 91, 'Dee':50, 'El':55 }
print( "original set: ", my_set )

#use an helper function
def helper_comparison( word, content ):
    return len(word)
#my_sorted_set =sorted( my_set.items(), key=helper_comparison)
#print( "lambda sort by length of key and by content: ", my_sorted_set )


#sort using a lambda. length of firt paramener,, value of second parameter
my_sorted_set =sorted( my_set.items(), key=lambda e:(len(e[0]), e[1]))
print( "lambda sort by length of key and by content: ", my_sorted_set )

#----------------------------------------------------
# generate list easily from iterable objects
#   LIST COMPRHENSION

print("Generate list using range: ", [x for x in range (10)] )
print("Generate list of tuples: ", [(x, 2**x) for x in range (10)] )
print("Generate list in two dimension: ", [(x, y, x*y) for x in range (10) for y in range(2,16,3)] )
print("Generate list in two dimension with conditions: ", [(x, y, x*y) for x in range (10) for y in range(2,16,3) if x > y] )


#----------------------------------------------------
#use for sort

my_list = ['Anna', 'Astrid', 'Bee', 'Crosta', 'Dee', 'El']
print("Sort list ", sorted( [n for n in my_list]))

#----------------------------------------------------
#   generators
#   with () instead of [] is a generator. a box that will do next iteration when it's called

my_generator = ((x, y, x*y) for x in range (10) for y in range(2,16,3))

#get value
print("first step: ", next(my_generator))
print("first step: ", next(my_generator))
#generator remembers step.
print("use a generator inside a list comprenshion, i already did first: ", [ x for x in my_generator])

#----------------------------------------------------
#   generator
#   yield release control, until next call. it's a return but remember state of function

def my_yield_generator():
    n = 0
    while True:
        n += 1
        yield n

my_generator_instance = my_yield_generator()
print( "ask a value. yield return but return state", next(my_generator_instance) )
print( "ask a value. yield return but return state", next(my_generator_instance) )
print( "ask a value. yield return but return state", next(my_generator_instance) )

print(" a yield function can have a finite number of steps. if call when over it return error")
def my_finite_yield_generator():
    yield 99
    yield 'STOP!!!'

my_generator_instance = my_finite_yield_generator()
print( "ask a value. yield return but return state", next(my_generator_instance) )
print( "ask a value. yield return but return state", next(my_generator_instance) )
#third call crash because yield is over
#print( "ask a value. yield return but return state", next(my_generator_instance) )

#----------------------------------------------------
# see optimization potential

#time library
import time

#range to check
max = 20_000_000

start = time.time()
u1_res = any([x % 17 == 0 for x in range(max)])
stop = time.time()
print("if a list is used and checked, it must construct the list: ", stop-start, 's', u1_res )

start = time.time()
u1_res = any(x % 17 == 0 for x in range(max))
stop = time.time()
print("if a generator is used and checked, it stops early: ", stop-start, 's', u1_res )


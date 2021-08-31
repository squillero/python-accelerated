##
#

#-------------------------------------------------------

#del is not necessary due to garbage collector
#label = None does the same
#the garbage collector deletes things that are not referenced

#-------------------------------------------------------

data = list()
for cnt in range(10):
    data.append(cnt)

print(data)

del data[5]

print("del element of a list", data)


#-------------------------------------------------------

#copy makes shallow copies

#the list is duplicated, byt the lists point to the same elements. i can change the links
data_shallow_copy = data[:]
data_shallow_copy = data.copy()
print(data, data_shallow_copy)

list_a = [ 'a', 'b', ['c','d'] ]
list_shallow = list_a[:]

print('shallow copy: ', list_a, list_shallow)

#changing a single element does as expected
list_shallow[1] = 'x'
print('change one reference OK: ', list_a, list_shallow)

#changing a single element does as expected
list_shallow[2][0] = 'x'
print('change mutables STILL change both: ', list_a, list_shallow)

#-------------------------------------------------------

#if has ranges
value = 40
if (10 < value < 50):
    print("yes")
else:
    print("no")

#-------------------------------------------------------

#operator is

def check_is( source_a, source_b ):
    if (source_a is source_b):
        print("yes, first is second")
    else:
        print("no, first is not second")

a = 10
b = a
c = 10
check_is(a, b)
check_is(a, c)
check_is(b, c)
a = 11
check_is(a, b)
check_is(a, c)
check_is(b, c)

#-------------------------------------------------------

#if can be done with one object
u1_flag = True
if u1_flag:
    print("yes, flag is True")

str_tmp = ''
if str_tmp:
    print("yes, string has something")
else:
    print('no, string is empty')

num_tmp = 10
if num_tmp:
    print("yes, num is not zero")
else:
    print('no, num is zero')

list_temp = list()
if list_temp:
    print("yes, list is not empty")
else:
    print('no, list is empty')





#-------------------------------------------------------    
## generator that spit out one number of the fibonacci sequence one at a time
def my_fibonacci_generator():
    #spit out first element
    yield 0
    #spit out second element
    yield 1
    f_minus2 = 0
    f_minus1 = 1
    #loop
    while True:
        #compute current state
        f_now = f_minus1 +f_minus2
        #update memory states
        f_minus2 = f_minus1
        f_minus1 = f_now
        #spit out next element
        yield f_now

## main
def main():
    #instance the generator
    #my_instance = my_fibonacci_generator()
    #ask the generator to spit out 10 numbers of the fibonacci sequence
    #for cnt in range(10):
        #show sequence
        #print(f"fibonacci {cnt} -> {next(my_instance)}")
    #print(f"fibonacci {cnt} -> {next(my_instance)}")
    
    #create a list using zip. zip ends when an iterator ends. otherwise fibonacci would get stuck
    my_fibonacci_sequence = [item for item in zip(range(10), my_fibonacci_generator())]
    print(my_fibonacci_sequence)
    



#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    main()
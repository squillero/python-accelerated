## prime factor
# function that return the prime factors

def factorize( my_source : int ) -> list():
    #make int
    value = int(my_source)
    #initialize factor list
    my_factors = list()
    #init while
    cnt = 2
    while cnt <= value:
        #if: I found a factor
        if (value % cnt) == 0:
            #print(value % cnt, value, cnt)
            #divide by the factor
            value //= cnt
            #print(value)
            #add factor to the list
            my_factors.append(cnt)
        
        else:
            #next test factor
            cnt+=1
    
    if not my_factors:
        my_factors.append(value)

    print(my_source, my_factors)
    return my_factors

def main():
    factorize(1)
    factorize(42)
    factorize(100)
    factorize(13)
    factorize(10000)
    factorize(9999)
    factorize(128)

    return None

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    main()
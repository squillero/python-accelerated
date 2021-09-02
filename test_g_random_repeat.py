#NOTE: done with convert to string and str.find is much faster due to better builtin find

#python modules
import logging
import time as lib_time
import random as lib_random

##
#   measure how long it takes for a sequence of a given length to repeat
#   length of repeat sequence
#   min
#   max
#   seed
def measure_repeat( min : int, max : int, length : int ) -> int:
    
    #initialize sequence list
    my_sequence = list()
    #while a repeat is not found
    while True:
        #generate a random number
        temp = lib_random.randint(min, max)
        #add the number to a sequence
        my_sequence.append( temp )
        #check if adding the number causes a repeat
        index = is_repeat( my_sequence, length )
        if index >= 0:
            logging.info(f'length: {len(my_sequence)}')
            logging.info(f'index: {index}')
            logging.info(f'sequence: {my_sequence}')
            return len(my_sequence)
        else:
            pass
    
    return 0

##  check if the last {sequence_length} symbols inside a sequence are repeated somewhere else in the sequence
#   
def is_repeat( source_sequence : list(), sequence_length : int ) -> int:

    #if source sequence is too short
    if sequence_length >= len(source_sequence):
        #cannot repeat
        return -1

    #generate the mask sequence
    mask = list()
    mask[0:sequence_length] = source_sequence[-sequence_length:]
    #generate the seek sequence
    seek = list()
    seek[0:len(source_sequence)-sequence_length] = source_sequence[0:len(source_sequence)-sequence_length]

    #debug
    logging.debug(f'mask: {mask} | seek: {seek}')

    #check if mask is inside seek
    index = seq_in_seq(mask, seek)
    if (index >= 0):
        logging.info(f'found sequence: {mask}')
        logging.debug(f'in sequence: {seek}')
        logging.debug(f'at index: {index}')
        return index    

    return -1

## see if a sub sequence is inside a master sequence. return index of repeat if any
#
def seq_in_seq(subseq, seq):
    while subseq[0] in seq:
        index = seq.index(subseq[0])
        if subseq == seq[index:index + len(subseq)]:
            return index
        else:
            seq = seq[index + 1:]
    else:
        return -1

## main
def main():

    start = lib_time.time()
    #make sure the seed is the same for all
    my_seed = 42
    lib_random.seed(my_seed)
    logging.info(f'seed: {my_seed}')

    #test submodule
    #print(is_repeat( [5, 7, 3, 5, 7] , 2 ))

    #execute
    sequence_length = measure_repeat( 0, 100, 2 )
    print('', sequence_length)

    stop = lib_time.time()
    print(f'elapsed time: {stop - start}')
    pass

#if the file is being read WITH the intent of being executed
if __name__ == '__main__':
    logging.basicConfig(
        #level of debug to show
        level=logging.INFO,
        #header of the debug message
        format='[%(asctime)s] %(levelname)s: %(message)s',
    )
    main()
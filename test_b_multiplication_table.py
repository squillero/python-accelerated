##  @package multiplication table
#ask for a number
#print the multiplication table for theat number
#square

#ask user for number
user_str = input('Gimme NUMBER!')
user_num = int(user_str)
assert(user_num >0), f"... DVMMY!"
#activate header
u1_header = True
#scan mul factors on rows
for num_row in range(1, user_num+1 +1):

    #if print header mode
    if u1_header == True:
        print(f" \t",end='')
    #if print row header
    else:
        #print row header
        print(f"{int(num_row-1)}\t",end='')
    
    #scan mul factors on cols
    for num_col in range(1, user_num+1):
        if u1_header == True:
            print(f"| {int(num_col)}\t",end='')
        else:
            #print row header
            print(f"| {int(num_row-1) *int(num_col)}\t",end='')
            
    #deactivate header mode
    u1_header = False

    #end row
    print("\n")

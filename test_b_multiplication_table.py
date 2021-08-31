##  @package multiplication table
#ask for a number
#print the multiplication table for theat number

#ask user for number
user_num = input("Gimme NUMBER!")
#scan mul factor
for cnt in range(1, 10+1):
    #print the multiplication table
    print(f"{int(user_num)}\t*\t{int(cnt)}\t= {int(user_num) *int(cnt)}")

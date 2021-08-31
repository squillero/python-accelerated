#-------------------------------------------------------    

#while just like C

cnt = 0
while (cnt < 20):
    #next
    cnt+=1

    if (cnt == 0):
        #it's a special statement that allow a blank
        pass

    if (cnt == 17):
        #for special case do not make processing and restart from beginning
        continue

    if (cnt > 19):
        #break current loop
        break

    print(cnt)
#else executed naturally without passing from a break
else:    
    pass

#-------------------------------------------------------    

for cnt in range(10):
    if (cnt==5):
        break
else:
    print("for else: ", cnt)

#-------------------------------------------------------    
# switch case????

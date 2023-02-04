print("\n \n")
print("**********RENTAL PRICES OF DIFFERENT TYPES OF MOVIES**********")
print("--> New Movies - ₹75/day")
print("--> Old Movies - ₹50/day")
movie=0
new=0
old=0
while(movie!='3'):
    movie=(input("\nEnter '1',if you want to rent New Movies \nEnter '2',if your want to rent Old Movies \nEnter '3' to exit.\n:"))
    if(movie=='1'):
        print("____________________________")
        print("***Available New Movies are***\n____________________________ \n->1. Avengers infinity war \n->2. Thor Love & Thunder \n->3. Ant Man & The Wasp(Quantumania) \n->4. Wakanda Forver \n->5. Hawkeye")
        name=input("Enter the Movie Number: ")
        new=new+1
        choice=input("Do you want to rent more Movies(Y/N) :")
        if(choice in "nN"):
            break
        elif(choice in "yY"):
            print(end='')
        else:
            print("  --INVALID INPUT--  \n\nSTART THE PROGRAM AGAIN")
            break


    elif(movie=='2'):
        print("____________________________")
        print("***Available Old Movies are***\n____________________________ \n->1. Thor(The Dark World) \n->2. Mission Impossible - I  \n->3. The Rise of the Apes \n->4. Avatar - I \n->5. Iron man - I")
        name=input("Enter the Movie Number: ")
        old=old+1
        choice=input("Do you want to rent more Movies(Y/N) :")
        if(choice in "nN"):
            break
        elif(choice in "yY"):
            print(end='')
        else:
            print("  --INVALID INPUT--  \n\nSTART THE PROGRAM AGAIN")
            break

    elif(movie!='3'):
        print("\n---INVALID INPUT---")
        break
    
if(movie=='3' or choice in "nN"):
    print("\nNew Movies bought: %d"%new)
    print("Total Cost of New Movies: ₹%d"%(new*75))
    print("Old Movies bought: %d"%old)
    print("Total Cost of Old Movies: ₹%d"%(old*50))
    print("   ****************   \n-->Final Cost : %d\n   ****************   "%((new*75)+(old*50)))
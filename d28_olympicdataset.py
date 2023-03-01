from d28_analysis import analytics
obj=analytics()
t=0
while(t==0):
    def start():
        print('\n \n \n')
        n=int(input("✌️  This is an Analysis Program of Olympic Dataset. \n⟿  Enter '1' to get highest medalist Nation. \n⟿  Enter '2' to get lowest medalist Nation. \n⟿  Enter '3' to get the Country with only 1 Gold medal or 1 Silver medal or 1 Bronze medal. \n⟿  Enter '4' to get highest Gold, Silver & Bronze Medalist Nation. \n⟿  Enter '5' to get a specific Nation's details. \n⟿  Enter '6' to get details of Countries by their Rank. \n☣  Enter Value: "))
        match n:
            case 1:
                obj.maxi
            case 2:
                obj.mini
            case 3:
                obj.gsb
            case 4:
                obj.gsb1
            case 5:
                obj.spc
            case 6:
                obj.samerank
            case _:
                print("👎  INVALID INPUT  👎")
    start()
    exi=input("Do you want to Exit(y/n): ")
    if(exi=='y' or exi=='Y'):
        break;
    elif(exi=='n' or exi=='N'):
        start()
    else:
        print("👎  INVALID INPUT  👎")
        break;  




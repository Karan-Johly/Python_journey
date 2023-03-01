import pandas as pd
df=pd.read_csv("D:\\Coding\\Python Programming\\Datasets\\tokyomedals.csv")
df.index=[x for x in range(1,df.shape[0]+1)]
class analytics:
    def __init__(self):
        pass
    @property
    def maxi(self):
        return print(df[df['Total']==df['Total'].max()][['Country','Total']])
    @property
    def mini(self):
        return print(df[df['Total']==df['Total'].min()][['Country','Total']])
    @property
    def gsb(self):
        n=int(input("➤ Enter 1 to get Countries with only 1 Gold medal. \n➤ Enter 2 to get Countries with only 1 Silver medal. \n➤ Enter 3 to get Countries with only 1 Bronze medal. \nEnter Value: "))
        if(n==1):
            print(df[(df['Gold Medal']==1) & (df['Silver Medal']==0) & (df['Bronze Medal']==0)][['Country','Gold Medal','Silver Medal','Bronze Medal']])
        elif(n==2):
            print(df[(df['Gold Medal']==0) & (df['Silver Medal']==1) & (df['Bronze Medal']==0)][['Country','Gold Medal','Silver Medal','Bronze Medal']])
        elif(n==3):
            print(df[(df['Gold Medal']==0) & (df['Silver Medal']==0) & (df['Bronze Medal']==1)][['Country','Gold Medal','Silver Medal','Bronze Medal']])
        else:
            print("\***👎  INVALID INPUT  👎***/")
    @property
    def gsb1(self):
        n=int(input("➤ Enter 1 to get Nation with highest Gold medal. \n➤ Enter 2 to get Nation with highest Silver medal. \n➤ Enter 3 to get Nation with highest Bronze medal. \nEnter Value: "))
        if(n==1):
            print(df[df['Gold Medal']==df['Gold Medal'].max()][['Country','Gold Medal']])
        elif(n==2):
            print(df[df['Silver Medal']==df['Silver Medal'].max()][['Country','Silver Medal']])
        elif(n==3):
            print(df[df['Bronze Medal']==df['Bronze Medal'].max()][['Country','Bronze Medal']])
        else:
            print("\***👎  INVALID INPUT  👎***/")
    @property
    def spc(self):
        C=input("Enter the Name of Country: ")
        print(df[df['Country']==C])
    @property
    def samerank(self):
        R=int(input("Enter the Country Rank: "))
        print(df[df['Rank By Total']==R][['Country','Total','Rank By Total']])
    
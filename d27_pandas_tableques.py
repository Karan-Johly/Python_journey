#********Method 1*************

import pandas as pd
dict={"Rollno":[1,2,3,4,5,6,7,8,9,10],
      "Name":["Kiran","Jatin","Mohit","Lalit","Pawan","Gagan","Rohit","Sachin","Palvi","Mohan"],
      "Age":[21,18,17,22,19,20,18,17,16,15],
      "English":[55,42,70,80,72,71,99,58,47,46],
      "Maths":[45,33,29,30,44,45,44,39,41,42],
      "Science":[50,55,72,61,51,71,57,89,51,41],
      "Hindi":[60,61,74,72,52,62,71,71,52,59],
      "Punjabi":[70,62,75,73,53,63,57,66,59,54]}

df=pd.DataFrame(dict)
# df["Total"]=df["English"]+df["Maths"]+df["Science"]+df["Hindi"]+df["Punjabi"]
# df["Percentage"]=((df["Total"]/500)*100)
# print(df)

# **********************Method2******************
df.insert(8,"Total",df["English"]+df["Maths"]+df["Science"]+df["Hindi"]+df["Punjabi"])
df.insert(9,"Percentage",df["Total"]/5)
print(df)
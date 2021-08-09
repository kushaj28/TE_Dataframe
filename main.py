import requests
import pandas as pd
import json
url="https://takaful-interview-969lesz9nxfe.runkit.sh"
param1={"gender":"male"}
male_req=requests.get(url,params=param1)
param2={"gender":"female"}
female_req=requests.get(url,params=param2)
data_male=male_req.json()
data_female=female_req.json()
print(type(data_male))
print(data_male)
print(data_female)
data = pd.DataFrame([data_male,data_female],index=[1,2])
data.to_csv(r'C:\Users\kusha\Desktop\dataframe.csv')

print (data)

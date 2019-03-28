import pandas as pd
import numpy as np
from strgen import StringGenerator as SG

data_xls = pd.read_excel('DELEGATE LIST mun emailids (2).xlsx',"UNCSW")

data = data_xls.to_csv('UNCSW.csv', encoding='utf-8', index=False)



data = pd.read_csv("UNCSW.csv")

# print(data)


data["passwords"] = ""

# del1 = data["DELEGATE1"]
# del2 = data["DELEGATE2"]
# del1.fillna("",inplace = True)
# del2.fillna("",inplace= True)
names = data["Names"]
names.fillna("",inplace = True)


passwords = data["passwords"]
print(data)

for i in range(0,len(names)):
  	if names[i] is not "" :
  		passwords[i] = SG("[a-zA-Z0-9]{8}").render()
print(data)
data.to_csv("UNCSW-generated.csv")
writer = pd.ExcelWriter('final_passwords_gen.xlsx', engine='xlsxwriter')
unsc = pd.read_csv('UNSC-generated.csv')
unsc.to_excel(writer, sheet_name='UNSC')

DISEC = pd.read_csv('DISEC-generated.csv')
DISEC.to_excel(writer, sheet_name='DISEC')

UNSCW = pd.read_csv('UNCSW-generated.csv')
UNSCW.to_excel(writer, sheet_name='UNCSW')

AIPPM = pd.read_csv('AIPPM-generated.csv')
AIPPM.to_excel(writer, sheet_name='AIPPM')

WHSR = pd.read_csv('WHSR-generated.csv')
WHSR.to_excel(writer, sheet_name='WHSR')

EC = pd.read_csv('EC-generated.csv')
EC.to_excel(writer, sheet_name='EC')

IP = pd.read_csv('IP-generated.csv')
IP.to_excel(writer, sheet_name='IP')


writer.save()
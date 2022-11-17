import json
from tkinter.ttk import Separator
  
file = "NATURA_MULE_SOFT_RESERVA_SGI_OUT_2022_0046692713.json"

myFile=open(file, 'r')
myObject=myFile.read()
u = myObject.encode('utf-8-sig')
myObject = u.encode('utf-8')
myFile.encoding
myFile.close()
myData=json.loads(myObject,'utf-8')

Separator = ";"

count = 0
print ("Register, Material Code, Sales Code, Priority, Product Type, statusProduct ")
for i in myData['data']['product']:
    count = count +1
    
    if(i['statusProduct'] == "1"):
        print (str(count) + ""+Separator+" " + i['productId'] + ""+Separator+" "+ i['brand'] + i['countryId'] + "-"+ i['salesProductId'] + ""+Separator+" " + i['priority'] + ""+Separator+" " + i['productType'] + ""+Separator+" " +i['statusProduct'])

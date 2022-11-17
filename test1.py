import os
import json
from tkinter.ttk import Separator

brand = "NATURA"
country = "ARGENTINA"
xApiKey = "Vhr3TaxzAa5I2QEXC7F3q3yKX3Rc8Tn95hwmVoVU"
dataResourceFile = "data.json"
Separator = ";"

# Step 1 - extract data from server
# output = os.system("curl --location --request GET 'https://ncf-apigw.natura-mx-jcf-prd.naturacloud.com/cme-repository-paas-api/product?country="+country+"&brand="+brand+"' --header 'x-api-key: "+xApiKey+"' > "+dataResourceFile+""  )
# print(output)

# Step 2 - normalize data to extract report file
print ("ProductID, SalesCode, Priority, MaterialCode")

file = dataResourceFile
myFile=open(file, 'r')
myObject=myFile.read()
u = myObject.encode('utf-8-sig')
myObject = u.encode('utf-8')
myFile.encoding
myFile.close()
myData=json.loads(myObject,'utf-8')
Separator = ";"

# for i in myData['data']:
#   print (i['ProductID__c'] + ""+Separator)
  




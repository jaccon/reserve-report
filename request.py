import requests

brand="NATURA"
country="ARGENTINA"

headers = { 'Content-Type' : 'application/json; charset=utf-8',
            'Content-Length': '5818551',
            'Connection': 'keep-alive',
            'x-amzn-RequestId': '598d4c89-80b9-458a-956e-bc7297c94445',
            'x-amz-apigw-id': 'bwEkbGouoAMFxXw=',
            'X-Powered-By': 'Express',
            'ETag': 'W/"58c8b7-Gnhheszogvkf7FVpcaiHjXDneQU"',
            'x-amzn-Remapped-Date': 'Thu, 17 Nov 2022 15:07:13 GMT"',
          }

reqUrl = "https://ncf-apigw.natura-mx-jcf-prd.naturacloud.com/cme-repository-paas-api/product?country="+country+"&brand="+brand
r=requests.get(reqUrl, headers=headers)
print(r)



# curl --location --request GET 'https://ncf-apigw.natura-mx-jcf-prd.naturacloud.com/cme-repository-paas-api/product?country=ARGENTINA&brand=NATURA' \
# --header 'x-api-key: Vhr3TaxzAa5I2QEXC7F3q3yKX3Rc8Tn95hwmVoVU'


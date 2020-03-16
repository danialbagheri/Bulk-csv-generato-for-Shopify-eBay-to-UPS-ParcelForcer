import csv
import datetime

orderFile = open('orders.csv', newline='')
dpdfile = open('dpd.csv', newline='')
orders = csv.reader(orderFile)
trackings = csv.reader(dpdfile)
all_orders = []
all_shipping = []


for row in orders:
    orders = {}
    orders['post_code'] = row[18].replace(" ", "")
    orders['item_number'] = row[20]
    if len(row) < 45:
        pass
    else:
        orders['transaction_id'] = row[45]
    all_orders.append(orders)


for i in trackings:
    shipping = {}
    shipping['consignment'] = i[2]
    shipping['post_code'] = i[4]
    all_shipping.append(shipping)


def compare_lists(orders, shipping):
    today = datetime.datetime.now()
    file_name_date = today.strftime("%Y-%m-%d")
    successful_count = 0
    with open(f'archive/fileExchange-{file_name_date}.csv', 'w', newline='') as fileExchange:
        fieldnames = [
            'Action',
            'ItemID',
            'TransactionID',
            'ShippingStatus',
            'ShippingCarrierUsed',
            'ShipmentTrackingNumber',
        ]
        shippingwriter = csv.DictWriter(
            fileExchange, fieldnames=fieldnames)
        shippingwriter.writeheader()
        for item in shipping:
            for order in orders:
                if order['post_code'] == item['post_code']:
                    shippingwriter.writerow({
                        'Action': "Status",
                        'ItemID': order['item_number'],
                        'TransactionID': order['transaction_id'],
                        'ShippingStatus': '1',
                        'ShippingCarrierUsed': 'DPD',
                        'ShipmentTrackingNumber': item['consignment'],
                    }
                    )
                    successful_count += 1
    print(successful_count)


compare_lists(all_orders, all_shipping)
# import requests
# url = "https://webservices.sandbox.ebay.com/BulkDataExchangeService"  #Sandbox
# # url = "https://webservices.ebay.com/BulkDataExchangeService"  # Production
# #headers = {'content-type': 'application/soap+xml'}
# headers = {
#     'content-type': 'text/xml',
#     'X-EBAY-SOA-OPERATION-NAME': 'SetShipmentTrackingInfo',
#     'X-EBAY-SOA-SECURITY-TOKEN':

# }
# body = """<?xml version="1.0" encoding="UTF-8"?>
#          <SOAP-ENV:Envelope xmlns:ns0="http://ws.cdyne.com/WeatherWS/" xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/"
#             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
#             <SOAP-ENV:Header/>
#               <ns1:Body><ns0:GetWeatherInformation/></ns1:Body>
#          </SOAP-ENV:Envelope>"""

# response = requests.post(url,data=body,headers=headers)
# print response.content

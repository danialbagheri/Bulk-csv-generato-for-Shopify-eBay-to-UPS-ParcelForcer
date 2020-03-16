import csv
import datetime
# import pdb


order_file = open('orders.csv', newline='')
ups_file = open('ups/ups_tracking_numbers.csv', newline='')
orders = csv.reader(order_file)
tracking_numbers = csv.reader(ups_file)
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


for i in tracking_numbers:
    shipping = {}
    shipping['tracking_number'] = i[2]
    shipping['post_code'] = i[9].replace(" ", "")
    all_shipping.append(shipping)


def compare_lists(orders, shipping):
    today = datetime.datetime.now()
    file_name_date = today.strftime("%Y-%m-%d")
    successful_count = 0
    with open(f'ups/archive/ebay-bulk-trackingnumber-{file_name_date}.csv', 'w', newline='') as fileExchange:
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
                        'ShippingCarrierUsed': 'UPS',
                        'ShipmentTrackingNumber': item['tracking_number'],
                    }
                    )
                    successful_count += 1
    print(
        f"Found {successful_count} matching post codes with ebay orders, your file is saved here:")
    print(f"ups/archive/ebay-bulk-trackingnumber-{file_name_date}.csv")


compare_lists(all_orders, all_shipping)

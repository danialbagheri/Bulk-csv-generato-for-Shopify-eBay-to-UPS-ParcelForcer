import csv
import datetime
import pdb


# ups_file = open('ups/ups_tracking_numbers.csv', newline='')

# tracking_numbers = csv.reader(ups_file)


def process_orders():
    all_orders = []
    order_file = open('orders.csv', newline='')
    orders = csv.reader(order_file)
    for row in orders:
        # pdb.set_trace()
        orders = {}
        orders['order_number'] = row[1]
        orders['name'] = row[3]
        orders['email'] = row[4]
        orders['note'] = row[5]
        orders['name'] = row[12]
        orders['phone'] = row[13]
        orders['address 1'] = row[14]
        orders['address 2'] = row[15]
        orders['city'] = row[16]
        orders['county'] = row[17]
        orders['post_code'] = row[18].replace(" ", "")
        orders['item_number'] = row[20]
        orders['quantity'] = row[24]
        quantity = row[24]
        if quantity:
            try:
                quantity = int(quantity)
            except:
                continue
        else:
            quantity = 0
        if len(row) < 45:
            pass
        else:
            orders['transaction_id'] = row[45]
        if int(quantity) > 1 and int(quantity) < 5:
            for i in range(len(row[24])):
                all_orders.append(orders)
        all_orders.append(orders)

    order_file.close()
    return all_orders


def writes_csv()


def create_tables_for_csv(orders, shipping):
    today = datetime.datetime.now()  # "13/02/2019"
    max_entries = 240
    file_number = 1
    file_name_date = today.strftime("%Y-%m-%d")
    successful_count = 0
    file = open(
        f'ups/archive/ups-address-labels-{file_name_date}-{file_number}.csv', 'w', newline='')
    fieldnames = [
        'Contact Name',
        'Company or Name',
        'Country',
        'address 1',
        'Address 2',
        'City',
        'Postal Code',
        'Telephone',
        'Extension',
        'E-mail Address',
        'Weight',
        'Length',
        'Width',
        'Height',
        'Unit of Measure',
    ]
    shippingwriter = csv.DictWriter(
        file, fieldnames=fieldnames)
    shippingwriter.writeheader()

    for order in orders:
        shippingwriter.writerow({
            'Action': "Status",
            'Contact Name': order[""],
            'Company or Name': order[""],
            'Country': order[""],
            'address 1': order[""],
            'Address 2': order[""],
            'City': order[""],
            'Postal Code': order[""],
            'Telephone': order[""],
            'Extension': order[""],
            'E-mail Address': order[""],
            'Weight': order[""],
            'Length': order[""],
            'Width': order[""],
            'Height': order[""],
            'Unit of Measure': order[""],
        }
        )
        successful_count += 1
    print(
        f"Found {successful_count} matching post codes with ebay orders, your file is saved here:")
    print(f"ups/archive/ebay-bulk-trackingnumber-{file_name_date}.csv")


process_orders()
if "__name__" == "__main__":
    process_orders()

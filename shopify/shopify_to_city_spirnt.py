import csv
import datetime
import pdb


# ups_file = open('ups/ups_tracking_numbers.csv', newline='')

# tracking_numbers = csv.reader(ups_file)
def fill_the_empty(row_number):
    count = 0
    order_file = open('imports/orders.csv', newline='')
    orders_reader = csv.reader(order_file)
    previous_row = row_number - 1
    orders = {}
    for order in orders_reader:
        # pdb.set_trace()
        if count == previous_row:
            orders['order_number'] = order[0]
            orders['item_name'] = order[17]
            orders['quantity'] = order[16]
            orders['email'] = order[1]
            orders['status'] = order[2]
            orders['price'] = order[18]
            orders['customer_name'] = order[34]
            orders['address 1'] = order[36]
            orders['address 2'] = order[37]
            orders['company'] = order[38]
            orders['city'] = order[39]
            orders['county'] = order[42]
            orders['post_code'] = order[40].replace(" ", "")
            orders['notes'] = order[44]
            orders['phone'] = order[66]
            orders["status"] = order[4]
        count += 1
    order_file.close()
    return orders


def process_orders():
    all_orders = []
    order_file = open('imports/orders.csv', newline='')
    orders_reader = csv.reader(order_file)
    row_count = 0
    col_count = 0
    for row in orders_reader:
        if row_count < 1:
            for col in row:
                # print(f"col {col_count}: row: {col} \n")
                col_count += 1
        if row_count >= 1:
            # pdb.set_trace()
            orders = {}
            quantity = row[16]
            item_name = row[17]
            financial_status = row[2]
            status = row[4]
            # customer details needs repeating if financial status is empty
            if financial_status == "":
                orders = fill_the_empty(row_count)
            else:
                orders['order_number'] = row[0]
                orders['item_name'] = row[17]
                orders['quantity'] = row[16]
                orders['email'] = row[1]
                orders['payment_status'] = row[2]
                orders['price'] = row[18]
                orders['customer_name'] = row[34]
                orders['address 1'] = row[36]
                orders['address 2'] = row[37]
                orders['company'] = row[38]
                orders['city'] = row[39]
                orders['county'] = row[42]
                orders['post_code'] = row[40].replace(" ", "")
                orders['notes'] = row[44]
                orders['phone'] = row[66]
                orders["status"] = row[4]

            if quantity:
                try:
                    quantity = int(quantity)
                except:
                    continue
            else:
                quantity = 0

            if item_name == "Anti Bacterial Hand Hygiene Gel - 5Litre" and status == "unfulfilled":
                if quantity >= 2 and quantity <= 9:
                    for i in range(quantity):
                        all_orders.append(orders)
                elif quantity == 1:
                    all_orders.append(orders)
                else:
                    print(
                        f"order on line {row_count} is has {quantity} items and must be sent differently")
        row_count += 1

    order_file.close()
    return all_orders


# def writes_csv()


def create_tables_for_csv(orders):
    today = datetime.datetime.now()  # "13/02/2019"
    max_entries = 240
    file_number = 1
    file_name_date = today.strftime("%Y-%m-%d")
    successful_count = 0
    file_name = "exports/city-sprint-address-labels"
    file = open(
        f'{file_name}-{file_name_date}-{file_number}.csv', 'w', newline='')
    fieldnames = [
        'Recipient Business Name',
        'Recipient Address Line 1',
        'Recipient Address Line 2',
        'Recipient Address Line 3',
        'Recipient Post Town',
        'Recipient PostCode',
        'Recipient Mobile Number',
        'Recipient Email Address',
        'Special Instructions 1',
        'Special Instructions 2',
        'Reference Number',
    ]
    shippingwriter = csv.DictWriter(
        file, fieldnames=fieldnames)
    shippingwriter.writeheader()

    for order in orders:
        name_and_company = order['customer_name'] + " - " + order['company']
        shippingwriter.writerow({
            'Recipient Business Name': name_and_company,
            'Recipient Address Line 1': order["address 1"],
            'Recipient Address Line 2': order['address 2'],
            'Recipient Address Line 3': "",
            'Recipient Post Town': order["city"],
            'Recipient PostCode': order["post_code"],
            'Recipient Mobile Number': order['phone'],
            'Recipient Email Address': order['email'],
            'Special Instructions 1': order["notes"],
            'Special Instructions 2': "",
            'Reference Number': order["order_number"],
        }
        )
        successful_count += 1
    print(
        f"generated {successful_count} address entries for city-Sprint")
    print(f"{file_name}-{file_name_date}.csv")


# process_orders()
orders = process_orders()
create_tables_for_csv(orders)

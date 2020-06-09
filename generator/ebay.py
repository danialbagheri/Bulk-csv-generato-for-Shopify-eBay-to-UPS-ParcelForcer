import csv
import datetime
import pdb


# ups_file = open('ups/ups_tracking_numbers.csv', newline='')

# tracking_numbers = csv.reader(ups_file)
def fill_the_empty(row_number):
    '''
    This fills the rows in the shopify orders when a customer have bought more than
    one item. Please check the orders.csv file to understand.
    proobably doesn't do anything at the moment!
    '''
    count = 0
    order_file = open('imports/ebay-orders.csv',
                      encoding='mac-roman', newline='')
    orders_reader = csv.reader(order_file)
    previous_row = row_number - 1
    orders = {}
    for row in orders_reader:
        if count == previous_row:

            orders['customer_name'] = row[2]
            orders['email'] = row[3]
            orders['note'] = row[35]
            orders['address 1'] = row[42]
            orders['address 2'] = row[43]
            orders['city'] = row[44]
            orders['county'] = row[47]
            orders['post_code'] = row[46].replace(" ", "")
            orders['phone'] = row[48]
            quantity = row[24]
        elif count == row_number:
            orders['order_number'] = row[0]
            orders['item_sku'] = row[34]
            orders['quantity'] = row[14]
            orders['price'] = row[15]
            orders['company'] = ""

        count += 1
    order_file.close()
    return orders


def process_ebay_orders(file_path=None):
    if file_path:
        path = file_path
    else:
        path = 'imports/ebay-orders.csv'
    message = ""
    all_orders = []
    ups_orders = []
    box_of_500ml = []
    box_of_200ml = []
    box_of_100ml = []
    box_of_50ml = []
    row_count = 0
    col_count = 0
    order_file = open(path, encoding='mac-roman', newline='')
    orders_reader = csv.reader(order_file)
    for row in orders_reader:
        if row_count < 1:
            for col in row:
                # print(f"col {col_count}: row: {col} \n")
                col_count += 1
        # pdb.set_trace()
        if row_count >= 1:
            orders = {}
            # import pdb
            # pdb.set_trace()
            orders['order_number'] = row[0]
            orders['customer_name'] = row[2]
            orders['item_sku'] = row[34]

            if orders['item_sku'] == "":
                pass
            else:
                if orders['customer_name'] == "":
                    orders = fill_the_empty(row_count)
                else:
                    orders['email'] = row[3]
                    orders['note'] = row[35]
                    orders['address 1'] = row[42]
                    orders['address 2'] = row[43]
                    orders['city'] = row[44]
                    orders['county'] = row[47]
                    orders['post_code'] = row[46].replace(" ", "")
                    orders['phone'] = row[48]
                    orders['price'] = row[15]
                    orders['quantity'] = row[14]
                    orders['company'] = ""
                    quantity = row[14]

                if quantity:
                    try:
                        quantity = int(quantity)
                    except:
                        continue
                else:
                    quantity = 0

                # Now find the list of irems
                if orders['item_sku'] == "CALB10":
                    if quantity >= 2 and quantity <= 8:
                        for i in range(quantity):
                            ups_orders.append(orders)
                    elif quantity == 1:
                        ups_orders.append(orders)
                    else:
                        message += f"order number {orders['order_number']} has {quantity} items and must be sent differently. 5litre \n"
                        message += f"Customer name: {orders['customer_name']} phone number: {orders['phone']}\n"
                        message += f"Address: {orders['address 1']}\n {orders['address 2']}\n {orders['post_code']}\n"
                elif orders['item_sku'] == "CALB11BOX":
                    if quantity >= 2 and quantity <= 8:
                        for i in range(quantity):
                            box_of_500ml.append(orders)
                    elif quantity == 1:
                        box_of_500ml.append(orders)
                    else:
                        message += f"order number {orders['order_number']} has {quantity} items and must be sent differently. 500ml \n"
                        message += f"Customer name: {orders['customer_name']} phone number: {orders['phone']}\n"
                        message += f"Address: {orders['address 1']}\n {orders['address 2']}\n {orders['post_code']}\n"
                elif orders['item_sku'] == "CALB08BOX":
                    if quantity >= 2 and quantity <= 8:
                        for i in range(quantity):
                            box_of_200ml.append(orders)
                    elif quantity == 1:
                        box_of_200ml.append(orders)
                    else:
                        message += f"order number {orders['order_number']} has {quantity} items and must be sent differently. 200ml \n"
                        message += f"Customer name: {orders['customer_name']} phone number: {orders['phone']}\n"
                        message += f"Address: {orders['address 1']}\n {orders['address 2']}\n {orders['post_code']}\n"
                elif orders['item_sku'] == "CALB07BOX":
                    if quantity >= 2 and quantity <= 8:
                        for i in range(quantity):
                            box_of_100ml.append(orders)
                    elif quantity == 1:
                        box_of_100ml.append(orders)
                    else:
                        message += f"order number {orders['order_number']} has {quantity} items and must be sent differently. 100ml \n"
                        message += f"Customer name: {orders['customer_name']} phone number: {orders['phone']}\n"
                        message += f"Address: {orders['address 1']}\n {orders['address 2']}\n {orders['post_code']}\n"
                else:
                    message += f"Investigate this order number: {orders['order_number']}."
        row_count += 1

    order_file.close()
    print(box_of_500ml)
    return message, ups_orders, box_of_500ml, box_of_200ml, box_of_100ml


# process_ebay_orders()

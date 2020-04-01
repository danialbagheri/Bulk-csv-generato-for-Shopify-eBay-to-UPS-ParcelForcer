# Shopify and eBay to UPS and ParcelForce CSV generator

This python applications generates a bulk csv file to be imported for UPS, Parcel force and DPD courier.
You will need to have basic python knowledge to be able to use this program.
It would probably need some adjustment for different users and purposes.
Depends on your setup and templates you may need to adjust the software to your need. It is highly customisable once you understand how it works.

## Currently Supperted Platform and Couriers

* Shopify
* Amazon
* ebay (originally developed and needs updating)
* DPD (not integrated with the new code inside the generator folder)
* UPS
* Parcel Force


## GUI (work in progress)

The GUI is designed and developed with Python QT library.

![Image of GUI](./qt-design/ui.png)

## Step By step instructions

You have to first create a virtual environment:

```
python3 -m venv venv
```

You have to enable virtual environment after that:

```
source venv/bin/activate
```

now, you need install the libraries with PIP:

```
pip install -r requirements.txt
```

now your are ready. you need to change your directory with command `cd generator` and create a folder `mkdir imports`in this directory. This is where you need to locate your downloaded orders from Amazon, ebay and shopify. files needs to be named like this `shipify-orders.csv` and likewise for amazon and ebay. all letters should be lowercase. The command line interactive will generate the CSV files. You may need to adjust the code for your own template and need. It is easy all you have to do is to go to `processes_orders` functions for each store and in the csv_generator file and then uncommend the first row print to identify your orders column numbers and names.


```
python csv_generator.py
```

to test the GUI, use the below command:

```
python main.py
```

Happy Coding

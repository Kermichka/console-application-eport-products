import shopify
import os
import csv
import sys

shop_url = os.getenv('SHOP_URL')
access_token= os.getenv('ACCESS_TOKEN')
api_version ='2023-01'

session = shopify.Session(shop_url, api_version, access_token)
shopify.ShopifyResource.activate_session(session)
current_shop = shopify.Shop.current()

products = shopify.Product.find()

arguments = sys.argv
output_filename = arguments[1]

with open(output_filename, mode='w', newline='') as csv_file:
    fieldnames = products[0].attributes.keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for product in products:
        writer.writerow(product.attributes)
print('Ready!')
exit(0) 
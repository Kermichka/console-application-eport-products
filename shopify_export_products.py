import shopify
import os
import csv
import sys
import logging
from dotenv import load_dotenv

load_dotenv() 

logger = logging.getLogger()

shop_url = os.getenv('SHOP_URL')
access_token= os.getenv('ACCESS_TOKEN')
api_version ='2023-01'

logger.info('Creating shopify session...')
session = shopify.Session(shop_url, api_version, access_token)
shopify.ShopifyResource.activate_session(session)
logger.info('Created shopify session.')

logger.info('Getting all product data...')
products = shopify.Product.find()
logger.info('%i products found.', len(products))

arguments = sys.argv
output_filename = arguments[1]

with open(output_filename, mode='w', newline='') as csv_file:
    fieldnames = products[0].attributes.keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for product in products:
        writer.writerow(product.attributes)
logger.info('Ready! :3')

# TODO 
# 4h
# USE logging library, print info messages by default, print timestamp & level in front of the message /dont change logger.info lines/
# USE python-dotenv DONT COMMIT .env FILE!!!
# --filename or -f for filename (argparse only if 38 line) (22 & 23 remove)
# --level or -l /debug info warning/
# functions "__name__" = "__main__"
# black, pre-commit, flake8, from vankata
# mypy
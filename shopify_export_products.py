import shopify
import os
import csv
import sys
import logging
import argparse
from dotenv import load_dotenv

def configure_parser():
    parser = argparse.ArgumentParser(description="Shopify Data Exporter")
    parser.add_argument("-f", "--filename", help="Output filename for CSV")
    parser.add_argument(
        "-l", "--level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    )
    return parser

def configure_logger(level_logging, log_filename="example.log"):
    log_format = '[%(asctime)s] - %(levelname)s:%(name)s:%(message)s '
    logging.basicConfig(filename=log_filename, encoding="utf-8", level=level_logging, format=log_format, filemode='w')
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(level_logging)
    stderr_handler.setFormatter(logging.Formatter(log_format))
    logger = logging.getLogger()
    logger.addHandler(stderr_handler)
    return logger

def main():

    load_dotenv()
    shop_url = os.getenv("SHOP_URL")
    access_token = os.getenv("ACCESS_TOKEN")
    api_version = "2023-01"

    parser = configure_parser()
    
    args = parser.parse_args()
    output_filename = args.filename
    level_logging = args.level
    logger = configure_logger(level_logging)
    return shop_url, access_token, api_version, output_filename, logger

if __name__ == "__main__":

    shop_url, access_token, api_version, output_filename, logger = main()

    logger.info("Creating shopify session...")
    session = shopify.Session(shop_url, api_version, access_token)
    shopify.ShopifyResource.activate_session(session)
    logger.info("Created shopify session.")

    logger.info("Getting all product data...")
    products = shopify.Product.find()
    logger.info("%i products found.", len(products))

    with open(output_filename, mode="w", newline="") as csv_file:
        fieldnames = products[0].attributes.keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow(product.attributes)

    logger.info("Ready! :3")

# TODO
# mypy

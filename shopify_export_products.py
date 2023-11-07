import shopify
import os

shop_url = os.getenv('MERCHANT')
api_version ='2023-01'

API_KEY="30b2cc7f0d06481d9c061c6d6aa6dda7"
ACCESS_TOKEN="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"

session = shopify.Session(shop_url, api_version, ACCESS_TOKEN)
shopify.ShopifyResource.activate_session(session)
current_shop = shopify.Shop.current()
print(current_shop)

products = shopify.Product.find()
for product in products:
    print(product.attributes)
else:
    print("No products found.")
exit(0) 
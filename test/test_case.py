import json
from operator import delitem

from Amazon_project.search import AmazonPage

def test_amazon_search(driver):
    amazon = AmazonPage(driver)

    amazon.search_product("iPhone 17")
    min_price = 134900
    amazon.get_products_above_price(min_price)
    amazon.get_products_above_price(min_price)


    # all_products = amazon.get_first_product_details()   # ← get full list

    # Print all
    # for product in all_products:
    #     print(f"Title: {product['title']}")
    #     print(f"Price: {product['price']}")
    # [cel_widget_id *= "MAIN-SEARCH_RESULTS-"].a - price - whole
    #
    #
    # # Save in JSON file
    # with open("amazon_product.json", "w") as f:
    #     json.dump(all_products, f, indent=4)
    #
    # print(" All products saved to amazon_product.json")

    title, price = amazon.get_first_product_details()

    print("2nd Product Title:", title)
    print("2nd Product Price:", price)




    data = {
        "title": title,
        "price": price,


    }

    with open("amazon_product.json", "w") as f:
        json.dump(data, f, indent=4)

    print(" 2nd product data saved to amazon_product.json")

    with open("amazon_product.json", "w") as f:
        json.dump(products, f, indent=4, )

    print(" All products  saved to amazon_product.json")




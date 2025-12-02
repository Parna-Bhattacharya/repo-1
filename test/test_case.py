

from Amazon_project.search import AmazonPage

def test_amazon_search(driver):
    amazon = AmazonPage(driver)

    amazon.search_product("iPhone 17")
    min_price = 174900
    amazon.get_first_product_details()
    amazon.get_products_above_price(min_price)





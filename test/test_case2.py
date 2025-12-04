from Amazon_project.clothing import ClothingPage
from Amazon_project.deal.early_deals import EarlyDeal
from Amazon_project.deal.today import Deal
from Amazon_project.deal.tv import Tv
from Amazon_project.ethnic import EthnicPage
from Amazon_project.go_to_cart import Cart
from Amazon_project.headphones.brands import Brand
from Amazon_project.home_page import HomePage
from Amazon_project.location.footer import Footer
from Amazon_project.location.go_to_website import GoToWebsite
from Amazon_project.location.usa_shopping import BlackFriday
from Amazon_project.news.All_click import AllClick
from Amazon_project.news.go_to_cart import GoToCart
from Amazon_project.news.popover_click import Popovers
from Amazon_project.woman import WomanPage
from Amazon_project.news.productivity import Product
from Amazon_project.all_click import AllPage
from Amazon_project.books import Book
from Amazon_project.hardbook import HardBook



import time

def test_fashion(driver):
    home_page = HomePage(driver)
    home_page.fashion_home()
    woman_page=WomanPage(driver)
    woman_page.woman_home()
    clothing_page=ClothingPage(driver)
    clothing_page.clothing_home()
    ethnic_page=EthnicPage(driver)
    ethnic_page.ethnic_home()
    ethnic_page.add()
    ethnic_page.adds_()
    go_to=Cart(driver)
    go_to.go_to_cart()
    go_to.proceed_to_cart()
    print("\nFashion home page passed")
    print("\nWoman home page passed")
    print("\nClothing home page passed")
    print("\nethnic home page passed ")
def test_books(driver):
    all_find=AllPage(driver)
    all_find.all_clicking()

    all_find.see_all_clicking()

    all_find.book_clicking()

    all_find.indian_book_clicking()

    all_find.search_indian_book("ramayan")

    all_books=Book(driver)
    all_books.get_it_tommorow()

    # hardbook=HardBook(driver)
    # hardbook.get_hardbook()

def test_new(driver):
    news_page=AllClick(driver)
    news_page.news()

    news_page.echo()

    # prime=Product(driver)
    # prime.products()

    alexas=Product(driver)
    alexas.click_alexa()
    alexas.click_device()

    over=Popovers(driver)
    over.click_popover()

    go=GoToCart(driver)
    go.go_to()

    go.electronics()

    go.watches()

def test_headphone(driver):
    boat=Brand(driver)
    boat.search("headphone brands")
    boat.adding()
def test_location(driver):
    usa=Footer(driver)
    usa.select_location()
    usas=GoToWebsite(driver)
    usas.go_to_website()
    usas.choose_location()
    black=BlackFriday(driver)
    black.change_address()

def test_nav(driver):
    dealing=Deal(driver)
    dealing.today_deal()
    clicking=EarlyDeal(driver)
    clicking.early_deal()
    clicking.click_element()

    tvs=Tv(driver)
    tvs.tv_deal()

    tvs.exchange()




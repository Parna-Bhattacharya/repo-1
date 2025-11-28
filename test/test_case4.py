import time

from Amazon_project.fresh_vegetable.cake import Cake
from Amazon_project.fresh_vegetable.fresh_vegis import FreshVegetable
from Amazon_project.fresh_vegetable.mother import Cakes


def test_vagis(driver):
    all_vagis=FreshVegetable(driver)
    all_vagis.click_fresh()
    time.sleep(5)
    all_vagis.search_icecream("icecream cake")
    hoachpochs=Cake(driver)
    hoachpochs.hochpoch()
    time.sleep(5)
    hoachpochsss=Cakes(driver)
    hoachpochsss.hochpochss()
    time.sleep(5)




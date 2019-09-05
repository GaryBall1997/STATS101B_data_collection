"""
This file was made to conduct alcohol test for STATS 101B
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from thread_class import *


def main():
    # add the thread
    # the second parameter could be the user ID
    thread1 = myThread(1, "e92lg9kuua", 3)
    thread2 = myThread(2, "gvwl9y2x2d", 3)
    thread3 = myThread(3, "vpzwg623lp", 3)


    # thread staring
    thread1.start()
    thread2.start()
    thread3.start()
    print("Exiting Main Thread")


def get_info(user_id):
    # int(input("Enter the country you want to search:"))
    driver = webdriver.Chrome()
    driver.get(
        "https://islands.smp.uq.edu.au/login.php")
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")

    except:
        pass

    driver.find_element_by_xpath(
        "//*[@id=\"content\"]/form/div/div[1]/input").clear()
    driver.find_element_by_xpath(
        "//*[@id=\"content\"]/form/div/div[1]/input").send_keys(
        "3160100572@zju.edu.cn")
    driver.find_element_by_xpath(
        "//*[@id=\"content\"]/form/div/div[2]/input").send_keys(
        "GaryBall594176", Keys.ENTER)
    driver.get(
        "https://islands.smp.uq.edu.au/village.php?Hayarano")
    driver.find_element_by_xpath("//*[@id=\"villagemap\"]/div[1]").click()
    # driver.find_element_by_xpath("//*[@id=\"houseinfo\"]/table[1]/tbody/tr[1]/td[1]").click()
    driver.get(
        "https://islands.smp.uq.edu.au/village.php?Hayarano")

    driver.get(
        "https://islands.smp.uq.edu.au//islander.php?id=" + user_id)

    driver.find_element_by_xpath("// *[ @ id = \"t3tab\"]").click()

    # shots of vodka
    shots_volda = 5
    for i in range(shots_volda):
        driver.find_element_by_xpath("//*[@id=\"task_menu\"]/div[15]").click()
        driver.find_element_by_xpath("//*[@id=\"tasksalcohol\"]/div[7]/span").click()
        sleep(10)

    # sleep 20 minutes
    sleep(1200)

    # take blood alcohol test every 1 minutes.
    blood_alcohol_test = 30

    for j in range(blood_alcohol_test):
        driver.find_element_by_xpath("//*[@id=\"task_menu\"]/div[7]").click()
        driver.find_element_by_xpath("//*[@id=\"tasksblood\"]/div[2]/span").click()
        # take blood alcohol test every 1 minutes
        sleep(60)

    driver.quit()


if __name__ == "__main__":
    main()


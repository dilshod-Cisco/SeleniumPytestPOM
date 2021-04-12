#from src.all_imports import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, NoSuchElementException

from selenium.webdriver.common.by import By
import datetime
import time

import src.utilities as utils

# this is reusable functions for webpages.
class BasePage:
    def __init__(self, driver):
        # this is global properties in constructor (function __init__)
        self.driver = driver
        self.wwait = WebDriverWait(self.driver, 10)

    def click_element_by_xpath(self,xpath):
        """
        this method finds the element by xpath and clicks it
        :param xpath: correct unique xpath of single element
        """
        try:
            utils.LOG.info(f"xpath provided: {xpath}")
            # element = driver.find_element_by_xpath(xpath)
            element = self.wwait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

            utils.LOG.info("clicking the element")
            element.click()
        except NoSuchElementException as err:
            utils.LOG.warning(f"Check element by following xpath: {xpath}")
            utils.LOG.error(err)
            self.take_screenshot('ErrorClickElement_')

    def enter_text_by_xpath(self, xpath, some_text):
        """
        this method finds the element by xpath and enters text in it
        :param xpath: correct unique xpath of single INPUT element
        :param some_text: text to be entered in the element
        """
        try:
            utils.LOG.info(f"xpath provided: {xpath}")
            # element = driver.find_element_by_xpath(xpath)
            # element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
            element = self.wwait.until(EC.presence_of_element_located((By.XPATH, xpath)))

            utils.LOG.info(f"entering the following text :{some_text}")
            element.send_keys(some_text)
        except WebDriverException as err:
            utils.LOG.error(f"Entering Text failed by following xpath: {xpath}")
            utils.LOG.error(err)
            self.take_screenshot('ErrorEnterText_')

    def highlight_element(self, element):
        js_script = "arguments[0].setAttribute('style', arguments[1]);"
        original_style = element.get_attrivute('style')
        new_style = "color: green; border: 2px solid green;"
        # new_style = "background: yellow; color: green; border: 2px solid green;"
        self.driver.execute_script(js_script, element, new_style)
        self.driver.execute_script(js_script, element, original_style)
        utils.LOG.info("Element highlighted")

    def take_screenshot(self, message=""):
        timestmp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
        # ROOT_DIR is "C:/dev/week7"
        file_location = f"{utils.ROOT_DIR}/screenshots/"
        file_location = f"C:/DEV/week7/screenshots/"
        file_name = message + timestmp + ".png"
        full_file_path = file_location + file_name

        self.driver.save_screenshot(full_file_path)
        utils.LOG.info("screenshot was taken and completed")
        # driver.get_screenshot_as_png(message + timestmp)


    def get_text_by_xpath(self, xpath: str) -> str:
        try:
            utils.LOG.info(f"xpath provided: {xpath}")
            # element = driver.find_element_by_xpath(xpath)
            element = self.wwait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

            utils.LOG.info("getting the element text")
            return element.text
        except NoSuchElementException as err:
            utils.LOG.warning(f"Check element by following xpath: {xpath}")
            utils.LOG.error(err)
            self.take_screenshot('ErrorGetText_')


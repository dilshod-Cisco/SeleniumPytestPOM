

from src.all_imports import *


driver = webdriver.Chrome()
# driver.maximize_window()
driver.implicitly_wait(20)  # read more about this

def launch_website(url):
    driver.get(url)
    print(f"opened the browser and website : {url}")
    time.sleep(1)  # thread.sleep() in java




def click_element_by_xpath(xpath):
    """
    this method finds the element by xpath and clicks it
    :param xpath: correct unique xpath of single element
    """
    try:
        print(f"xpath provided: {xpath}")
        # element = driver.find_element_by_xpath(xpath)
        wwait = WebDriverWait(driver, 10)
        element = wwait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

        print("clicking the element")
        element.click()
    except NoSuchElementException as err:
        print(f"Check element by following xpath: {xpath}")
        print(err)
        take_screenshot('ErrorClickElement_')




def enter_text_by_xpath(xpath, some_text):
    """
    this method finds the element by xpath and enters text in it
    :param xpath: correct unique xpath of single INPUT element
    :param some_text: text to be entered in the element
    """
    try:
        print(f"xpath provided: {xpath}")
        # element = driver.find_element_by_xpath(xpath)
        wwait = WebDriverWait(driver, 10)
        # element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        element = wwait.until(EC.presence_of_element_located((By.XPATH, xpath)))

        print(f"entering the following text :{some_text}")
        element.send_keys(some_text)
    except WebDriverException as err:
        print(f"Entering Text failed by following xpath: {xpath}")
        print(err)
        take_screenshot('ErrorEnterText_')


def highlight_element(element):
    js_script = "arguments[0].setAttribute('style', arguments[1]);"
    original_style = element.get_attrivute('style')
    new_style = "color: green; border: 2px solid green;"
    # new_style = "background: yellow; color: green; border: 2px solid green;"
    driver.execute_script(js_script, element, new_style)
    driver.execute_script(js_script, element, original_style)



def take_screenshot(message=""):
    timestmp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
    # ROOT_DIR is "C:/dev/week7"
    file_location = f"{utils.ROOT_DIR}/screenshots/"
    file_location = f"C:/DEV/week7/screenshots/"
    file_name = message + timestmp + ".png"
    full_file_path = file_location + file_name


    driver.save_screenshot(full_file_path)
    # driver.get_screenshot_as_png(message + timestmp)



def login_to_automation_practice(url, email, password):
    """
    *********** Scenario: Login to "http://automationpractice.com/index.php"
    Prerequisite: create an account:
    username: hello@email.com, have strong password: "$Password001"
    identify all locators by inspecting on browser (xpath, optional: id, css selector):
    sign_in_link = "//a[@class='login'" # this is incorrect XPATH, to see Try Except
    """
    #login_page = LoginPage() # this is the steps:
    sign_in_link = "//a[@class='login']"
    email_input = "//input[@id='email']"
    password_input = "//input[@id='passwd']"
    sign_in_button = "//button[@id='SubmitLogin']"
    sign_out_link = "//a[@class='logout']"

    # Steps:
    launch_website(url)
    click_element_by_xpath(sign_in_link)
    time.sleep(2)
    enter_text_by_xpath(email_input, email)
    enter_text_by_xpath(password_input, password)
    click_element_by_xpath(sign_in_button)
    time.sleep(10)
    utils.LOG.info("successfully signed in ")
    utils.LOG.info("signing out now...")
    click_element_by_xpath(sign_out_link)
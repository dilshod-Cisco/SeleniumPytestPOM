from src.all_imports import *

data = utils.load_yaml(f"{utils.ROOT_DIR}/data/config.yml")
data_neg = utils.load_yaml(f"{utils.ROOT_DIR}/data/login_scenarios/login_negative.yml")

@pytest.mark.login
@pytest.mark.loginPositive
def test_login_case1(driver):
    #print("This is it, I am doing my Framework !!!")
    utils.LOG.info("test_login_case1 started....")
    # utils.LOG.debug("Debug message....")
    # utils.LOG.error("I am an exception case.")
    # utils.LOG.warn(" something does not seem to be right, but not an error.")
    # utils.LOG.critical("WOUUW WOOUW STOP NOW< CAN NOT RUN ANYTHING AT THIS POINT!!!!")

    #driver.get("http://automationpractice.com/index.php")
    # time.sleep(10)

    web_url = data['scenario1']['web_url']
    username = data['scenario1']['username']
    pswd = data['scenario1']['password']

    login_page = LoginPage(driver)

    # sign_in_link = "//a[@class='login']" # this is the FIRST VERSION.
    # email_input = "//input[@id='email']"
    # password_input = "//input[@id='passwd']"
    # sign_in_button = "//button[@id='SubmitLogin']"
    # sign_out_link = "//a[@class='logout']"


    #login_to_automation_practice(web_url, username, pswd)



    driver.get(web_url)
    print(f"opened the browser and website : {web_url}")
    time.sleep(1)  # thread.sleep() in java

    login_page.click_sign_in_link()
    login_page.enter_email(username)
    login_page.enter_password(pswd)
    login_page.click_sign_in_button()
    utils.LOG.info("We are able to sign in now.")
    time.sleep(5)
    login_page.take_screenshot('HomePage-')

    login_page.sign_out()
    utils.LOG.info("test_login_case1 completed ")

@pytest.mark.login
@pytest.mark.loginNegative
def test_login_case2(driver):
    pass
    web_url = data_neg['scenario1']['web_url']
    username = data_neg['scenario1']['username']
    pswd = data_neg['scenario1']['password']



    # wwait = WebDriverWait(driver, 10)
    # element = wwait.until(EC.element_to_be_clickable((By.XPATH, sign_in_link)))
    #
    # element.click()
    # time.sleep(2)

    # element = wwait.until(EC.presence_of_element_located((By.XPATH, email_input)))
    # element.send_keys(username)
    # element = wwait.until(EC.presence_of_element_located((By.XPATH, password_input)))
    # element.send_keys(pswd)

    # element = wwait.until(EC.element_to_be_clickable((By.XPATH, sign_in_button)))
    # element.click()
    # time.sleep(10)

    # utils.LOG.info("successfully signed in  ")
    # utils.LOG.info("signing out now.....")

    # element = wwait.until(EC.element_to_be_clickable((By.XPATH, sign_out_link)))
    # element.click()
    # utils.LOG.info("test_login_case1 completed")

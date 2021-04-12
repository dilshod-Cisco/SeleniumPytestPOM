from src.all_imports import *

utils.LOG = utils.create_logger()


@pytest.fixture(scope='session')
def driver():
    """this is my pytest fixture (set of code to execute before/after my scope."""
    utils.LOG.info("********** This is the SETUP fixture to run before your scope of your fixture *********")

    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.implicitly_wait(20)  # read more about this
    utils.LOG.info("**********  SETUP fixture completed **********")

    yield driver

    utils.LOG.info("******** This is the TEARDOWN steps after each of your scope *************")
    utils.LOG.info(f"Current url:  {driver.current_url}")
    utils.LOG.info(f"Current title: {driver.title}")
    utils.LOG.info(f"Current win_handle: {driver.current_window_handle}")
    utils.LOG.info(f"Current name: {driver.name}")


    driver.quit()
    utils.LOG.info("browser is closed")

    utils.LOG.info("********  TEARDOWN completed *************")

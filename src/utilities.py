import logging
import time

from os.path import abspath, dirname

# to find the full location of your project in your system use this
import yaml

ROOT_DIR = dirname(dirname(abspath(__file__)))

LOG = object

def get_str_day():
    return time.strftime("%Y%m%d")  # 20200927



def get_str_seconds():
    return time.strftime("%Y%m%d_%H%M%S", time.localtime())


def create_logger(filename=""):
    logging.basicConfig(filename=f"{ROOT_DIR}/logs/{filename}{get_str_day()}.log",
                        level=logging.INFO,
                        format="%(asctime)-15s [%(levelname)s] %(funcName)s: %(message)s",
                        filemode='a')  # 'w' - to overwrite in each run, 'a' - append
    return logging.getLogger()


def load_yaml(filepath):
    with open(filepath, 'r') as data:
        document = yaml.safe_load(data)
    return document



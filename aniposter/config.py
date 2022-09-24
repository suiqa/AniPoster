import configparser
from loguru import logger

config = configparser.ConfigParser()
config.read('config.ini')

token = config["BOT"]["token"]
parse_mode = config["BOT"]["parse_mode"]

if not token or not parse_mode:
    logger.error("Pls check BOT config section")
    quit()
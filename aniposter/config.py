import configparser
from loguru import logger

config = configparser.ConfigParser()
config.read('config.ini')

# Bot Stuff
token = config["BOT"]["token"]
parse_mode = config["BOT"]["parse_mode"]
start_text = config["BOT"]["start_text"]

# Poster Stuff
channel_id = config["POSTER"]["channel_id"]

# SauceNao Stuff
saucenao_key = config["SauceNao"]["api_key"]

if not token or not parse_mode:
    logger.error("Pls check BOT config section")
    quit()
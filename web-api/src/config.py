import configparser
import json

_config_ini = configparser.ConfigParser()

_config_ini.read('config.ini', encoding="utf-8")

db_config = _config_ini["DATABASE"]

web_api_config = _config_ini['WEB_API']

solt = _config_ini['Default'].get('SOLT')

origins = json.loads(_config_ini['Default'].get('ORIGINS'))
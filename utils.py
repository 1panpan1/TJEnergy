import re
from datetime import datetime
from configparser import ConfigParser

class EmailConfigException(Exception):
    pass

class ParserConfigException(Exception):
    pass

def log(msg):
    print("{}  {}".format(datetime.now().strftime("%y-%m-%d %H:%M:%S"), msg))

def valid_addr(address):
    """
    check the validity of email address
    """
    regex = r'[\w]+@([\w]+\.)+[\w]+'
    if re.match(regex, address) is not None:
        return True
    else:
        return False

def valid_url(url):
    """
    check the validity of url.
    """
    regex = r'((http|https|ftp)://)?[\w_\-\.]+(:[0-9]{1,5})(/[\w_\-\.]*)*(\?[\w&%_=#\'\"\-]+)*'
    if re.match(regex, url) is not None:
        return True
    else:
        return False

def load_config(config_file):
    cfg_dict = {}
    cfg = ConfigParser()
    cfg.read(config_file)
    if cfg.has_option("email", "username") is False or \
        cfg.has_option("email", "passcode") is False or \
        cfg.has_option("email", "sender_email") is False or \
        cfg.has_option("email", "receiver_emails") is False or \
        cfg.has_option("parser", "url") is False or \
        cfg.has_option("email", "hostname") is False or \
        cfg.has_option("email", "hostport") is False or \
        cfg.has_option("energy", "limit") is False or \
        cfg.has_option("energy", "send_email_weekday") is False or \
        cfg.has_option("energy", "send_email_hour") is False or \
        cfg.has_option("energy", "interval") is False or \
        cfg.has_option("energy", "alert_interval") is False:
        log("Parsing config failed.")
        return None
    else:
        cfg_dict['email_hostname'] = cfg.get("email", "hostname")
        cfg_dict['email_hostport'] = int(cfg.get("email", "hostport"))
        cfg_dict['email_username'] = cfg.get("email", "username")
        cfg_dict['email_passcode'] = cfg.get("email", "passcode")
        cfg_dict['email_sender_email'] = cfg.get("email", "sender_email")
        cfg_dict['email_receiver_emails'] = [x.strip() for x in cfg.get("email", "receiver_emails").split(',')]
        cfg_dict['parser_url'] = cfg.get("parser", "url")
        cfg_dict['energy_limit'] = 0 if cfg.get("energy", "limit") == "" else float(cfg.get("energy", "limit"))
        cfg_dict['energy_send_email_weekday'] = [x.strip() for x in cfg.get("energy", "send_email_weekday").split(',')]
        cfg_dict['energy_send_email_hour'] = [x.strip() for x in cfg.get("energy", "send_email_hour").split(',')]
        cfg_dict['energy_interval'] = int(cfg.get("energy", "interval"))
        cfg_dict['energy_alert_interval'] = int(cfg.get("energy", "alert_interval"))
        return cfg_dict

if __name__ == "__main__":
    cfg = load_config("config.ini")

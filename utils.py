from datetime import datetime
from configparser import ConfigParser

def log(msg):
    print("{} {}".format(datetime.now().strftime("%y-%m-%d %H:%M:%S"), msg))

def load_config(config_file):
    cfg_dict = {}
    cfg = ConfigParser()
    cfg.read(config_file)
    if cfg.has_option("email", "username") is False or \
        cfg.has_option("email", "passcode") is False or \
        cfg.has_option("email", "sender_email") is False or \
        cfg.has_option("email", "receiver_emails") is False or \
        cfg.has_option("parser", "url") is False:
        log("Parsing config failed.")
        return None
    else:
        cfg_dict['email_username'] = cfg.get("email", "username")
        cfg_dict['email_passcode'] = cfg.get("email", "passcode")
        cfg_dict['email_sender_email'] = cfg.get("email", "sender_email")
        cfg_dict['email_receiver_emails'] = cfg.get("email", "receiver_emails").split(',')
        cfg_dict['url'] = cfg.get("parser", "url")
        return cfg_dict

if __name__ == "__main__":
    load_config("config.ini")
import ConfigParser


def get_config_object(config_path):
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    return config

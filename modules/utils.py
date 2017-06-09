def get_now_time():
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

def get_app_info(app_section_name, app_info_key):
    import modules.config_module as config_module
    config = config_module.get_config_object('./config/app.config')
    return config.get(app_section_name, app_info_key)

def html_decode(value):
    # decode html, e.g. '&gt;' -> '>', '&lt;' -> '<', '&quot;' -> '"', '&amp;' -> '&'
    from HTMLParser import HTMLParser
    h = HTMLParser()
    return h.unescape(value)


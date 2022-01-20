# -*- coding: utf-8 -*-

tg_key = "683653170:AAFN19KTaPfi2kprLcD7av3F7h812DZpMCg"
# telegram bot api key

zbx_tg_prefix = "zbxtg"  # variable for separating text from script info
zbx_tg_tmp_dir = "/var/tmp/" + zbx_tg_prefix  # directory for saving caches, uids, cookies, etc.
zbx_tg_signature = False

zbx_tg_update_messages = True
zbx_tg_matches = {
    "problem": "PROBLEM: ",
    "ok": "OK: "
}

zbx_server = "http://127.0.0.1/zabbix/"  # zabbix server full url
zbx_api_user = "moe47"
zbx_api_pass = "moe47@12345"
zbx_api_verify = True  # True - do not ignore self signed certificates, False - ignore

zbx_basic_auth = False
zbx_basic_auth_user = "moe47"
zbx_basic_auth_pass = "moe47@12345"

proxy_to_zbx = None
proxy_to_tg = None

# proxy_to_zbx = "http://proxy.local:3128"
# proxy_to_tg = "https://proxy.local:3128"

# proxy_to_tg = "socks5://user1:password2@hostname:port" # socks5 with username and password
# proxy_to_tg = "socks5://hostname:port" # socks5 without username and password

google_maps_api_key = None  # get your key, see https://developers.google.com/maps/documentation/geocoding/intro

zbx_tg_daemon_enabled = False
zbx_tg_daemon_wl_ids = [6931850, ]
zbx_tg_daemon_wl_u = ["john47moe", ]

zbx_db_host = "localhost"
zbx_db_database = "zabbix"
zbx_db_user = "zabbix"
zbx_db_password = "!QAZ2wsx#EDC"


emoji_map = {
    "Resolved": "✅",
    "High": "❗",
    "Disaster": "❌",
    "Information": "ℹ️",
    "Warning": "⚠️",
    "bomb": "💣",
    "fire": "🔥",
    "hankey": "💩",
}

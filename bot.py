#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

# Custom your logger
"""
from nonebot.log import logger, default_format

logger.add(
    "error.log", rotation="00:00", diagnose=False, level="ERROR", format=default_format
)
"""
# You can pass some keyword args config to init function

nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

nonebot.load_builtin_plugins("echo")
nonebot.load_plugin("nonebot_plugin_manager")  # 插件管理器
nonebot.load_plugin("nonebot_plugin_covid19_news")  # 新冠疫情播报
# nonebot.load_plugin("nonebot_plugin_translator") # 多语种翻译器
nonebot.load_plugin("nonebot_plugin_fortune")  # 综合签到系统
nonebot.load_plugin("nonebot_plugin_abstract")  # 抽象工具
# nonebot.load_plugin("nonebot_plugin_giyf") # 搜索
nonebot.load_plugin("nonebot_plugin_remake")  # 人生重开模拟器
nonebot.load_plugin("nonebot_plugin_caiyunai")  # 彩云小梦
# nonebot.load_plugin("nonebot_plugin_guess") # 猜城市名
nonebot.load_plugin("nonebot_plugin_russian")  # 俄罗斯轮盘赌
nonebot.load_plugin("nonebot_plugin_simplemusic")  # 综合点歌
nonebot.load_plugin("nonebot_plugin_mcstatus")  # MC服务器状态查询
# nonebot.load_plugin("nonebot_plugin_phlogo")  # Pornhub风格图标生成
nonebot.load_plugin("nonebot_plugin_withdraw")  # 撤回
nonebot.load_plugin("nonebot_plugin_weather_lite")  # 天气查询
nonebot.load_plugin("nonebot_plugin_morning")  # 早晚安
# nonebot.load_plugin("nonebot_plugin_status")  # 服务器状态
nonebot.load_plugin("nonebot_plugin_cocdicer")  # COC骰子
nonebot.load_plugin("nonebot_plugin_trpglogger")  # 跑团记录
# nonebot.load_plugin("")
# nonebot.load_plugin("")
# nonebot.load_plugin("")
# nonebot.load_plugin("")
# nonebot.load_plugin("")
# nonebot.load_plugin("")
# nonebot.load_plugin("leona/plugins/leona_actions")  # 基本交互

# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins

# nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
#
# config = driver.config
# do something...


if __name__ == "__main__":
    nonebot.logger.warning(
        "Always use `nb run` to start the bot instead of manually running!"
    )
    nonebot.run(app="__mp_main__:app")

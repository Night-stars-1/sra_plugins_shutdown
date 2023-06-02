from . import *

import re
from time import time
import flet as ft
from utils.log import log, level
from utils.config import read_json_file, CONFIG_FILE_NAME, _

from onepush import notify

start_time = 0

def get_message(*arg):
    """
    说明:
        收集消息并返回
    返回:
        收集到的消息
    """
    if arg:
        content = arg[0][:-1].replace("\x1b[0;34;40m","").replace("-1\x1b[0m","")
        if re.match(_(r'开始(.*)锄地'),content):
            notify_log(f"\n{content}")
        elif re.match(_(r'识别超时'),content):
            notify_log(f"\n{content}")

log.add(get_message, level=level,format="{message}")

@hookimpl
def add_option(SRA, option_dict):
    global start_time
    start_time = time()

@hookimpl
def stop(SRA):
    elapsed_time = str(time()-start_time)
    notify_log(_("运行完成, 总耗时: {elapsed_time}").format(elapsed_time=elapsed_time))

def notify_log(content=""):
    """
    默认推送日志
    """
    config = read_json_file(CONFIG_FILE_NAME)
    notifier = config.get('ONEPUSH', {}).get('notifier', '')
    params = config.get('ONEPUSH', {}).get('params', '')
    if not notifier or not params:
        log.error('未配置推送或未正确配置推送')
        return
    if not config.get('ONEPUSH', {}).get('title', ''):
        config['ONEPUSH']['title'] = ''
    return notify(notifier, content=content, **params)
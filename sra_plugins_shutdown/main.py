'''
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2023-06-08 14:19:52
LastEditors: Night-stars-1 nujj1042633805@gmail.com
LastEditTime: 2023-06-08 14:30:50
Description: 

Copyright (c) 2023 by Night-stars-1, All Rights Reserved. 
'''
from . import *

from utils.log import log
from subprocess import run, DEVNULL

@hookimpl
def stop(SRA):
    shell = ["shutdown", "-s", "-f", "-t", "60"]
    result = run(shell, shell=True, capture_output=True)
    log.info("将在{shutdown_time}后关机".format(shutdown_time=result.stdout))
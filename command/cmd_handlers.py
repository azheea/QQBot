import json
# import command.handlers as handlers
import logging
from logging.handlers import RotatingFileHandler
import importlib

# 配置日志
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file = './log.txt'


handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
handler.setFormatter(log_formatter)
handler.setLevel(logging.DEBUG)

# 创建一个 logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

#我是谁?
who_im_i = {"guild":"","group":"","private":""}

with open("./command/commands.json", encoding="utf-8") as f:
    commands = json.load(f)

for a, value in commands.items():
    module_name = value.get('name')
    exec(f"from command.command.{module_name} import *")
    print(f"指令 {module_name} 已加载")



def execute_function(func_name, *args, **kwargs):
    # 获取当前全局作用域中的函数
    global_functions = globals()
    if func_name in global_functions and callable(global_functions[func_name]):
        # 执行同名函数，并传递参数
        return global_functions[func_name](*args, **kwargs)
    else:
        print(f"Function {func_name} not found or not callable.")

def icommand(icommand_word: str, userid: str,cmdfrom:str) -> str:
    command = icommand_word.split()
    if not command:
        return "无效的命令 使用/帮助 获取帮助"

    keyword = command[0]
    arguments = command  # 获取命令的参数部分
    arguments.insert(0, userid)  # 将 userid 添加到参数列表中
    # arguments.insert(1, cmdfrom)  # 将 cmfrom 添加到参数列表中
    #参数现在是["cmd_sender" "cmd_from" "cmdxxxx"] 不出意外的话

    # 遍历 commands 字典
    for key, value in commands.items():
        if keyword in value["keywords"]:
            if value["enable"] == True:    
                #权限部分的实现,说实在的,我也没想好,按照 0-全体/1-我/2-妖魔鬼怪吧
                #鉴权
                if value["permission"] == 1:
                    if who_im_i.get(cmdfrom) == userid:
                        #插进来的热更新
                        if keyword == "/reload":
                            hot_update = []
                            for a, value in commands.items():
                                module_name = value.get('name')
                                # print(module_name)
                                importlib.reload(importlib.import_module(f"command.command.{module_name}"))
                                hot_update.append(f"指令 {module_name} 已重新加载")
                            hot_update = "\n".join(hot_update)
                            result = f"热重载完成! {hot_update}"
                        else:
                            #不是热更新,正常执行命令
                            result = execute_function(value["name"], *arguments)
                    else:
                        result = "您无权限执行此命令!"
                else:
                        result = execute_function(value["name"], *arguments)
            else:
                return "inv"
            # 记录 arguments 和 result
            logger.debug(f"Command: {icommand_word}, User ID: {userid}, Arguments: {arguments}, Result: {result}")
            return result
    
    return "无效的命令 使用/帮助 获取帮助"
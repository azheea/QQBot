# -*- coding: utf-8 -*-
import os
import subprocess

import json

import requests

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
# from botpy.ext.command_util import Commands
from botpy.message import C2CMessage,GroupMessage,Message
# from botpy.manage import GroupManageEvent

config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))
path = os.path.dirname(os.path.abspath(__file__))
_log = logging.get_logger()
_log.setLevel(0)

repo_url = "https://github.com/azheea/QQBot.git"
with open("./info.json") as f:
    cfg = json.load(f)
version = cfg["version"]

repo_version = version

print(f"当前本地机器人版本:{version},救生员已启动!")
def do(mode):
    global repo_version 
    global version
    # print(mode)
    if "/开机" in mode:
        try:
            subprocess.Popen(['python', 'BotMain.py'])
            return "已开机!"
        except Exception as e:
            return "线程创建被阻止!"

    if "/检查更新" in mode:
        try:
            #我操凭什么不能用git archvie
            #傻逼gogs gogs小人,不得续用！！！！！！！！！！！！！！！！！！！！！！
            # c = subprocess.Popen(["git", "archive", f"--remote={repo_url}",f"--output={path}/temp.json","HEAD:info.json"])
            # print(c)

            # with open("./temp.json") as w:
            #     print(w)
            #     a = json.load(w)
            #     print(a)

            a = json.loads(requests.get("https://github.com/azheea/QQBot/raw/main/info.json").text)
            

            repo_version = a.get("version")
            with open("./info.json") as f:
                cfg = json.load(f)
            version = cfg["version"]

            if(version != repo_version):
                return f"当前机器人版本{version},repo中版本为{repo_version},请及时更新以同步特性"
            else:
                return f"当前为最新版本{repo_version}"
        except Exception as e:
            return e

    if "/更新" in mode:
        try:
            # print(version,repo_version
            if(version != repo_version):
                # a = git.Repo.git.pull(repo_url,repo_dir)
                result = subprocess.run(["git", "pull"], cwd=path, check=True, text=True, capture_output=True)
                print(result)
                return result
            else:
                return f"当前为最新版本{repo_version}"

        except Exception as e:
            return e

    if "/启动" in mode:
        try:
            subprocess.Popen(['python', 'IsAzheSleep\IsAzheSleep\main.py'])
            return "已启动IsAzheSleep模块!"
        except Exception as e:
            return "线程创建被阻止!"



class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    #群消息模块
    async def on_group_at_message_create(self, message: GroupMessage):
        if message.author.member_openid == "1DB8AEB82A6A62B0857E27034F963C7E":
            message_back = do(message.content)
            if message_back != None:
                messageResult = await message._api.post_group_message(
                    group_openid=message.group_openid,
                    msg_type=0, 
                    msg_id=message.id,
                    content=f"\n{message_back}")

    #私聊模块
    async def on_c2c_message_create(self, message: C2CMessage):
        if message.author.user_openid == "1DB8AEB82A6A62B0857E27034F963C7E":
            message_back = do(message.content)
            if message_back != None:
                await message._api.post_c2c_message(
                    openid=message.author.user_openid, 
                    msg_type=0, msg_id=message.id, 
                    content=f"{message_back}"
                )

    #频道模块
    async def on_at_message_create(self, message: Message):
        message.content = message.content[23:]
        if message.author.id == "1DB8AEB82A6A62B0857E27034F963C7E":
            message_back = do(message.content)
            if message_back != None:
                await message.reply(content=message_back)


if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_messages=True,public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=config["appid"], secret=config["secret"])
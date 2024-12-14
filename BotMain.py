# -*- coding: utf-8 -*-
import os
import json
import command.cmd_handlers as handlers

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.ext.command_util import Commands
from botpy.message import C2CMessage,GroupMessage,Message
from botpy.manage import GroupManageEvent

config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()
_log.setLevel(0)

#bot自己的版本,不必与repo的相同
cfg = {}
version = "0.1.0b4"

with open("./info.json", "r") as f:
    cfg = json.load(f)
cfg["version"] = version
with open("./info.json", "w") as f:
    f.write(json.dumps(cfg))

print(f"机器人启动!当前版本为{version}")

#机器人主程序 
class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_group_add_robot(self, event: GroupManageEvent):
        _log.info("机器人被添加到群聊：" + str(event))
        await self.api.post_group_message(group_openid=event.group_openid,msg_type=0,event_id=event.event_id,content="啊这.的Bot已启用!",)

    async def on_group_del_robot(self, event: GroupManageEvent):
        _log.info("机器人被移除群聊：" + str(event))

    #群消息模块
    async def on_group_at_message_create(self, message: GroupMessage):
        message_back = handlers.icommand(message.content,userid=message.author.member_openid,cmdfrom="group")
        _log.debug("handler from group")
        if message_back != "inv":
            await message._api.post_group_message(
                group_openid=message.group_openid,
                msg_type=0, 
                msg_id=message.id,
                content=f"\n{message_back}")

    #私聊模块
    async def on_c2c_message_create(self, message: C2CMessage):
        message_back = handlers.icommand(message.content,userid=message.author.user_openid,cmdfrom="private")
        _log.debug("handler from dm")
        if message_back != "inv":
            await message._api.post_c2c_message(
                openid=message.author.user_openid, 
                msg_type=0, msg_id=message.id, 
                content=f"{message_back}"
            )

    #频道模块
    async def on_at_message_create(self, message: Message):
        _log.debug("handler from guild")
        message.content = message.content[23:]
        message_back = handlers.icommand(message.content,userid=message.author.id,cmdfrom="guild")
        if message_back != "inv":
            await message.reply(content=message_back)


if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_messages=True,public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=config["appid"], secret=config["secret"])
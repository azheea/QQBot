# QQBot

使用官方api实现的QQ机器人

## 开始

***推荐使用 `git clone https://github.com/azheea/QQBot.git`进行下载 方便更新***

### 准备

在[QQ开放平台](https://q.qq.com "QQ开放平台")申请一个机器人 并填写appid与密钥至config.yaml(必须)

```
appid: ""
secret: ""
```

python >= 3.8(必须)

Git(可选)

### 部署

```bash
git clone https://github.com/azheea/QQBot.git
cd QQBot
pip install -r requirements.txt
```

接下来

`py main.py`

请在群\私聊 、QQ频道分别使用一次/debug

将获取的id分别填入lifeguard.py command\cmd_handlers.py中 其中私聊与群聊的id一致

> Warning:后续版本将不会直接编辑代码

停止main.py


之后要启动机器人 建议使用 `py lifeguard.py`启动机器人

import json
with open("./info.json", "r") as f:
    cfg = json.load(f)
version = cfg["version"]
info = f"""COPYRIGHT 啊这.
使用的开源项目:
azheea/score_to_school(GPLv3)
azheea/IsAzheSleep(GPLv3)
希望各位点点star喵!
当前bot版本{version}"""

def about(*arguments):
    return info

import requests
import json

all_news = []
def rwonline(*arguments):
    try:
        returns = (requests.get(url="http://46.3.103.33:50001/api/online")).text
        print(returns)
        text = json.loads(returns)
        stat = text.get("result")
        num = text.get("message")
        if int(num) == -1:
            return f"当前在线人数:{num},原生态你个杂鱼"
        else:
            return f"服务器在线,当前在线人数:{num}"
    except:
        return f"服务器不在线"
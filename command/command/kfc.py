import requests
import json
def kfc(*arguments):
    text = json.loads((requests.get("https://api.pearktrue.cn/api/kfc")).text)
    return "".join(text.get("text"))
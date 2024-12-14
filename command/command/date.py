import requests
import json
def date(*arguments):
    text = json.loads((requests.get("https://api.pearktrue.cn/api/countdownday/")).text)
    return "\n".join(text.get("data"))
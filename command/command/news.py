import requests
import json

# all_news = []
# def news(n_type,a):
#     if n_type != "":
#         if n_type == "沙雕":
#             text = json.loads((requests.get("https://api.pearktrue.cn/api/random/duanzi/")).text)
#             return text.get("duanzi")
#         elif n_type == "科技":
#             text = json.loads((requests.get("https://api.pearktrue.cn/api/sciencenews/")).text)
#             data = text.get("data")
#             for news in data:
#                 all_news.append(news.get("title"))
#             return "\n".join(all_news)
#         else:
#             return "无效的参数"
#     else:
#         return "缺少参数,请使用/help获取帮助"
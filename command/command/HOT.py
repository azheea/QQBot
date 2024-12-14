import requests
import json

# all_news = []
# def HOT(n_type,a):
#     if n_type != "":
#             text = json.loads((requests.get(f"https://api.pearktrue.cn/api/dailyhot/?title={n_type}")).text)
#             data = text.get("data")
#             for news in data:
#                 all_news.append(news.get("title"))
#             returns = "\n".join(all_news)
#             print(returns)
#             return returns 
#     else:
#         return "缺少参数,请使用/help获取帮助"
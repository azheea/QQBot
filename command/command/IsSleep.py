import requests

def IsSleep(*arguments) -> str:
    arguments = list(arguments)
    # print(arguments)
    if len(arguments) >= 2:
        arguments.append("")
    status = arguments[2]
    userid = arguments[0]
    if status == "":
        try:
            text = requests.get(url="http://127.0.0.1:7788/api").text
            return f"啊这.现在{text}"
        except Exception as e:
            return f"发生异常: {str(e)}"
    elif userid == "1DB8AEB82A6A62B0857E27034F963C7E":
        try:
            response = requests.post(url="http://127.0.0.1:7788/api", json={"key": "azhesleep", "status": status})
            response.encoding = 'utf-8'  # 设置响应编码
            if response.status_code == 200:
                return response.json()  # 解析 JSON 内容并返回
            else:
                return f"请求失败，状态码: {response.status_code}"
        except Exception as e:
            return f"发生异常: {str(e)}"
    else:
        return "无效的参数.你没有权限更改状态"
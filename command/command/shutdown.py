import requests

def shutdown(*arguments) -> str:
    arguments = list(arguments)
    userid = arguments[0]
    if userid == "1DB8AEB82A6A62B0857E27034F963C7E":
        exit()
    else:
        return "你没有权限执行此命令"
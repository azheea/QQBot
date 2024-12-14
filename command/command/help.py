import json

with open("./command/commands.json", encoding="utf-8") as _:
    commands = json.load(_)
def help(*arguments):
    # print(arguments)
    all_commands = []
    for key,value in commands.items():
        if value.get('show') == True:
            all_commands.append(f"命令\n{str(value.get('keywords'))}\n  -{value.get('description')}\n")
    return "\n".join(all_commands)
import json
import random

with open("./cards.json", encoding="utf-8") as f:
    tarots = json.load(f)

explains = ["过去", "现在", "未来", "建议", "环境", "希望发生的事情", "结果"]
def tarot(*arguments):
    arguments = list(arguments)
    if len(arguments) <= 2:
        arguments.append("")
    # print(arguments)
    agree = arguments[2]
    picking_tarots = {}
    if agree != "开始":
        return "欢迎使用塔罗牌\n使用 /塔罗 开始 以开始\n请先默念你想要知道的内容 \n注意 本功能仅属于娱乐 若吞消息则证明违规了("
    
    card_statuss = ["正位", "逆位"]
    picking_tarots = {}

    while len(picking_tarots) < 7:
        card_name = random.choice(list(tarots.keys()))
        seed = random.randint(0, 1)
        card_status = card_statuss[seed]
        # print(seed)
        # print(card_status, card_name)
        if picking_tarots.get(card_name) == None:
            step = explains[len(picking_tarots)]
            ans = ((tarots.get(card_name)).get(card_status)).get(step)
            if ans == None and step == "希望发生的事情":
                ans = ((tarots.get(card_name)).get(card_status)).get("希望的事情")
            picking_tarots[f"第{len(picking_tarots)+1}张牌 {card_name} {card_status}"] = f"你所希望知道的这件事的{step}:\n{ans}"

    result = ""
    for key, value in picking_tarots.items():
        result += f"{key}\n{value}\n"

    return result
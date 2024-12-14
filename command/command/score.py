import command.command.score_to_school.main as getscore
#/分数 省份名称 年份 专业名称
def score(*arguments) -> str:
    arguments = list(arguments)
    # print(arguments)
    if len(arguments) <= 4:
        return "无效的参数,命令格式/分数 省份名称 年份 专业名称"
    userid = arguments[0]
    province_id = arguments[2]
    year = arguments[3]
    if year.isdigit() == True:
        if int(year) > 2024 or int(year) <= 2019:
            return "年份无效..."
    else:
        return "年份无效..."
    want = arguments[4]
    allscore = getscore.main(province_id, year, want)
    answer = f"{province_id} {want} {year}年录取分数如下:\n"    
    for key, value in allscore.items():
        answer = f"{answer}学校:{key} 专业:{value.get('spname')} 最低分数:{value.get('min')} 最低排名:{value.get('min_section')}\n"
    return answer
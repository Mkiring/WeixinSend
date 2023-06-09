def weather(max:int,min:int):
    if min >=10: # 温度上限20°C以上
        tips = "近日早晚天热，记得适当减少衣物哦"
    else :
        if min <=10:
            tips = "近日早晚天凉，记得适当添加衣物哦"
        else:
            tips = ""
    return tips


def zhiri(i: int):
    zhiri_list = ["103寝室", "2032寝室", "2033寝室", "2034寝室", "2035寝室"]
    if (i >= 0 and i <= len(zhiri_list)-1):
        zhiri = "今天该%s扫地哦" % (zhiri_list[i])
    else:
        if (i == 6):
            zhiri = "今天该%s扫地哦" % (zhiri_list[4])
        else:
            zhiri = ''
    return zhiri


def weekday(i: int):
    weekday_list = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    if (i >= 0) and (i <= len(weekday_list)-1):
        today = weekday_list[i]
    else:
        today = ''
    return today


def emjoy(i: int):
    emjoy_list = [
        "(*^o^*)",
        "(◦˙▽˙◦)",
        "(*σ´∀`)σ",
        "( ͡° ͜ʖ ͡°)✧",
        "٩(*´◒`*)۶",
        "(｡>∀<｡)",
        "(๑´∀`๑)",
        "(◕ˇ∀ˇ◕)",
        "ヾ(´∀｀。ヾ)",
        "੭ ᐕ)੭*⁾⁾",
        "ヾ(✿ﾟ▽ﾟ)ノ",
        "(*^ω^*)",
        "(=^▽^=)",
        "(*^▽^*)",
        "(-^o^-)",
        "╮(‵▽′)╭",
        "ヾ(^▽^*)))",
        "╰(*´︶`*)╯",
        "٩(๑^o^๑)۶",
        "✧٩(ˊωˋ*)و✧",
        "(*˘︶˘*).。.:*♡",
        "(*๓´╰╯`๓)♡",
        "(๑•॒̀ ູ॒•́๑)啦啦啦",
        "✧*。٩(ˊωˋ*)و✧*。",
        "ヾ(@^▽^@)ノ ",
        "o((*^▽^*))o ",
        "O(≧▽≦)O",
        "(´▽｀)ノ♪",
        "(^３^)╱~~",
        "(/≧▽≦)/~┴┴ ",
        "(￣y▽￣)~*捂嘴偷笑",
        " o(*≧▽≦)ツ ~ ┴┴",
        "٩(●´৺`●)૭٩(●´৺`●)و",
        ".ヽ(^Д^*)/. ",
        "(≧ω≦)/",
        "*(^o^)/*",
        "ヽ(*^^*)ノ",
        "（∩▽∩）"]
    if (i >= 0) and (i <= len(emjoy_list)-1):
        emjoy = emjoy_list[i]
    else:
        emjoy = ''
    return emjoy

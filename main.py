import requests
import json
import datetime
import time
import random
import os
import platform
# 自定义python模块(week.py)
import week

# 获取当前路径
path = os.getcwd()
# 随机数方法获取小K每日随机心情
emjoy_radom = round(random.randint(1, 38))-1

weixin_template_id = []
weixin_user_ID = []
city_code = []
city_name = []
provide = []
birth_next = []
birthday_next = []

# 加载本地配置
if (platform.system() == 'Linux'):
    with open(path+'/config.json', 'r', encoding='utf-8') as f:
        json_j = json.loads(f.read())
else:
    if (platform.system() == 'Windows'):
        with open(path+'.\\Python\\WeixinSend\\config.json', 'r', encoding='utf-8') as f:
            json_j = json.loads(f.read())
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 浏览器标头区域
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}  # 浏览器请求标头

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 时间区域
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
time_m = datetime.datetime.now()
time_t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 下一次生日时间
birth_next.append(datetime.datetime(2024, 3, 11))
birth_next.append(datetime.datetime(2024, 2, 20))

# 获取下一次生日时间差
for i in range(2):
    birthday_next.append((birth_next[i] - time_m).days)


# 顾名思义，开始时间
love_day = datetime.datetime(2023, 3, 22)

# 获取爱情时间差
love_day = (time_m - love_day).days

# 获取值日人员信息
clean_people = week.zhiri(datetime.datetime.now().weekday())

# 获取今日是星期几
today = week.weekday(datetime.datetime.now().weekday())

emjoy = week.emjoy(emjoy_radom)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 配置区域
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 微信appID
weixin_appID = json_j['weixin_appID']

# 微信weixin_appsecret
weixin_appsecret = json_j['weixin_appsecret']

# 微信access_token
weixin_access_token = json_j['weixin_access_token']

# 推送消息模板ID
weixin_template_id.append(json_j.get('weixin_template')[0].get('template_ID'))
for i in range(2):
    # 已关注测试号的用户openID
    weixin_user_ID.append(json_j.get('weixin_user_ID')[i].get('weixin_openID'))

# 城市ID
    city_code.append(json_j.get('city')[i].get('city_code'))

# 城市名称
    city_name.append(json_j.get('city')[i].get('city_name'))

# 城市所属省份
    provide.append(json_j.get('city')[i].get('provide'))

# 和风天气token
hefeng_token = json_j.get('hefeng_token')

# 今日诗词token
jinrishici_token = json_j.get('jinrishici_token')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 链接和URL调用区域
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 今日诗词调用URL
# jinrishici_url = 'https://v2.jinrishici.com/sentence'
# headers['X-User-Token'] = jinrishici_token

# 一言URL
yiyan_url = "https://v1.hitokoto.cn/"

# 和风天气地址查询URL
# hefeng_city_url = "https://geoapi.qweather.com/v2/city/lookup?location=%s&adm=%s&key=%s" %(city_name, provide, hefeng_token)


# 一个野生的天气查询URL
weather_url = "http://t.weather.sojson.com/api/weather/city/%s" % (city_code)

# 微信access_token_URL
weixin_get_access_token_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (
    weixin_appID, weixin_appsecret)

# 获取微信access_token
weixin_access_token = json.loads(requests.get(
    url=weixin_get_access_token_url, timeout=5).text).get('access_token')

# 模板消息发送url
weixin_url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s" % (
    weixin_access_token)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 数据发送区域
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 获取一言相应数据
yiyan = json.loads(requests.get(url=yiyan_url, timeout=5).text).get('hitokoto')

for i in range(2):
    if i == 1:
        clean_people = ''
    # 和风天气查询URL
    hefeng_url = "https://devapi.qweather.com/v7/weather/3d?location=%s&key=%s" % (
        city_code[i], hefeng_token)
    # 获取和风天气相应数据
    hefeng = json.loads(requests.get(url=hefeng_url, timeout=15).text)

    weather = hefeng.get('daily')[0].get('textDay')  # 天气 当日
    tmpMax = hefeng.get('daily')[0].get('tempMax')  # 最高温
    tmpMin = hefeng.get('daily')[0].get('tempMin')  # 最低温
    moonPhase = hefeng.get('daily')[0].get('moonPhase')  # 月相

    time_next = hefeng.get('daily')[1].get('fxDate')  # 获取第二天时间 第二日
    weather_next = hefeng.get('daily')[1].get('textDay')  # 天气
    tmpMax_next = hefeng.get('daily')[1].get('tempMax')  # 最高温
    tmpMin_next = hefeng.get('daily')[1].get('tempMin')  # 最低温
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#

    weixin_post_data = {
        "touser": weixin_user_ID[i],  # 测试号关注用户
        "template_id": weixin_template_id[0],  # 模板消息ID
        "client_msg_id": str(time_t),  # 防重id
        "data": {
            "time": {
                "value": "%s %s" % (time_t, today),  # 时间区域
                "color": "#c96e8c"
            },
            "city": {
                "value": provide[i],  # 城市
                "color": "#c96e8c"
            },
            "parent": {
                "value": city_name[i],  # 省份
                "color": "#c96e8c"
            },
            "type": {
                "value": weather,  # 今日天气
                "color": "#e7b688"
            },
            "tep_high": {
                "value": tmpMax+"°C",  # 高温
                "color": "#c71c33"
            },
            "tep_low": {
                "value": tmpMin+"°C",  # 低温
                "color": "#2892d4"
            },
            "tianqi": {
                "value": "  明天是: %s"
                "\n  天气: %s"
                "\n  最高温度: %s°C"
                "\n  最低温度: %s°C" % (time_next, weather_next,
                                    tmpMax_next, tmpMin_next),  # 近三天天气
                "color": "#2ab5d5"
            },
            "notice": {
                "value": "\n  小K今日心情: %s"
                "\n  小K提醒: "
                "\n    近日早晚温度较低，早上和夜晚记得穿厚点哦" % (emjoy),  # 穿衣贴士
                "color": "#982f4d"
            },
            "love_days": {
                "value": "Miko已经陪伴你%s天" % (love_day),  # 和Miko的时光
                "color": "#da8b41"
            },
            "birthday_left": {
                "value": "%s天" % (birthday_next[i]),  # 生日
                "color": "#c96e8c"
            },
            "words": {
                "value": yiyan+"\n",  # 一言
                "color": "#7c34a9"
            },
            "zhiri": {
                "value": clean_people,  # 值日信息
                "color": "#20a175"
            },
        }
    }
    content = requests.post(
        url=weixin_url, json=weixin_post_data, timeout=5).text
    print(content)

'''

模板消息
今天是：{{time.DATA}}
您所在的城市是：{{city.DATA}}{{parent.DATA}}  
今日天气：{{type.DATA}} 
日最高温：{{tep_high.DATA}}
日最低温：{{tep_low.DATA}}
{{tianqi.DATA}}
{{notice.DATA}}
{{love_days.DATA}}
距离下一个生日还有：{{birthday_left.DATA}}
{{words.DATA}}
{{zhiri.DATA}}
'''
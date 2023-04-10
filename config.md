## config.json字段注释
#### weixin_appID
  你的微信测试号ID
  
#### weixin_appsecret
  你的微信测试号token

#### weixin_access_token
  测试号与微信服务器通信所需要的token，7200s有效期
  获取方式：GET https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=appID&secret=appsecret

#### city
  城市代码
###### city_name
  城市名
###### city_code
  城市id

  
#### weixin_template
  微信测试号推送消息模板

###### title
  消息模板标题
###### template_token
  消息模板ID


#### weixin_user_ID
  关注你的测试号的用户数组
    
###### weixin_userID
  关注你的测试号的用户昵称
###### weixin_openID
  关注你的测试号的用户的token

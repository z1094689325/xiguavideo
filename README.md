这是抓取西瓜视频app的小项目

1. getJson.py：此模块的功能是传入一个url，返回url对应的json，文件中有一个类GetJson，其中有个方法getJson(),需要传入url，headers两个参数，headers可有可无。返回没有处理过的json格式的数据。
2. getNewVideos.py：此模块的功能是 ：返回西瓜视频的最新推荐视频的json数据，其中有一个类GetNewVideos，类中有getNewVideos()方法，不需要传参，把一次请求到的json数据处理后存入一个新的字典里。main()方法的目的是让返回的字典中的数据超过20条；saveMongo()把数据存入到MongoDB。getToMongo()把MongoDB中的数据提取出来，随机取20个返回。
3. getUserInfo.py：此模块的功能是根据用户id，返回用户信息的json字符串，其中有一个类GetUserInfo，有一个函数getUserInfo()需要一个参数，user_id，返回用户信息的json
4. getUserVedio.py：此模块的功能是根据用户的id和视频数量，返回对应的用户的视频信息，实例化需要user_id和video_total_count俩个参数。此模块中有一个类GetUserVedio，使用时调用main()函数，返回json
5. getVideoInfo.py：此模块的功能是播放用户的视频的时候，返回视频参数，需要三个参数video_id：视频id, play_auth_token：视频授权, play_biz_token：视频播放令牌，这三个参数缺一不可，在getUserVedio中返回的参数中含有这三个参数。模块中有一个类GetVideoInfo,使用时调用getVideoInfogetVideoInfo(video_id, play_auth_token, play_biz_token)，返回视频信息的json
6. xigua_app.py：此模块的功能是根据group_id(和video_id相同)返回对应的评论信息，使用时调用get_pinglun_info(group_id)，传入一个group_id，返回对应的评论的json字符串。


* * *

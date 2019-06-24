

import json

from flask import Flask, render_template,request

from getNewVideos import GetNewVideos

from getUserInfo import GetUserInfo

from getUserVedio import GetUserVedio

from getVideoInfo import GetVideoInfo

from xigua_app import Film

app = Flask(__name__)

@app.route('/newvideo.json')
def getNewVideos():
    
    x = GetNewVideos()

    videos = x.getToMongo()

    return json.dumps(videos, ensure_ascii = False)



@app.route('/userinfo.json')
def getUserInfo():

    user_id = '179946784569095'
    
    user_info = GetUserInfo().getUserInfo(user_id)

    return json.dumps(user_info,ensure_ascii=False)



@app.route('/videoinfo.json')
def getVideoInfo():

    video_id = 'v02004130000bk44i7qk781i15g2vqv0'

    play_auth_token = 'HMAC-SHA1:2.0:1561106335101074982:bab42eac5b9e4a8eb25a91fc371ad533:INRhzA/CMuOgFPz8yb3V1jrM2hw='

    play_biz_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjExMDYzMzUsInZlciI6InYxIiwiYWsiOiJiYWI0MmVhYzViOWU0YThlYjI1YTkxZmMzNzFhZDUzMyIsInN1YiI6InBnY18xMDgwcCJ9.F5qYiCcXEwpGt-qsUuXtZzID3f8OuI8TEJtv5pwc5tg'

    v = GetVideoInfo().getVideoInfo(video_id, play_auth_token, play_biz_token)

    return json.dumps(v, ensure_ascii=False)


@app.route('/uservideos.json')
def getUserVideos():

    user_id = '179946784569095'

    num = '120'

    user_videos = GetUserVedio(user_id, num).main()

    return json.dumps(user_videos, ensure_ascii=False)


@app.route('/comment.json')
def getComment():
    
    group_id = '6703874839536468493'
    
    comments = Film().get_pinglun_info(group_id)
    
    
    return json.dumps(comments, ensure_ascii=False)









app.run(host='127.0.0.1',port=5000)
    

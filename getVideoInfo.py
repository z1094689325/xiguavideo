

import  base64

from getJson import GetJson


class GetVideoInfo:

    '''获取视频信息'''
    def __init__(self):
        #Authorization 是授权  视频参数里传过来
        self.headers = {
            'Accept-Encoding': 'gzip',
            'Authorization': '',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; xiaomi 8 Build/LMY48Z) VideoArticle/7.6.5 ok/3.10.0.2',
            'Cookie': 'odin_tt=67694c726859616c76685a764e796677765d9bb577116779bc2005ad89008ae35b0e708cf8af76d1755078ef80a54431b26fb2209cd255d88878b8956ce1e6dd; qh[360]=1; _ga=GA1.2.857360671.1560845721; _gid=GA1.2.920658333.1560845721; install_id=75706685885; ttreq=1$8a0c313082fc55b027a88743ff7005881a180e98',
            }
    
        self.url_format = 'https://is.snssdk.com/video/openapi/v1/?action=GetPlayInfo&video_id={}&ptoken={}'
    
        self.video_infos = {}
        
        
    
    def getVideoInfo(self,video_id, play_auth_token, play_biz_token):

        'video_id 视频id, play_auth_token  视频授权, play_biz_token 视频播放令牌, 请求失败返回None'
        
        url = self.url_format.format(video_id, play_biz_token)

        self.headers['Authorization'] = play_auth_token

        rst = GetJson().getJson(url, headers=self.headers)

        if rst != None :

            info = rst['video_info']['data']
        
        else:

            return None

        video_list = info['video_list']

        for i in video_list :
            #视频地址是base64加密的
            self.video_infos[video_list[i]['definition']] = str(base64.b64decode(video_list[i]['main_url']).decode('utf-8'))
        
        return {info['video_id'] : self.video_infos}


if __name__ == '__main__' :

    x = GetVideoInfo()

    video_id = 'v02004130000bk44i7qk781i15g2vqv0'

    play_auth_token = 'HMAC-SHA1:2.0:1561106335101074982:bab42eac5b9e4a8eb25a91fc371ad533:INRhzA/CMuOgFPz8yb3V1jrM2hw='

    play_biz_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjExMDYzMzUsInZlciI6InYxIiwiYWsiOiJiYWI0MmVhYzViOWU0YThlYjI1YTkxZmMzNzFhZDUzMyIsInN1YiI6InBnY18xMDgwcCJ9.F5qYiCcXEwpGt-qsUuXtZzID3f8OuI8TEJtv5pwc5tg'

    v = x.getVideoInfo(video_id, play_auth_token, play_biz_token)
    

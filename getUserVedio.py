
from getJson import GetJson
from math import ceil

class GetUserVedio:

    '''获取用户全部视频'''

    def __init__(self, user_id, video_total_count):
        
        self.videos = {}

        self.user_id = user_id

        self.video_total_count = video_total_count

        self.time_stamp = None

        self.url_format = 'https://is.snssdk.com/video/app/user/videolist/v2/?to_user_id={}&isBackground=False&tab=video&series_lvideo=0&next_offset=0{}&iid=75706685885&device_id=68332167897&ac=wifi&channel=tengxun2&aid=32&app_name=video_article&version_code=765&version_name=7.6.5&device_platform=android&ssmix=a&device_type=xiaomi+8&device_brand=xiaomi&language=zh&os_api=22&os_version=5.1.1&uuid=865166025860498&openudid=63c441172837d6bc&manifest_version_code=365&resolution=720*1280&dpi=320&update_version_code=76502&_rticket=1560923145723&fp=c2TZFlxOPl5ZFlTrcrU1F2m7LrcI&tma_jssdk_version=1.16.3.0&rom_version=LMY48Z'

        self.headers = {

        'Accept-Encoding': 'gzip',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; xiaomi 8 Build/LMY48Z) VideoArticle/7.6.5 ok/3.10.0.2',
        'Cookie': 'install_id=75706685885; ttreq=1$8a0c313082fc55b027a88743ff7005881a180e98; odin_tt=67694c726859616c76685a764e796677765d9bb577116779bc2005ad89008ae35b0e708cf8af76d1755078ef80a54431b26fb2209cd255d88878b8956ce1e6dd; _ga=GA1.2.857360671.1560845721; _gid=GA1.2.920658333.1560845721; qh[360]=1'
        
        }

    def getNextVedio(self):

        '获取用户视频，单词请求返回30个'

        if self.time_stamp == None:

            url = self.url_format.format(self.user_id, '')

        else:
            
            param = '&max_behot_time={}'.format(self.time_stamp)

            url = self.url_format.format(self.user_id, param)

        

        rst = GetJson().getJson(url,headers=self.headers)
        
        if rst != None :
            
            info = rst['data']

            for i in info:
    
                vedio = dict(
                    #标题
                    title = i['title'],
                    #视频摘要
                    abstract = i['abstract'],
                    #时间
                    behot_time = i['behot_time'],
                    #评论数
                    comment_count = i['comment_count'],
                    #id
                    group_id_str = i['group_id_str'],
                    #发布时间
                    publish_time = i['publish_time'],
                    #视频id  Url需要
                    video_id = i['video_id'],
                    #授权 需要添加到请求头
                    play_auth_token = i['play_auth_token'],
                    #播放令牌  url需要
                    play_biz_token = i['play_biz_token'],
                    #展示图片url
                    img = i['video_detail_info']['detail_video_large_image']['url'],
                    #西瓜原地址
                    url = i['article_url'],
                    #点赞人数
                    video_like_count = i['video_like_count'],
                    #播放次数
                    video_watch_count = i['video_detail_info']['video_watch_count'],

                    user_info = dict(

                        name = i['user_info']['name'],

                        author_desc = i['user_info']['author_desc'],

                        description = i['user_info']['description'],

                        user_id = i['user_info']['user_id'],

                    )
    
                )
    
                self.videos[i['video_id']] = vedio
                
                print('存入成功。。。。')
    
            self.time_stamp = self.videos[list(self.videos.keys())[-1]]['behot_time']

    def main(self):
        
        '''获取所有用户视频，可以多线程处理'''

        page = ceil(int(self.video_total_count)/30)

        for i in range(page):

            self.getNextVedio()

        return {'user_video' : self.videos}
    

if __name__ == '__main__' :

    x = GetUserVedio('179946784569095','130')

    v_info = x.main()

        
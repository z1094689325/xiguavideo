

import base64
import json
import time
import pymongo

import random

from math import ceil

from getJson import GetJson


class GetNewVideos:
    
    '''获取最新推荐的视频,每次至少返回20个视频信息'''
    
    
    def __init__(self):
        
        
#        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        #连接MongoDB
        self.client = pymongo.MongoClient("mongodb://140.143.206.157:27017/")
        
        self.db = self.client.test
        
        self.tab_video = self.db.newvideos

               
        self.url_format = 'http://is.snssdk.com/video/app/stream/v51/?category=video_new&min_behot_time={}&last_refresh_sub_entrance_interval={}'
        #存储视频信息
        self.videos = {}
        #获取最后一个视频的behot_time
        self.time_stamp = None


    def getNewVideos(self):
        
        '''获取视频信息存入字典'''

        #最新时间
        last_refresh_sub_entrance_interval = ceil(time.time())

        min_behot_time = self.time_stamp

        url = self.url_format.format(min_behot_time, last_refresh_sub_entrance_interval)
        #请求成功返回json，失败返回None
        rst = GetJson().getJson(url)
        #如果返回None，直接跳出函数
        if rst != None:
            
            info = rst['data']
        
        else :
            
            return 
        
        for i in info :
            #content是字符串，转成字典
            content = json.loads(i['content'])
            #视频播放的json
            video_play_info = json.loads(content['video_play_info'])['video_list']
            #存放视频的字典
            video_play_infos = {}
            #获取视频信息，原视频地址是base64加密，这里进行了解密
            for i in video_play_info:
                
                video_play_infos[video_play_info[i]['definition']] = str(base64.b64decode(video_play_info[i]['main_url']).decode('utf-8'))
            #如果用户信息为空，name用户为None
            if content['user_info'] != None :
                
                user_info = dict(
                        
                        #编号
                        user_id = content['user_info']['user_id'],
                        #用户名
                        name = content['user_info']['name'],
                        #签名
                        author_desc = content['user_info']['author_desc'],
                        #头像
                        avatar_url = content['user_info']['avatar_url'],
                    )
            else :

                user_info = None
            #电影信息的字典    
            vedio = dict(

                    #标题
                    title = content['title'],
                    #简介摘要
                    abstract = content['abstract'],
                    #视频地址
                    article_url = content['article_url'],
                    #视频Id
                    video_id = content['video_id'],
                    #点赞数
                    video_like_count = content['video_like_count'],
                    #播放数
                    video_watch_count = content['video_detail_info']['video_watch_count'],
                    #最热时间
                    behot_time = content['behot_time'],
                    #发布时间
                    publish_time = content['publish_time'],
                    #标签
                    tag = content['tag'],
                    #评论数
                    comment_count = content['comment_count'],
                    #用户信息
                    user_info = user_info,
                    #分类信息
                    log_pd = dict(
                        #分类名称
                        category_name = content['log_pb']['category_name'],
                        #分类id
                        group_id = content['group_id'],
                    ),
                    #视频播放信息
                    video_play_info = video_play_infos
                )
            
            #电影的组Id为key
            self.videos[str(content['id'])] = vedio
            
            print(len(self.videos))
        #把最后一个视频的behot——time赋值给time_stamp
        self.time_stamp = self.videos[list(self.videos.keys())[-1]]['behot_time']


    def saveMongo(self):
        '''去重存入mongo'''
        for i in self.videos:
            
            info = self.tab_video.find({'id':str(i)})
            
            ls = [j for j in info]
            
            if not ls :
                
                self.tab_video.insert_one({'id':str(i),'video_info':self.videos[i]})
                


    def main(self):
        
        '''保证每次返回的视频数量超过20'''
        #字典中视频的数量
        num = len(self.videos)
        #判断videos中视频的数量，超过20则返回
        while num <20 :
 
            self.getNewVideos()
            
            num = len(self.videos)
            
        self.saveMongo()
        
        return self.videos


    def getToMongo(self):
        
        '''从Mongo中取出所有视频信息,删除_id,随机取出20条'''
        
        videos_info = self.tab_video.find()
        
        ls = []
        
        for i in videos_info :
            
            del i['_id']
            
            ls.append(i)
        
        videos = random.sample(ls, 20)
        
        return {'videos_info':videos}

if __name__ == '__main__' :

    x = GetNewVideos()

#    info = x.main()
    
    info = x.getToMongo()

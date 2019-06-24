# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:51:29 2019

@author: DELL
"""

import requests
from json import loads

class Film:
    
    '''
    
            #用户评论点赞数
            digg_count 
            #用户评论回复个数
            reply_count 
            #用户评论内容
            text 
            #评论用户的名称
            user_name 
            #评论用户头像的图片
            user_profile_image_url 
            #视频封面图片
            cover_url 
            #视频评论个数
            total_number 
            #发布视频的用户的名称
            group_user_name 
            #视频标题
            title
    
    '''
    
    headers = {
        
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; redmi note 4 Build/LMY48Z) VideoArticle/7.6.5 ok/3.10.0.2',
        'Cookie': 'install_id=75665790976; ttreq=1$43c8fed602cc90bd6d0162dbcd3e6f1890aba768; odin_tt=52e3c39c614ca8478696228bddc8f4bf8524901fbf56f90ed8495cef38b3e436bff1e3f3ea4c0ce19c65696fd7b50ade'

        }
    
    domain = 'https://is.snssdk.com/article/v4/tab_comments/?group_id={}'


    '''获取某个视频的评论，点赞，回复等数据'''
    def get_pinglun_info (self,group_id):
        
        res = requests.get(self.domain.format(group_id) , headers = self.headers)
            
        res.encoding = 'utf-8'
        
        info = loads(res.text)
        
        pinglun_content = []
        
        #视频评论个数
        total_number = info['total_number']
        
        if total_number != 0:
        
            pinglun_urls = [self.domain.format(group_id)+'&count=20&offset=%d'%(20*i) for i in range(0,int(total_number/20))]
            
            if total_number%20 != 0:
                
                url = self.domain.format(group_id)+'&count=20&offset=%d'%(total_number - total_number%20)
                
                pinglun_urls.append(url)
            
    #        return pinglun_urls
            
            for l in pinglun_urls:
                
                res = requests.get(l, headers = self.headers)
                    
                res.encoding = 'utf-8'
                
                info = loads(res.text)
                
                #视频封面图片
                cover_url = info['repost_params']['cover_url']
                #发布视频的用户的名称
                group_user_name = info['group']['user_name']
                #视频标题
                title = info['repost_params']['title']
                    
                pinglun_user = [{'digg_count' : i['comment']['digg_count'],\
                           'reply_count' : i['comment']['reply_count'],\
                           'text' : i['comment']['text'],\
                           'user_name' : i['comment']['user_name'],\
                           'user_profile_image_url' : i['comment']['user_profile_image_url']} for i in info['data']]
                
                pinglun_info = dict(
                        
                        cover_url = cover_url,
                        
                        group_user_name = group_user_name,
                        
                        pinglun_user = pinglun_user,
                        
                        title = title
                        
                        )
                
                pinglun_content.append(pinglun_info)
        
        else :
            
            print('此视频暂无评论，还不来抢个沙发？')
            
            pinlun_info = dict(
                    
                    context = '此视频暂无评论，还不来抢个沙发？'
                    
                    )
            
            pinglun_content.append(pinlun_info)
            
        return  {'PL_info':pinglun_content}
    
    
if __name__ == '__main__':
    
    x = Film()
    
#    info = x.get_UP_info(url)
    
#    UP_info = x.get_UP_info(UP_url)
    
    #    info = x.get_UP_info(UP_url_1)
    
#    info = x.get_pinglun_info(pinglun_url)
    
#    info = x.get_shipin_info(info_url)
    
    info1 = x.get_pinglun_info(6677883396015784461)
    
    #    info1 = x.get_pinglun_info(6701999819231068679)
    




from getJson import GetJson

class GetUserInfo:

    '''获取用户信息'''

    headers = {
        'Accept-Encoding': 'gzip',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; xiaomi 8 Build/LMY48Z) VideoArticle/7.6.5 ok/3.10.0.2',
        'Cookie': 'odin_tt=67694c726859616c76685a764e796677765d9bb577116779bc2005ad89008ae35b0e708cf8af76d1755078ef80a54431b26fb2209cd255d88878b8956ce1e6dd; qh[360]=1; _ga=GA1.2.857360671.1560845721; _gid=GA1.2.920658333.1560845721; install_id=75706685885; ttreq=1$8a0c313082fc55b027a88743ff7005881a180e98',
        }
    
    url = 'https://is.snssdk.com/video/app/user/home/v7/?to_user_id={}&device_id=68332167897&channel=tengxun2&version_code=765&device_platform=android'

    def getUserInfo(self, user_id):

        '''根据url获取用户的信息的字典'''

        info = GetJson().getJson(self.url.format(user_id), headers=self.headers)['user_info']

        user_info = dict(
            #用户名
            name = info['name'],
            #
            author_desc = info['author_desc'],
            #粉丝数
            followers_count = info['followers_count'],
            #关注
            following_count = info['following_count'],
            #用户id
            user_id = info['user_id'],
            #视频数
            video_total_count = info['video_total_count'],
            #简介
            description = info['description'],

            share_url = info['share_url'],

            video_total_share_count = info['video_total_share_count'],

        )

        return user_info
    
if __name__ == '__main__' :

    x = GetUserInfo()

    user_info = x.getUserInfo('103798325513')
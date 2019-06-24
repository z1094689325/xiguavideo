
import requests


class GetJson:

    headers = {

        'Accept-Encoding': 'gzip',

        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo y31 Build/LMY48Z) VideoArticle/7.6.5 ok/3.10.0.2'

    }
        
    def getJson(self, url, headers = None):

        if headers == None:

            headers = self.headers

        try:

            rst = requests.get(url, headers = headers)

        except :

            print('连接失败')

            return None

        else:

            rst.encoding = 'utf-8'

            return rst.json()
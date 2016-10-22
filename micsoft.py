import demjson,requests,time
from lxml import etree
from setting import USER_AGENT
from setting import CLIENT_ID,CLIENT_SECRET
from tool import randomChose

class MSAPI:
    def __init__(self):
        self.headers = {'User-Agent': randomChose(USER_AGENT),
                        'content_type': "text/plain"}
        self.proxy = None
        self.expire = 0

    def msTokenGet(self):
        '''
        微软翻译接口token获取
        '''
        url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
        payload = { 'client_id': CLIENT_ID,
                    'client_secret': CLIENT_SECRET,
                    'scope': "http://api.microsofttranslator.com",
                    'grant_type': "client_credentials"}
        response = requests.post(url, headers=self.headers, data=payload)
        response = demjson.decode(response.text)
        token = response['access_token']
        self.expire = float(token.split('&ExpiresOn=')[1].split('&')[0])
        self.headers['Authorization'] = 'bearer %s' % token

    def langDetect(self,data):
        '''
        语言类型检测
        '''
        #token过期则重新获取
        if self.expire - time.time() < 5:
            self.msTokenGet()
        url = 'http://api.microsofttranslator.com/V2/Http.svc/Detect?text=%s'%data
        response = requests.get(url, headers=self.headers)
        htmlCode = response.text
        html = etree.HTML(htmlCode)
        lang = html.xpath('//string/text()')[0]
        return lang

    def translate(self, data, to='zh-CHS'):
        '''
        翻译
        '''
        #token过期则重新获取
        if self.expire - time.time() < 5:
            self.msTokenGet()
        url = 'http://api.microsofttranslator.com/V2/Http.svc/Translate?text=%s&to=%s'%(data,to)
        response = requests.get(url, headers=self.headers)
        htmlCode = response.text
        html = etree.HTML(htmlCode)
        result = html.xpath('//string/text()')[0]
        return result
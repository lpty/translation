import demjson,requests
from setting import USER_AGENT
from tool import randomChose

class BaiDuAPI:
    def __init__(self):
        self.headers = {'User-Agent': randomChose(USER_AGENT)}
        self.proxy = None

    def langdetect(self,data):
        '''
        百度语言类型检测
        '''
        url = 'http://fanyi.baidu.com/langdetect?query='+data
        response = requests.get(url, headers=self.headers, proxies=self.proxy)
        string = response.text
        dic = demjson.decode(string)
        result = str(dic['lan'])
        return result

    def translate(self,data,to='zh'):
        '''
        百度翻译接口，默认日语to中文
        '''
        url = 'http://fanyi.baidu.com/v2transapi?to=' + to + '&query=' + data + '&transtype=translang&simple_means_flag=3'
        response = requests.get(url, headers=self.headers, proxies=self.proxy)
        string = response.text
        dic = demjson.decode(string)
        result = str(dic['trans_result']['data'][0]['dst'])
        return result

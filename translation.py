from baidu import BaiDuAPI
from micsoft import MSAPI


def main(string):
    api = BaiDuAPI()
    baidutrans = api.translate(string)
    api = MSAPI()
    mstrans = api.translate(string)
    return baidutrans,mstrans

if __name__ == '__main__':
    baidutrans, mstrans = main('入荷予定あり')
    print('Baidu translate:%s'%baidutrans)
    print(('Micsoft translate:%s'%mstrans))

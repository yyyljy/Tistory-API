from math import ceil
from os import access
from unittest.result import failfast
import requests
import KEYS
 
class Tistory:
    access_token = KEYS.access_token
    params = {
        'access_token' : access_token
    }

    def __init__(self):
        pass
    
    def getBlogInfo(self):
        getBlogInfoUrl = 'https://www.tistory.com/apis/blog/info?'
        self.params['output'] = 'json'
        res = requests.get(getBlogInfoUrl, params=self.params)
        print(res.json())

    def getCategoryInfo(self, blogName):
        getCateUrl = 'https://www.tistory.com/apis/category/list?'
        self.params['output'] = 'json'
        self.params['blogName'] = blogName
        res = requests.get(getCateUrl, params=self.params)
        print(res.json())

    def chkArticleList(self, blogName, link):
        chkArtiUrl = 'https://www.tistory.com/apis/post/list?'
        self.params['output'] = 'json'
        self.params['blogName'] = blogName
        self.params['page'] = 1
        res = requests.get(chkArtiUrl, params=self.params)
        resJson = res.json()
        pageCnt = int(resJson['tistory']['item']['count'])
        totalCnt = int(resJson['tistory']['item']['totalCount'])

        # 게시글 중복 여부 확인
        if totalCnt == 0:
            pass
        else:
            artiDict = resJson['tistory']['item']['posts']
            repeat = ceil(totalCnt / pageCnt)
            if repeat <= 1:
                pass
            
            elif repeat > 1:
                for i in range(2, repeat+1):
                    self.params['page'] = i
                    res = requests.get(chkArtiUrl, params=self.params)
                    resJson = res.json()
                    artiDict.extend(resJson['tistory']['item']['posts'])
            else:
                return False
            print(artiDict)
            for arti in artiDict:
                if arti['content'] == link:
                    return True
            return False

    def writeBlog(self, blogName, title, content, visibility, category, tag, acceptComment):
        writeBlogUrl = 'https://www.tistory.com/apis/post/write?'
        self.params['output'] = 'json'
        self.params['blogName'] = blogName
        # 필수
        self.params['title'] = title
        # 필수
        self.params['content'] = content
        self.params['visibility'] = visibility
        # 기본값 : 0
        # (0:비공개, 1:보호, 2:발행)
        self.params['category'] = category
        # 기본값 : 0
        # News : 1040605
        self.params['tag'] = tag
        self.params['acceptComment'] = acceptComment
        # 기본값 1
        # 0, 1
        res = requests.post(writeBlogUrl, params=self.params)
        print(res.json())
 
def main():
    ti = Tistory()
    # ti.getAuthCode()
    # ti.getAccessToken()
    # ti.getBlogInfo()
    # ti.getCategoryInfo(blogName='peta')
    # for i in range(20, 26):
    #     ti.writeBlog('peta', 'Test'+str(i), 'This is Test ' + str(i), 1, 1040605, 'cricket,tesing', 0)
    ti.chkArticleList('peta', '/cricket-news/123727/bavuma-to-lead-sa-at-the-world-cup-injured-van-der-dussen-misses-out')
        
if __name__ == '__main__':
    main()
from os import access
import requests
import KEYS
 
class Tistory:
    access_token = KEYS.access_token
    params = {
        "access_token" : access_token
    }

    def __init__(self):
        pass
    
    def getBlogInfo(self):
        getBlogInfoUrl = "https://www.tistory.com/apis/blog/info?"
        self.params["output"] = "json"
        res = requests.get(getBlogInfoUrl, params=self.params)
        print(res.json())

    def getCategoryInfo(self, blogName):
        getCateUrl = "https://www.tistory.com/apis/category/list?"
        self.params["output"] = "json"
        self.params["blogName"] = blogName
        res = requests.get(getCateUrl, params=self.params)
        print(res.json())

    def writeBlog(self, blogName, title, content, visibility, category, tag, acceptComment):
        writeBlogUrl = "https://www.tistory.com/apis/post/write?"
        self.params["output"] = "json"
        self.params["blogName"] = blogName
        # 필수
        self.params["title"] = title
        # 필수
        self.params["content"] = content
        self.params["visibility"] = visibility
        # 기본값 : 0
        # (0:비공개, 1:보호, 2:발행)
        self.params["category"] = category
        # 기본값 : 0
        # CRICKET : 1040605
        self.params["tag"] = tag
        self.params["acceptComment"] = acceptComment
        # 기본값 1
        # 0, 1
        res = requests.post(writeBlogUrl, params=self.params)
        print(res.json())
 
def main():
    ti = Tistory()
    # ti.getAuthCode()
    # ti.getAccessToken()
    # ti.getBlogInfo()
    # ti.getCategoryInfo(blogName="peta")
    ti.writeBlog("peta", "Test3", "This is 3rd Test", 1, 1040605, "cricket,tesing,comment", 0)
    
if __name__ == "__main__":
    main()
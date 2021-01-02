import json
from baidu import baiduPush
from bing import bingPush

class postURL():
    dictSite = None

    def setSite(self,site,targetSpider):
        if targetSpider == "baidu":
            baiduPush.push(self.dictSite[site])
        elif targetSpider == "bing":
            bingPush.push(self.dictSite[site])




    def loadUrl(self):
        dictInfo = None
        with open("siteInfo.Json", "r") as f:
            self.dictSite = json.load(f)
        # print(dictInfo['site1']['url'])


if __name__ == '__main__':
    postURL = postURL()
    postURL.loadUrl()
    targetSpider = ["baidu","bing","google","360","other"]
    siteKey = ["site"+str(gh) for gh in range(1,4)]
    print(siteKey)
    postURL.setSite(siteKey[0],targetSpider[1])

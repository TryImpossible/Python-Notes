#coding=utf-8
# import urllib
# import urllib2
# import re

# url = 'http://www.qiushibaike.com/hot/page/1'
# headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
# try:
#     request = urllib2.Request(url, headers = headers);
#     response = urllib2.urlopen(request);
#     content = response.read().decode('utf-8')   
#     pattern = re.compile('<div class="article block untagged mb15 typs_.*?<h2>(.*?)</h2>.*?content".*?<span>(.*?)</span>.*?', re.S);

#     items = re.findall(pattern,content)

#     print '\n'
#     for item in items:
#         # print('\033[0;34;40m')
#         print item[0]
#         print item[1]
#         print '------------------------------'
   
# except urllib2.URLError, e:
#     if hasattr(e, 'code'):
#         print e.code
#     if hasattr(e, 'reason'):
#         print e.reason


#coding=utf-8
import urllib
import urllib2
import re
import thread
import time

class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self, pageIndex):
        try:
            url = 'http://wwww.qiushibaike.com/hot/page/' + str(pageIndex)
            request = urllib2.Request(url, headers=self.headers)
            reponse = urllib2.urlopen(request)
            pageCode = reponse.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print u'連接糗事百科失敗，錯誤原因', e.reason
                return None

    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print '頁面加載失敗...'
            return None
        pattern = re.compile('<div class="article block untagged mb15 typs_.*?<h2>(.*?)</h2>.*?content".*?<span>(.*?)</span>.*?', re.S);
        items = re.findall(pattern, pageCode)
        pageStories = []
        for item in items:
            pageStories.append(item[0].strip(),item[1].strip())
        return pageStories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1
    
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if (input == 'Q'):
                self.enable = False
                return
            print 
        
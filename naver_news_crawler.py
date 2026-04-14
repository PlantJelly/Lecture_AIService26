import urllib.request
import json
import time

class naver_news_crawler:
    def __init__(self, keyword, start = 1, display = 10):
        self.keyword = keyword
        self.start = start
        self.display = display
    
    def crawlNaverNews(self):
        client_id = "client_id"
        client_secret = "client_secret"
        encText = urllib.parse.quote(self.keyword)
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText
        new_url = url + "&start=" + str(self.start) + "&display=" + str(self.display) # JSON 결과 URL
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과 URL
        request = urllib.request.Request(new_url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            json_data = response_body.decode('utf-8')
            # json 문자열을 파이썬 객체로 변환
            py_data = json.loads(json_data)
            time.sleep(1)
            #print(py_data['items'])
            return py_data
        else:
            print("Error Code:" + rescode)
            return None
    
    def crawl(self):
        resultAll = []
        while self.start < 1000:
            crawled_data = self.crawlNaverNews()
            if crawled_data:
                print('crawling 성공 :', self.start)
                resultAll += crawled_data['items']
                self.start += 10
            else:
                print('crawling 실패 :', self.start)
                break
        print('crawling 완료. 총 진행건수 :', self.start)
        return resultAll

# keyword = '인공지능'
# start = 1
# display = 10

# crawler = naver_news_crawler(keyword, start, display)
# crawled_data = crawler.crawl()
# print(crawled_data[:5])
# print("=======================================================")
# print(crawled_data[-5:])
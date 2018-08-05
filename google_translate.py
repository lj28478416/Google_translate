from selenium import webdriver
import time
class GoogleTranslateSpider():
    def __init__(self):
        self.service_args = []
        self.service_args.append('--load-images=no')  ##关闭图片加载
        self.service_args.append('--disk-cache=yes')  ##开启缓存
        self.service_args.append('--ignore-ssl-errors=true')  ##忽略https错误
        # opt = webdriver.ChromeOptions()
        # opt.set_headless()
        # self.driver = webdriver.Chrome( options=opt,service_args=self.service_args)
        self.driver = webdriver.PhantomJS(service_args=self.service_args)
    def get_index(self):
        self.driver.get('https://translate.google.cn/#auto/en')
        while True:
            str1 = input('请输入要翻译的内容:')
            self.driver.find_element_by_id('source').clear()
            self.driver.find_element_by_id('source').send_keys(str1)
            self.driver.find_element_by_id('gt-submit').click()
            time.sleep(5)
            str2 = self.driver.find_element_by_xpath("//div[@id='gt-res-dir-ctr']/span[2]/span").text
            print(str2)
    def main(self):
        self.get_index()
if __name__ == '__main__':
    google_translate_spider = GoogleTranslateSpider()
    google_translate_spider.main()
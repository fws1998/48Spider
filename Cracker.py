from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from browsermobproxy import Server


def click(id):
    koudaiID.send_keys(str(id))
    getVC.click()


def getImage():
    for entry in result['log']['entries']:
        _url = entry['request']['url']
        return _url


def getColour(image):
    for i in range(0, 190):
        for j in range(20, 130):
            data = image.getpixel((i, j))
            if data[0] == 245 and data[1] == 187 and data[2] == 4:
                print(i, j)
                return i


server = Server(r"D:\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
server.start()
proxy = server.create_proxy()
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server={0}'.format(proxy.proxy))
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
proxy.new_har("my_baidu", options={'captureHeaders': True, 'captureContent': True})

browser = webdriver.Chrome("D:\\chromedriver.exe", options=options)

browser.get("https://live.48.cn/Recharge/")
koudaiID = browser.find_element_by_id("pocket_id")
getVC = browser.find_element_by_id("isright")

click(1)
result = proxy.har

# 根据URL找到数据接口
'''if "/api/v2/aweme/post" in _url:
    _response = entry['response']
    _content = _response['content']['text']'''

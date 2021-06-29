import requests
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from browsermobproxy import Server


def click(id):
    koudaiID.send_keys(str(id))
    getVC.click()


def getImage():
    return result['log']['entries'][15]['request']['url']


def getColour(image):
    for i in range(0, 190):
        for j in range(25, 125):
            data = image.getpixel((i, j))
            if data[0] == 245 and data[1] == 187 and data[2] == 4:
                print(i, j)
                return i


def drag_and_drop(browser, offset):
    print("dad start")
    knob = browser.find_element_by_class_name("slide_block")
    print("found")
    ActionChains(browser).drag_and_drop_by_offset(knob, offset, 0).perform()
    print("dad done")

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'}
server = Server(r"D:\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
server.start()
proxy = server.create_proxy()
options = webdriver.ChromeOptions()
options.add_argument("--auto-open-devtools-for-tabs")
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

re = requests.get(getImage(), headers=headers)
img = Image.open(BytesIO(re.content))
answer = getColour(img)
drag_and_drop(browser, answer)
result = proxy.har

# 根据URL找到数据接口
'''if "/api/v2/aweme/post" in _url:
    _response = entry['response']
    _content = _response['content']['text']'''

import json
from io import BytesIO

import requests
import threading
import PIL
from PIL import Image
from urllib3.packages.six import StringIO



class thread(threading.Thread):
    def __init__(self, a, b):
        threading.Thread.__init__(self)
        self.a = a
        self.b = b

    def run(self):
        headers = {
            'Cookie': '.AspNet.ApplicationCookie=AB93vqCoYrfdCucY_oclJGnRoz1U7RPQX-wafDjLCXV7oBn4DP2Fv2YDxn2N8tBqhWBrH8bhkSp4bnMHhr2SdNL-k0jpAr6dQpMIeBE3_pPLLQtw-pRXUmEMiSbIxy2YC2kiQtW6AieMyYgVKtf2XivK8XFeg6sLnt-wpo_FahiZYur20MKHlYsVX61ZvtSSAPrP6w309jsyAea1wbVI3gjaKVfnMmqCoYQ15PEDFcjma-aIcLbzj6P5FWD-_UBmilx1qDWgzbMjsids4TknNNcHLTL7Xurq7jttDZxnk-KrYZEALco7Nvy_WW8yNBATvRNurKgKahFFLBlBjg0co-jOyQ5aOGxlOxwLJejJUOwAHA-1IZnDZxFxNuzB7xjugxkIYsPyD_kf7ADuet5r6uyDEjEazo70Ktr8PvfJWv8qDXQxWlb8JvMjtz9CtLRd-XHoweJFVr6xx3xtS9gpeWIwdxASv7fKwoeTNBGb1vJm0J45L67wj4TR0LzCVBJaqgpLLpITHgT4uct3KwdxLc2H6yJq7wVpbVC-ewHM5fmIpRLw3nmXY8PLJNjivXTas93Y3K3Qj2Qv9Hp-4-nwHR4qZGfXrEBnxFgFukp1BDHFfg0aVv6wbHPCbHjHS_Q0K48TyKBwsS_7wA_ShxXxNGl3PQQ; PHPSESSID=0drr3d4uuf4cdnvjd2bttg3mp5; Example_auth=bae4I0ZwhQoRXE3ifWBh2lk8wOb1m4N3m%2Fw8eLj%2BwkEB0WRkQ4ON1a7SpX8S1uc0%2F2cYnjUooCTk',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'}
        for c in range(self.a, self.b):
            url = 'https://live.48.cn/Recharge/'
            # print(i)
            re = requests.get(url, headers=headers)
            print(re.content)
            img = Image.open(BytesIO(re.content))

            # 240*150的图片 宽：0-190，高：20-130
            def getColour(image):
                for i in range(0, 190):
                    for j in range(20, 130):
                        data = image.getpixel((i, j))
                        if data[0] == 245 and data[1] == 187 and data[2] == 4:
                            print(i, j)
                            return i
            index = getColour(img)
            print(index)
            url1 = "https://live.48.cn/Slidercode/check?tn_r=" + str(index)
            resp = requests.get(url1, headers)
            print(resp)
            print(resp.text)
            dict = json.loads(resp.text)
            nickname = dict["nickName"]
            if nickname[0:1] == "02":
                print(nickname, )


thread1 = thread(7900000, 7902000)
'''thread2 = thread(7902000, 7904000)
thread3 = thread(7904000, 7906000)
thread4 = thread(7906000, 7908000)
thread5 = thread(7908000, 7910000)
thread6 = thread(7898000, 7900000)
thread7 = thread(7896000, 7898000)'''
thread1.start()
print(1)
'''thread2.start()
print(2)
thread3.start()
print(3)
thread4.start()
print(4)
thread5.start()
thread6.start()
thread7.start()
'''
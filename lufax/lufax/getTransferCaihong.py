import requests

def getUrl(url):
    '''
    get html return json
    '''
    return requests.get(url).json();    
def getToken(setcookie):
    # setcookie='_token="YmNkODlhNmIzZTAwOWU1ODJjNWE1ZWRjM2NmMWIwZTdhZmNmNDkzZDoxODQ0NzEwOjE0MTg2MzU2NTQ4MjY="; Version=1; Domain=.lufax.com; Path=/'
    startQuote = setcookie.find('"');
    endQuote = setcookie.find('"', startQuote + 1)
    # print startQuote,endQuote
    return setcookie[startQuote + 1:endQuote]
token = "MjI0ODA2ZjVkZDljOWZjNzRlOGY5YTBiZjlkMTBkNWJhY2NiN2UyYjo0MzAxNjg2OjE0MTg4MDgzMzUzODU="

def getData():
    global token
    print token
    cookie = ' _g=72c9c4aa-17c2-4922-bbf9-36359558f2dd; _g2=b486480a-0296-4e1c-88a5-c42ee8d8195b; _adwp=39668519.4296646436.1403184311.1403184311.1403184311.1; _adwr=39668519%23http%253A%252F%252Fwww.lufax.com%252Findex.html; _jzqx=1.1403184316.1403184316.1.jzqsr=lufax%2Ecom|jzqct=/index%2Ehtml.-; _jzqa=1.3019665623214980000.1403184316.1403184316.1403184316.1; WT-FPC=id=24b942ee8a55eb920771403184289362:lv=1407377412030:ss=1407377346230; pgv_pvi=4437408768; IMVC=40ab9ec85d7749819881469ffdafc41c; _lufaxSID="40f1fe8a-34ef-4645-9b28-1148de32536b,64vJfoqUwcZgXiJv+DgwfwRfLinitnp6RBFE2Ty1R19DM1p0JYap9DABlIOg2LczEJLlSkqStFlZTL0SxmY4Lw=="; _tn="MzEzMUU5NzE3RDkzNURCQzBEQUVDNTQ3OEUzRUU0QjU="; _tnf=1; Hm_lvt_9842c7dcbbff3109ea37b7407dd0e95c=1417154622,1418611172,1418621907,1418634043; Hm_lpvt_9842c7dcbbff3109ea37b7407dd0e95c=1418634432; __utma=84260612.77761154.1403184289.1418621908.1418634043.32; __utmb=84260612.24.9.1418634471996; __utmc=84260612; __utmz=84260612.1416966720.26.7.utmcsr=my.lufax.com|utmccn=(referral)|utmcmd=referral|utmcct=/my/user-msg; _token="'
    url = '''https://list.lufax.com/list/service/product/fa-transfer-products/listing/1?column=investPeriod&order=asc&isDefault=false'''
    headers = {
               "Host": "list.lufax.com",
"Connection": "keep-alive",
"Cache-Control":" max-age=0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
"Accept-Encoding": "gzip, deflate, sdch",
"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2,ja;q=0.2",
"Cookie":cookie + token + '"'
               
               };
    import time
    headers2 = {
               "Host": "user.lufax.com",
"Connection": "keep-alive",
"Cache-Control":" max-age=0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
"Accept-Encoding": "gzip, deflate, sdch",
"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2,ja;q=0.2",
"Cookie":cookie + token + '"'
               
               };
    # print "https://user.lufax.com/user/keepSession.gif?timestamp=%d" % (int(time.time()) * 1000 + 828)
    r = requests.get("https://user.lufax.com/user/keepSession.gif?timestamp=%d" % (int(time.time() * 1000)), headers=headers2)
    # print r.headers,r.headers["Set-Cookie"]
    token = getToken(r.headers["Set-Cookie"])
    result = requests.get(url, headers=headers).json();       
    
    datas = result["data"];
    for data in datas:
        if data['investPeriod'] < 120  and data['interestRateDisplay'] > 0.071 and (100000 < data['currentPrice'] < 112201.25):
            print data;
            from pushBullet import PushBullet
            print PushBullet('v1lo4nxA7bU6CdzbISMLHnE0SPSIigF9aOujwSGlWwf5U').pushLink(None, str(data['productId']), 'https://list.lufax.com/list/productDetail?productId=%d' % data['productId'])
if __name__ == '__main__':
#     getToken("")
#     getData()
    import time  
    import random  
    for i in range(100000):  
        gap = random.uniform(10, 15) 
        print gap
        getData()
        time.sleep(gap)

import requests
import csv
def getUrl(url):
    '''
    get html return json
    '''
    return requests.get(url).json();    
def run():
    url = '''https://list.lufax.com/list/service/product/transfer-product-list/listing/%d?minAmount=5000&maxAmount=12000&column=currentPrice&tradingMode=00&order=asc&isDefault=false&_=1411530096702'''
    datas = [];
    for pageNum in xrange(1, 1000):
        result = getUrl(url % pageNum);
        print pageNum, result

        datas.extend(result['data']);
        if result['nextPage'] == pageNum:
            break;
    # print datas;
    datas = sorted(datas, key=lambda line:line['reducePriceDays']*-1)
    with open('test.csv', 'wb+') as f:
        print datas[0].keys()
        fieldnames=datas[0].keys()
        fieldnames.extend(['investSource','bidCurrentPrice']);
        dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(datas)
if __name__ == '__main__':
    #run();
    from pushBullet import PushBullet

    print PushBullet('v1lo4nxA7bU6CdzbISMLHnE0SPSIigF9aOujwSGlWwf5U').pushNote(None, 'test', 'test')
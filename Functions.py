import bs4
from urllib import request

def get_numbers():
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='
    fileWrite = open('numbers.txt', 'w')
    cnt = 1
    
    while True:
        targetUrl = url + str(cnt)

        target = request.urlopen(targetUrl)
        soup = str(bs4.BeautifulSoup(target,'html.parser'))

        if soup == "{\"returnValue\":\"fail\"}":
            break
        
        nums = {}

        nums[0] = soup.split("\"drwtNo1\":")[1].split("}")[0] + " "
        nums[1] = soup.split("\"drwtNo2\":")[1].split(",")[0] + " "
        nums[2] = soup.split("\"drwtNo3\":")[1].split(",")[0] + " "
        nums[3] = soup.split("\"drwtNo4\":")[1].split(",")[0] + " "
        nums[4] = soup.split("\"drwtNo5\":")[1].split(",")[0] + " "
        nums[5] = soup.split("\"drwtNo6\":")[1].split(",")[0] + " "
        nums[6] = soup.split("\"bnusNo\":")[1].split(",")[0] + " "

        for i in range(0, 7):
            fileWrite.write(nums[i])

        fileWrite.write("\n")
        cnt += 1


get_numbers()
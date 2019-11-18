from bs4 import BeautifulSoup
import requests

# 首先我们输入目标网址

_url = 'https://liansai.500.com/zuqiu-5283/teams/'

# 第一步，我们先用request获取页面的html代码
html_content = requests.get(_url, 'html.parser')
soup_content = BeautifulSoup(html_content.text, features="lxml")
team_container = soup_content.find('tbody').find_all('tr')

# 循环整个列表，获取有用信息组合成一个dict
save_data = {}
for i in team_container:
    team_id = i.find('a').attrs['href'].split(
        'http://liansai.500.com/team/')[1][:-1]
    team_name = i.find('a').text
    save_data[team_id] = team_name

print(save_data)
# print(team_container)

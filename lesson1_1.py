import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
a = requests.get(
    'https://www.zhihu.com/api/v4/search/preset_words?w=', headers=headers).text
print(a)

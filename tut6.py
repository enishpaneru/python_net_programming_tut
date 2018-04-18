import urllib.parse
import urllib.request

data = {'q': 'enish'}
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')
headers = {}
headers[
    'User-Agent'] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
req = urllib.request.Request("https://pythonprogramming.net/search", data=data)
print(req.get_method())
u1 = urllib.request.urlopen(req)
data = u1.read()
print(data)

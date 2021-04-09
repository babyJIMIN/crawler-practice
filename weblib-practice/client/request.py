from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET
http_response = urlopen('https://www.example.com')
body = http_response.read()
body = body.decode('utf-8')
print(body)

print("==================================================================================================")

# POST
data = {
    'id': 'test',
    'name': '이지민',
    'pw': '1234'
}
data = urlencode(data).encode('utf-8')

request = Request('https://www.example.com', data)
request.add_header('Content-Type', 'text/html')

http_reponse = urlopen(request)
print(http_reponse.status, http_reponse.reason)

body = http_response.read()
html = body.decode("utf-8")
print(html)

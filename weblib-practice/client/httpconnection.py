from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')

conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason)

# 성공
# GET / HTTP / 1.1
# 200 OK
if resp.status == 200:
    body = resp.read()
    print(type(body), body)

# 실패
# GET / hello.html HTTP / 1.1
# 404 Not Found
conn.request('GET', '/hello.html')
resp = conn.getresponse
print(resp.status, resp.reason)
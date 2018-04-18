import urllib.request

fields = {
'txtUsername' : 'dave',
'txtPassword' : '12345',
'submit_login' : 'Log In'
}
opener = urllib.request.build_opener(
urllib.request.HTTPCookieProcessor()
)
request = urllib.request.Request(
"http://somedomain.com/login.asp",
urllib.urlencode(fields))
# Login
u = opener.open(request)
resp = u.read()
# Get a page, but use cookies returned by initial login
u = opener.open("http://somedomain.com/private.asp")
resp = u.read()
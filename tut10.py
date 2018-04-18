# for csv files
# import csv
# f=open("sample.csv",'r')
# for each in csv.reader(f):
#     print(each)

# for parsing html
# from html.parser import HTMLParser
# class MyParser(HTMLParser):
#     def __init__(self):
#         HTMLParser.__init__(self)
#         self.links = []
#
#     def handle_starttag(self, tag, attrs):
#         if tag == 'a':
#             for name, value in attrs:
#                 if name == 'href':
#                     self.links.append(value)
#     def handle_data(self,data):
#         pass
#     def handle_endtag(self,tag):
#         pass
#
# # Fetch a web page
# import urllib.request
# u = urllib.request.urlopen("http://www.python.org")
# data = u.read()
# print(data)
# # Run it through the parser
# p = MyParser()
# p.feed(str(data))
#
# for x in p.links:
#     print(x)

# xml parsing
import xml.sax
class MyHandler(xml.sax.ContentHandler):
    def startDocument(self):
        print ("Document start")
    def startElement(self,name,attrs):
        print ("Start:", name)
    def characters(self,text):
        print ("Characters:", text)
    def endElement(self,name):
        print("End:", name)

# Create the handler object
hand = MyHandler()
# Parse a document using the handler
xml.sax.parse("data.xml",hand)
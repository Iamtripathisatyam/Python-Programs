import pyshorteners
url=input("Enter URL: ")
print(pyshorteners.Shortener().tinyurl.short(url))
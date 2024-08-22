clearText = "abc"
charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
encText = "".join([charSet[(charSet.find(c)+3)%95] for c in clearText])
print(encText)

encText = "".join([charSet[(charSet.find(c)-3)%95] for c in encText])
print(encText)

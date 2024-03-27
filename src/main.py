from textnode import TextNode


print("hello world")
tn = TextNode("This is a text node", "bold", "https://www.pornhub.com")
tn2 = TextNode("This is a text node", "italic", "https://www.pornhub.com")
print(tn)
print(tn == tn2)
import requests 
image = requests.get ("https://img.icons8.com/ios/50/ffffff/python.png")
with open("new_image.png", 'wb') as f:
    f.write(image.content)
    
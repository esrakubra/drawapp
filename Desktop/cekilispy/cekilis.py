from selenium import webdriver

import time

ytLiveChatURL = 'html/wwww.youtube.com/live_chat?v=mxTiT2igK7A'


# start web browser
browser=webdriver.Firefox()

# get source code
browser.get(ytLiveChatURL)
html = browser.page_source
time.sleep(2)
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
messages = soup.find_all('yt-live-chat-text-message-render')

for message in messages:
    content =message.find_all('div',{'id':content})

print(message)


# close web browser
browser.close()
import requests # Send network request and return response data (API) HTTP library
import re # A module for processing regular expression
from bs4 import BeautifulSoup # A web parsing library

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'}

# Get the video name and author
url = 'https://www.bilibili.com/video/BV1hv41167AZ?from=search&seid=2994033640821292376'
response = requests.get(url, headers)
response.encoding = 'utf-8'
page_text = response.text
soup = BeautifulSoup(page_text, 'lxml')
video_title = soup.find('span', class_='tit tr-fix').text
print('Video name：' + video_title)
uploader = soup.find('a', attrs={'report-id': 'name'}).text.strip()
print('Author：' + uploader)

# Get the barrage file
cid = '203530835'
xml = 'https://api.bilibili.com/x/v1/dm/list.so?oid={}'.format(cid)
response = requests.get(xml, headers)
response.encoding = 'utf-8'
xml_text = response.text
soup = BeautifulSoup(xml_text, 'lxml')
barrages = [re.sub(r'\s+', '', bar.text) for bar in soup.find_all('d')]

# Get the number of barrage
print('Number of barrage：' + str(len(barrages)))

# Write barrage to file
with open('./barrage.txt', 'w', encoding='utf-8') as output_file:
    for bar in barrages:
        output_file.write(bar + '\n')
print('Barrage information has been successfully written to the file！')

import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud # Wordcloud is a word cloud display library
from PIL import Image # A library of pictures that can be edited
import numpy as np # Numpy is an extension library of the python language

font = r'C:\Windows\Fonts\STXINWEI.TTF'

text = (open('C:/Users/Qnet/PycharmProjects/Project-2/barrage.txt', 'r', encoding='utf-8')).read()
cut = jieba.cut(text)  # Break down words
string = ' '.join(cut)
print(len(string))
img = Image.open('D:/Users/Qnet/Downloads/bingqilin.png')  # Open the background image
img_array = np.array(img)  # Convert picture to array
wc = WordCloud(
    background_color='white',
    width=400,
    height=711,
    mask=img_array,
    font_path=font,
    max_font_size = 150,
    min_font_size = 1,
    )
wc.generate_from_text(string)  # Draw a picture
plt.imshow(wc)
plt.axis('off')
plt.show()  # Show picture
wc.to_file('bingqilin_1.png')  # Save picture
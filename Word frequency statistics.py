import matplotlib.pyplot as plt # Matplotlib is mainly for data visualization charts
import jieba
from pylab import mpl # Pylab imports all functional functions into its separate namespace

# Solve the problem of failure to display Chinese in the matplotlib box
mpl.rcParams['font.sans-serif'] = ['SimHei']

with open('C:/Users/Qnet/PycharmProjects/Project-2/barrage.txt', 'r', encoding="utf-8") as f:
    contents = f.read()
words = jieba.lcut(contents)
# The number of occurrences of the stored number of times
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1


items = list(counts.items())
# Sort the words and extract the first 11 words
items.sort(key=lambda x: x[1], reverse=True)
names, dicts = [], []
for i in range(11):
    word, count = items[i]
    txt = "{0:<5}{1:>5}".format(word, count)
    names.append(word)
    dicts.append(count)

# Use matplotlib to draw and display
plt.figure()
plt.plot(names,dicts)
plt.xlabel('Top 11 words')
plt.ylabel('Word frequency')
plt.title("Top 11 words in barrage.txt")
plt.show()

import jieba

text = open("C:/Users/Qnet/PycharmProjects/Project-2/barrage.txt", "r", encoding='utf-8').read()
names = {'周震南','何洛洛','焉栩嘉','夏之光','姚琛','翟潇闻','张颜齐','刘也','任豪','赵磊','赵让'}
words  = jieba.lcut(text)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "南南":
        rword = "周震南"
    elif word == "洛洛":
        rword = "何洛洛"
    elif word == "嘉嘉":
        rword = "焉徐嘉"
    elif word == "光光":
        rword = "夏之光"
    elif word == "琛哥":
        rword = "姚琛"
    elif word == "小翟":
        rword = "翟潇闻"
    elif word == "齐齐":
        rword = "张颜齐"
    elif word == "也哥":
        rword = "刘也"
    elif word == "豪总":
        rword = "任豪"
    elif word == "磊磊":
        rword = "赵磊"
    elif word == "让让":
        rword = "赵让"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
# for word in excludes:
#     del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(40):
    word, count = items[i]
    if word in names:
        print ("{0:<10}{1:>5}".format(word, count))
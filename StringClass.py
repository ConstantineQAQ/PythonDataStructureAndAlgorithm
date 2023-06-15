import re
import docx


#朴素字符串匹配算法返回所有符合条件的字符串的起始位置
def naive(s, p)->list:
    i = 0
    j = 0
    pos = []
    while i < len(s) and j < len(p):
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
        if j == len(p):
            pos.append(i - len(p))
            j = 0
    return pos
    
    
#kmp算法返回所有符合条件的字符串的起始位置
def kmp(s, p)->list:
    i = 0
    j = 0
    pos = []
    next = getNext(p)
    while i < len(s) and j < len(p):
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next[j]
        if j == len(p):
            pos.append(i - len(p))
            j = 0
    return pos

#kmp算法的next数组
def getNext(p)->list:
    next = [-1] * len(p)
    i = 0
    j = -1
    while i < len(p) - 1:
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next

    
def getStringInDocx()->str:
    doc = docx.Document('test.docx')
    text = ''
    for para in doc.paragraphs:
        text += para.text
    return text


#利用正则表达式查找文档中的中文AABB形式的字符串和AABB整个字符串
def findChinese():
    text = getStringInDocx()
    pattern = re.compile(r'[\u4e00-\u9fa5]{2,}')
    print("文档中的中文AABB形式的字符串:{}".format(pattern.findall(text)))

#利用正则表达式查找字符串中符合标准的IP地址
def findIP():
    text = getStringInDocx()
    pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    print("文档中的IP地址:{}".format(pattern.findall(text)))


#利用正则表达式查找字符串中的符合标准的qq电子邮箱地址
def findEmail():
    text = getStringInDocx()
    pattern = re.compile(r'[1-9]\d{4,10}@qq\.com')
    print("文档中的qq邮箱地址:{}".format(pattern.findall(text)))

#利用正则表达式查找字符串中的符合标准的身份证号码
def findID():
    text = getStringInDocx()
    pattern = re.compile(r'\d{17}[\dXx]')
    print("文档中的身份证号码:{}".format(pattern.findall(text)))

#利用正则表达式查找字符串中的符合标准的url地址
def findURL():
    text = getStringInDocx()
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    print("文档中的url地址:{}".format(pattern.findall(text)))

#利用正则表达式过滤字符串中的html标签
def filterHTML():
    text = getStringInDocx()
    pattern = re.compile(r'<[^>]+>', re.S)
    print("过滤后的文档:{}".format(pattern.sub('', text)))

    #利用正则表达式查找字符串中的城市的带区号电话号码
def findPhone():
    text = getStringInDocx()
    pattern = re.compile(r'0\d{2}-\d{8}|0\d{3}-\d{7,8}}')
    print("文档中的电话号码:{}".format(pattern.findall(text)))



""" s = "abcabeabcabcmn"
p = "abc"
print("朴素字符串匹配算法:{}".format(naive(s, p)))
print("next数组:{}".format(getNext(p)))
print("kmp算法:{}".format(kmp(s, p)))  """


print("文档中的字符串:{}".format(getStringInDocx()))
print()
findIP()
print()
findEmail()
print()
findID()
print()
findURL()
print()
filterHTML()
print()
findPhone()
print()
findChinese()   
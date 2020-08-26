
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import time
import json
import datecaculate

#以Chrome作為Selenium開啟的瀏覽器
web = webdriver.Chrome()

#進入數位新報-資訊安全分類的網站
web.get("https://www.bnext.com.tw/categories/ai")

#存放所有爬取資料
TotalData=[]

#將網頁轉成HTML形式
html = web.page_source
soup=BeautifulSoup(html,'html.parser')




date_list=[]
date_list=datecaculate.GetDaysList()  #獲取日期資料
try:
    alldiv = soup.find_all('div',class_='item_box item_sty01 div_tab')
    for div in alldiv:
        print('----一篇新聞開始----')
        try:
            date=div.find('div',class_='div_td td1').text.strip()  #爬取新聞標題 
            if ('ago' in date):
                date=datecaculate.GetToday()
            else:
                date=datecaculate.StringToDate(date,'%Y-%m-%d').date() #爬取新聞發布時間
        except:
                print('時間爬取失敗')
        try:
            content=div.find('div',class_='item_summary').text.strip()  #爬取新聞內文
        except:
            print('內文爬取失敗')
        try:     
            link=div.find('a',class_='item_img bg_img_sty01').get('href') #爬取新聞連結
        except:
            print("連結爬取失敗")
        try:
            
            title=div.find('h2').text.strip()   
        except:
            print("標題爬取失敗")  


        #判斷新聞日期是否在指定範圍內
        if(date in date_list):
            date=datecaculate.DateToString(date)
            print('#標題:{} \n#內文：{} \n#發文日期：{}\n#連結：{}'.format(title, content,date, link))
            TotalData.append({'title':title,'content':content,'date':date,'link':link})
            print("TotalData儲存成功")
        else:
            print("超出日期範圍不紀錄")
            
               #########################################################################################     
        print('----一篇新聞結束---- ')
    print('---------爬蟲結束------- ')  
    web.close()
except:
    print('---------Bnext_News網站內容更新，爬蟲爬取失敗，請檢查------- ')  
    web.close()

print(TotalData)

with open(r'JSON\Bnext_News.json', 'w', encoding='utf-8') as f:
    json.dump(TotalData, f,ensure_ascii=False,indent=2)

def excel_:
    if cells('1','b')>    


from datetime import datetime
import datecaculate
from selenium import webdriver
from bs4 import BeautifulSoup
import json

chrome_path='C:\\Python38-32\\chromedriver.exe'
web = webdriver.Chrome(chrome_path)

web.get("https://www.ithome.com.tw/tags/資安周報")
TotalData=[]
# num_page = int(input("需要爬取的頁數 : "))

# while num_page > 0:
c_url = web.current_url
web.get(c_url)
html = web.page_source
soup=BeautifulSoup(html,'html.parser')
print('----開始進行爬蟲----')
try:
    alldiv = soup.find('div',class_='view-content')
    for div in alldiv:
        print('----一篇新聞開始----')
        if 'NavigableString' in type(div).__name__:
            print('此DIV無內容')
        else:
            try:
                title=div.find('p',class_='title').text   
                try:
                    content=div.find('div',class_='summary').text.strip()
                except:
                    print('內文爬取失敗')
                try:     
                    link='https://www.ithome.com.tw/'+div.find('a').get('href')
                except:
                    print("連結爬取失敗")
                try:
                    date=div.find('p',class_='post-at').text.strip()
                    date=datecaculate.StringToString(date,'%Y-%m-%d')#把原始網站的2000-00-00換成2000.00.00格式的字串
                    
                    
                except:
                        print("日期爬取失敗")
                
                try:
                    newdate=datecaculate.StringToDate(date,'%Y.%m.%d').date()#.date()為的是把Date格式跟陣列的統一才能比對
                    datelist=datecaculate.GetDaysList()
                except:
                        print("日期處理失敗")
                if newdate in datelist:

                    print('#標題:{} \n#內文：{} \n#發文日期：{}\n#連結：{}'.format(title, content,date, link))
                    TotalData.append({'title':title,'content':content,'date':date,'link':link})
                    print("TotalData儲存成功")
                else:
                    print("日期之外不存入")

            except:
                print("標題擷取失敗")
            #########################################################################################     


            # print(div)

        print(' ----一篇新聞結束---- ')
        # web.find_element_by_link_text('下一頁 ›').click()
        # num_page = num_page-1
    
    print(' ---------爬蟲結束------- ')  
    web.close()
except:
    print('-------------爬取失敗，iThome新聞更新，請檢查--------------')
    web.close()
    




print(TotalData)

with open(r'JSON\iThome_News.json', 'w', encoding='utf-8') as f:
    json.dump(TotalData, f,ensure_ascii=False,indent=2)

##寫檔



input_file = open (r'JSON\iThome_News.json',encoding = 'utf8')
json_array = json.load(input_file)
print(json_array[0]['content'])
print(len(json_array[0]['content']))
##讀檔








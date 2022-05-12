import smtplib
import ssl
from bs4 import BeautifulSoup
from lxml import etree
from numpy.core.fromnumeric import trace
import requests
import time
import lxml
import datetime
import lxml
import threading
import numpy as np
import pandas_datareader as web
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense,Dropout,LSTM
from tensorflow.keras.models import Sequential
from lxml import etree
import pandas as pd

from email.message import EmailMessage
import asyncio
from urllib.request import Request, urlopen
from urllib.request import urlparse as urljoin
from bs4 import BeautifulSoup
from bs4.element import Comment 
from bs4 import BeautifulSoup as bs
import lxml
from datetime import datetime
import socket
future_day=2
gettingdaysforpred=requests.get('https://www.calendardate.com/todays.htm').text
gettingdaysforpred=BeautifulSoup(gettingdaysforpred,'lxml')
gettingdaysforpred=gettingdaysforpred.find_all('td', colspan="9", align="CENTER")
gettingdaysforpred=gettingdaysforpred[0]
gettingdaysforpred=str(gettingdaysforpred)
gettingdaysforpred=gettingdaysforpred.replace('<td align="CENTER" colspan="9">','').replace('2022</td>','')
weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','Monday']
months=['January','February','March','April','May','June','July','August','September','October','November','December']
cryp="Cardano"
csubject="CRYPTO STOCK INFO (Cardano)"
myemail="cryptobot693@gmail.com"
recvemail="clivethompson09@gmail.com"
password="CLIVE10GWEN"
#def tag_visible(element):
import threading
#     if element.parent.name in [
#             'style', 'script', 'head', 'meta', "[document]"
#     ]:
#         return False
#     if isinstance(element, Comment):
#         return False
#     return True
# def GetText(soup):
#     texts = soup.findAll(text=True)
#     visible_texts = filter(tag_visible, texts)
#     return u" ".join(t.strip() for t in visible_texts)
# def getData(url):
#     try:
#         req = Request(url, headers={"Identity": "Epic Web Crawler"})
#     except Exception as e:
#         print("Something went wrong with", url, e)
#         return False
#     trys = 0
#     while trys < 10:
#         try:
#             responce = urlopen(req)
#             break
#         except:
#             trys += 1
#     if trys > 10:
#         print("The webpage won't work")
#         return False
#     try:
#         f = str(responce.read().decode())
#     except:
#         return False
#     content_type = responce.headers.get('Content-Type').lower()
#     if "html" not in content_type:
#         print(f"{url} is not an html page")
#         return False#     return f
# def getTitle(soup):
#     try:
#         title = str(soup.title.string)
#     except:
#         title = "none"
#     return title
# def getFavicon(soup, site):
#     icon_link = soup.find("link", rel="shortcut icon")
#     if icon_link is None:
#         icon_link = soup.find("link", rel="icon")
#     if icon_link is None:
#         return urljoin(site, '/favicon.ico')
#     favicon = urljoin(site, icon_link["href"])
#     return favicon
# already_found = open("links.txt").read().split("\n")
# def crawl(starturl):
#     global already_found
#     content = getData(starturl)
#     if content == False:
#         return
#     soup = bs(content, features="html5lib")
#     title = getTitle(soup)
#     text = GetText(soup)
#     favicon = getFavicon(soup, starturl)
#     links = [
#         urljoin(starturl, link.get("href")) for link in soup.find_all('a')
#         if urljoin(starturl, link.get("href")) not in already_found
#     ]
#     already_found += links
#     links_text = '\n'.join(links)
#     print(
#         f"URL: {starturl}\nTitle: {title}\nFavicon: {favicon}\nLinks: {links_text}"
#     )
#     open("links.txt", "a").write(links_text)
#     for link in links:
#         try:
#             crawl(link)
#         except:
#             print("excepted the problem")

tr=requests.get("https://www.coingecko.com").text
print(tr)
import lxml
tr=BeautifulSoup(tr,"lxml")
tr=tr.find_all("a", class_="d-lg-none font-bold tw-w-12")
print(tr)
tr=list(tr)
print(tr)
comparevals=[]
findvals={}
cryptonameslist=[]
allsfincrypt=[]
def price_pred(crypto_name,crypto_currnecy,*args):
    def main():
        global predictionlist
        predictionlist=[]
        global arg
        arg=args
        allsfincrypt.append(crypto_name.replace('-','_'))
        global outside_crypto_name
        outside_crypto_name=crypto_name
        cpage=requests.get(f'https://www.coingecko.com/en/coins/{crypto_name}/eur').text
        csoup=BeautifulSoup(cpage,"lxml")
        global cres
        cres=csoup.find_all('span', class_="no-wrap")
        cplusressuop=BeautifulSoup(cpage,"html.parser")
        dom=etree.HTML(str(cplusressuop))
        against_currency='EUR'
        ne=False
        try:
            data=web.DataReader(f'{crypto_currnecy}-{against_currency}',data_source='yahoo')
        except:
            try:
                data=web.DataReader(f'{crypto_currnecy}-USD',data_source='yahoo')
                ne=True
            except:
                try:
                    data=web.DataReader(f'{crypto_currnecy}-USD',"yahoo")
                    nes=True
                except:
                  pass
        for line in args:      
            scaler=MinMaxScaler(feature_range=(0,1))
            scaled_data=scaler.fit_transform(data['Close'].values.reshape(-1,1))
            prediction_days=60
            x_train,y_train=[],[]
            for x in range(prediction_days,len(scaled_data)-line):
                x_train.append(scaled_data[x-prediction_days:x,0])
                y_train.append(scaled_data[x+line,0])
            x_train,y_train=np.array(x_train),np.array(y_train)
            x_train=np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
            model=Sequential()
            model.add(LSTM(units=50,return_sequences=True,input_shape=(x_train.shape[1],1)))
            model.add(Dropout(0.2))
            model.add(LSTM(units=50,return_sequences=True))
            model.add(Dropout(0.2))
            model.add(LSTM(units=50))
            model.add(Dense(units=1))
            model.compile(optimizer='adam',loss='mean_squared_error')
            model.fit(x_train,y_train,epochs=50,batch_size=32)
            if ne:
                test_data=web.DataReader(f'{crypto_currnecy}-USD',data_source='yahoo')
            elif nes:
                test_data=web.DataReader(f'{crypto_currnecy}-USD','yahoo')
            else:
                test_data=web.DataReader(f'{crypto_currnecy}-{against_currency}',data_source='yahoo')
            actual_prices=test_data['Close'].values
            total_dataset=pd.concat((data['Close'],test_data['Close']),axis=0)
            model_inputs=total_dataset[len(total_dataset)-len(test_data) -prediction_days:].values
            model_inputs=model_inputs.reshape(-1,1)
            model_inputs=scaler.fit_transform(model_inputs)
            x_test=[]
            for x in range(prediction_days,len(model_inputs)):
                x_test.append(model_inputs[x-prediction_days:x,0])
            x_test=np.array(x_test)
            x_test=np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))
            prediction_prices=model.predict(x_test)
            prediction_prices=scaler.inverse_transform(prediction_prices)
            #threading.Thread(target=plt.show()).start()
            real_data = [model_inputs[len(model_inputs) - prediction_days : len(model_inputs)+1, 0]]
            real_data=np.array(real_data)
            real_data=np.reshape(real_data,(real_data.shape[0],real_data.shape[1],1))
            prediction=model.predict(real_data)
            prediction=scaler.inverse_transform(prediction)
            prediction=str(prediction)
            prediction=prediction.replace('[[','')
            prediction=prediction.replace(']]','')
            cryptonameslist.append(crypto_name)
            print(cres[0].text)
            global crypt_name
            crypt_name=crypto_name.replace("-","_")
            r=f"global {crypt_name}_compred"
            print(r)
            exec(r)
            print('EXECUTED')
            x=f"global {crypt_name}_compred"
            exec(x)
            print("---------------------------")
            print(prediction)
            print({cres[0].text[1:]})
            print("---------------------------")
            exeuteablecompare=f"{crypt_name}_compred=float({cres[0].text[1:]})-float({prediction})"
            exec(exeuteablecompare)
            exeuteablecompare=f"print({crypt_name}_compred)"
            exec(exeuteablecompare)
            exeuteablecompare=f"comparevals.append({crypt_name}_compred)"
            exec(exeuteablecompare)
            if line==args[0]:
                exeuteablecompare=f"{crypt_name}_list=[]"
                exec(exeuteablecompare)
            exeuteablecompare=f"{crypt_name}_list.append({crypt_name}_compred)"
            exec(exeuteablecompare)
            cryptss_name=crypt_name.replace("_"," ")
            if line==args[::-1][0]:
                global cbody
                Ys=crypt_name+"cbody"
                x=f'{Ys}="{cryptss_name} price: {cres[0].text}(24h)"'
                exec(x)
                for lines in range(len(predictionlist)):
                    x=f'{Ys}={crypt_name}_cbody+f"{arg[lines]} days (predicted) price:  {predictionlist[lines]}\n'
                    exec(x)
            if ne:
                wwwd=requests.get("https://www.x-rates.com/?form=USD&amount={prediction}").text
                wwwd=BeautifulSoup(wwwd,'lxml')
                rdq=wwwd.find_all("tr")
                prediction=str(rdq[1])
                prediction=prediction.split("\n")
                prediction=prediction[2].split(">")
                prediction=prediction[2].replace("</a")
                prediction=float(prediction[0])

            predictionlist.append(prediction)
            month = datetime.now().month     

    return main

for line in range(len(tr)):
    #print(tr)
    ere=f'e{line}_trplace=str(tr[{line}]).replace("[","").replace("]","").split("href=")'
    exec(ere)
    ewae=f"print(e{line}_trplace)"
    exec(ewae)
    x=f"x=e{line}_trplace[1]"
    #print(x)
    exec(x)
    #print(x)
    x=x.replace('"','')
    x=x.split(">")
    x=x[0]
    x=x.split("/")
    ere=f'e{line}_trplace=x'
    exec(ere)
    ere=f'e{line}_trplace=e{line}_trplace[3]'
    exec(ere)
    ere=f"e{line}_4lettercode=str(tr[{line}]).split('>')"
    exec(ere)
    ere=f"e{line}_4lettercode=e{line}_4lettercode[1]"
    exec(ere)
    x=f"x=str(e{line}_4lettercode)"
    exec(x)
    x=x.replace("\n","").replace("</a","")
    ere=f"e{line}_4lettercode=x"
    exec(ere)
    ere=f"yx=e{line}_trplace"
    exec(ere)
    s=price_pred(yx,x,30)
    s()
    print("i")
#sandp=price_pred("sandp","^GSPC")
try:
    num1=min(comparevals)
    print(num1)
    print(comparevals)
    comwda=comparevals.remove(num1)
    num2=min(comparevals)
    comwda=comwda.remove(num2)
    num3=min(comparevals)
    comwda=comwda.remove(num3)
    num4=min(comparevals)
    comwda=comwda.remove(num4)
    num5=min(comparevals)
    comwda=comwda.remove(num5)
except Exception as e:
    print(e)

def find_val(crypt_names):
    x=f'crypt_names_compred={crypt_names}_list'
    exec(x)
    for line in range(len(crypt_names_compred)):
        if crypt_names_compred[line]==num1 or num2 or num3 or num4 or num5:
            message=EmailMessage()
            csubject=f"CRYPTO STOCK INFO ({crypt_names})"
            message["From"]=myemail
            message["To"]=recvemail
            message["subject"]=csubject
            x=f"message.set_content({crypt_names}cbody)"
            exec(x)
            context=ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
                 server.login(myemail,password)
                 server.sendmail(myemail,recvemail,message.as_string())
        break

print("END")
for crypto_name in allsfincrypt:
    find_val(crypt_name)

# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import logging
logging.basicConfig(filename ='app.log',
                        level = logging.INFO)

from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=2)

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json
from stock_analysis import analyse_stock
from stock_price import stock_price_info
from daily_quotes import *

#manage threads here
stock_price_info_p = pool.apply_async(stock_price_info)
daily_q_p = pool.apply_async(daily_q)
pool.close()
pool.join()



#put all the functions in here
#stock details
#stock_price_info()
stock_list = ["TATACONSUM","BERGEPAINT","COALINDIA"]
f = open('stocks_info')
data = json.load(f)
f.close()

#daily quotes
quotes = daily_q_p.get()
quote = quotes[0]['q']
author = quotes[0]['a']
print("{} - {}".format(quote,author))

#functions to send mails comes here dont add any functions other than mail related here
fromaddr = "aiarjun027@gmail.com"
toaddr = "arjunprakash027@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "DAILY DIGEST"

#for daily quotes
body_quote = "\n--------------------\nDAILY QUOTE OF THE DAY\n\n{}\n\n-{}".format(quote,author)
msg.attach(MIMEText(body_quote, 'plain'))

#for stocks
for i in range(len(stock_list)):
    name = data['Stock_details'][str(i)]['Name']
    price = data['Stock_details'][str(i)]['price']
    fifty_ma = data['Stock_details'][str(i)]['50 days ma']
    twohundred_ma = data['Stock_details'][str(i)]['200 days ma']
    growth = analyse_stock(name)
    body = "\n--------------------\nName:{}\nprice:{}\n50DaysMA:{}\n200DaysMA:{}\nGrowth:{}".format(name,price,fifty_ma,twohundred_ma,growth)
    msg.attach(MIMEText(body, 'plain'))



s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "uenjjpiikiferigy")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()
os.remove("stocks_info")

#residue function comes here
# for stock in stock_list:
# # open the file to be sent
#     # filename = "{}.png".format(stock)
#     # attachment = open("{}.png".format(stock), "rb")

#     # instance of MIMEBase and named as p
#     p = MIMEBase('application', 'octet-stream')

#     # To change the payload into encoded form
#     # p.set_payload((attachment).read())

#     # encode into base64
#     encoders.encode_base64(p)

#     # p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

#     # attach the instance 'p' to instance 'msg'
#     msg.attach(p)

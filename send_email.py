# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json
from stock_analysis import analyse_stock
from stock_price import stock_price_info

stock_price_info()
stock_list = ["TATACONSUM","BERGEPAINT","COALINDIA"]

f = open('stocks_info')
data = json.load(f)

fromaddr = "aiarjun027@gmail.com"
toaddr = "arjunprakash027@gmail.com"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "DAILY DIGEST"

for i in range(len(stock_list)):
    name = data['Stock_details'][str(i)]['Name']
    price = data['Stock_details'][str(i)]['price']
    fifty_ma = data['Stock_details'][str(i)]['50 days ma']
    twohundred_ma = data['Stock_details'][str(i)]['200 days ma']
    growth = analyse_stock(name)
# string to store the body of the mail
    body = "\n--------------------\nName:{}\nprice:{}\n50DaysMA:{}\n200DaysMA:{}\nGrowth:{}".format(name,price,fifty_ma,twohundred_ma,growth)

# attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))


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

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "uenjjpiikiferigy")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()

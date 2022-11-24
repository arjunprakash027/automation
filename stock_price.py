from yahoofinancials import YahooFinancials 
import pandas as pd
import numpy as np
from datetime import date,timedelta
import matplotlib.pyplot as plt
import json
import logging
logging.basicConfig(filename ='app.log',
                        level = logging.INFO)

def stock_price_info():
	today = date.today()
	period = timedelta(days=90)
	three_mnths = today - period

	stock_list = ["TATACONSUM","BERGEPAINT","COALINDIA"]
	dicti = {}
	dicti['Stock_details'] = {}

	for i in range(len(stock_list)):
		dicti['Stock_details'][i] = {}
		yahoo_financials = YahooFinancials('{}.NS'.format(stock_list[i]))
		data = yahoo_financials.get_historical_price_data(start_date=str(three_mnths), 
													end_date=str(today), 
													time_interval='daily')

		# df = pd.DataFrame(data['{}.NS'.format(stock_list[i])]['prices'])
		# df = df.drop('date', axis=1).set_index('formatted_date')


		# df['SMA20'] = df['close'].rolling(20).mean()
		# df['SMA10'] = df['close'].rolling(10).mean()
		# df[['close', 'SMA20','SMA10']].plot(label='{}'.format(stock_list[i]),
		#                               figsize=(16, 8))
		# plt.title(stock_list[i])
		# plt.savefig("{}.png".format(stock_list[i]))

		price =  yahoo_financials.get_current_price()
		fifty_ma = yahoo_financials.get_50day_moving_avg()
		twohundred_ma = yahoo_financials.get_200day_moving_avg()
		dicti['Stock_details'][i]["Name"] = stock_list[i]
		dicti['Stock_details'][i]['price'] = price
		dicti['Stock_details'][i]['50 days ma'] = fifty_ma
		dicti['Stock_details'][i]['200 days ma'] = twohundred_ma
		json_object = json.dumps(dicti, indent = 4)
		with open("stocks_info", "w") as outfile:
			outfile.write(json_object)
		logging.info("stocks_info working")
		print("ran")


if __name__ == '__main__':
	print(dicti)
	json_object = json.dumps(dicti, indent = 4)
	with open("stocks_info", "w") as outfile:
		outfile.write(json_object)



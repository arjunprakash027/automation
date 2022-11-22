from yahoofinancials import YahooFinancials
from datetime import date,timedelta


def analyse_stock(stock):
    today = date.today()
    period = timedelta(days=20)
    twenty_days = today - period


    yahoo_financials = YahooFinancials('{}.NS'.format(stock))
    historical_stock_prices = yahoo_financials.get_historical_price_data(str(twenty_days), str(today) , 'daily')
    total_for_MO = 0
    hist_prices = historical_stock_prices['{}.NS'.format(stock)]['prices']


    positive = 0
    negative = 0


    #------current details-----#
    price =  yahoo_financials.get_current_price()
    #-----fifty day moving avg------#
    fifty_ma = yahoo_financials.get_50day_moving_avg()
    if fifty_ma - price > 0:
        positive += 1
    else:
        negative += 1

    #--------momentum osccilator------#
    for i in range(len(hist_prices)):
            total_for_MO += hist_prices[i]['close']

    MO = (price/total_for_MO) * 100	

    #------calculating VWAP----------#

    cummulative_price = 0
    cummulative_volume = 0 
    for i in range(len(hist_prices)):
        hist_prices[i]['close']
        cummulative_total = ((hist_prices[i]['high']+hist_prices[i]['low']+hist_prices[i]['close'])/3) * hist_prices[i]['volume']
        cummulative_price += cummulative_total
        cummulative_volume += hist_prices[i]['volume']
    VWAP = cummulative_price/cummulative_volume
    if VWAP > price:
        positive += 1
    else:
        negative += 1




    #-------------final result--------------------#

    if positive > negative:
        return("expected positive growth")
    else:
        return("expected negative growth")
        



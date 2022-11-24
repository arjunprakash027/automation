import requests
import logging
logging.basicConfig(filename ='app.log',
                        level = logging.INFO)

def daily_q():
    x = requests.get('https://zenquotes.io/api/today')
    quote = x.json()
    logging.info('daily_q working')
    return quote


if __name__ == '__main__':
    print(daily_q())

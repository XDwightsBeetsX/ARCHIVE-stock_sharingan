# Stock-Sharingan :chart_with_upwards_trend:

![build-status](https://travis-ci.com/XDwightsBeetsX/stock-sharingan.svg?branch=master)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

This app gives insight into the movements of the market and provide updates/notifications on triggered events.  
Data can be configured to save to disc or be sent by email / sms.  

## Documentation :book:
Placeholder text for documenting this app  
This app is gonna do cool stuff like send emails with market winners
and configuring that will be described here...

## The IEX Cloud API :computer:
||API Documentation|API Examples|Repo Interface|PyPI|Lang|Free|
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
|[**IEX Cloud**](https://iexcloud.io/):cloud:|[:book:](https://iexcloud.io/docs/api)|[:pencil:](https://github.com/addisonlynch/iexfinance#common-usage-examples) [:pencil:](https://github.com/addisonlynch/iex-examples)|[addisonlynch](https://github.com/addisonlynch/iexfinance) [:book:](https://addisonlynch.github.io/iexfinance/stable/stocks.html)|[:book:](https://pypi.org/project/iexfinance/)|`python`|:white_check_mark:|

Remember API have limits on calls!

### API Call Endpoints
- #### Stocks
|Endpoint|Weight|Example Call|Example Response|
|:--|---|---|:-:|
|get_price()|1|`tsla = Stock('TSLA')  tsla.get_price()`| |
|get_quote()|1|`a = Stock("AAPL")  a.get_quote()`| |
|get_historical_data()|10 / stock / unit time requested|`start = datetime(2017, 1, 1)  end = datetime(2018, 1, 1)  df = get_historical_data("TSLA", start, end)`| |
|get_social_sentiment()|#|`get_social_sentiment("AAPL")`| |
|get_ceo_compensation()|#|`get_ceo_compensation("AAPL")`| |

- #### RefData
|Endpoint|Weight|Example Call|Example Response|
|:--|---|---|:-:|
|get_symbols()|100|`get_symbols()`| |
|get_iex_symbols()|100|`get_iex_symbols()`| |

- #### Account
|Endpoint|Weight|Example Call|Example Response|
|:--|---|---|:-:|
|get_usage()|0|`get_usage(quota_type='messages')`| |
|get_api_status()|0|`get_api_status()`| |

Always include the argument `token="<YOUR API KEY>"` in endpoint calls!

## Troubleshooting :worried:
- Check your API key and location
- Check the `requirements.txt` and your python environment packages

###### :warning: THIS PROJECT BEARS NO FINANCIAL RESPONSIBILITY. DATA MAY NOT BE EXACT :warning:

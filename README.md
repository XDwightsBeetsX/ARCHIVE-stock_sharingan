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
|[**IEX Cloud**](https://iexcloud.io/):cloud:|[:book:](https://iexcloud.io/docs/api)|[:pencil:](https://github.com/addisonlynch/iexfinance#common-usage-examples) [:pencil:](https://github.com/addisonlynch/iex-examples)|[addisonlynch](https://github.com/addisonlynch/iexfinance) [:book:](https://addisonlynch.github.io/iexfinance/stable/stocks.html#)|[:book:](https://pypi.org/project/iexfinance/)|`python`|:white_check_mark:|

Remember API have limits on calls!

### API Call Endpoints
|Endpoint|Weight|Example Call|Example Response|
|:--|---|:-:|:-:|
|Time Series|0| | |
|Price Only|1| | |
|Last (Price)|0| | |
|Quote|1| | |
|Company Data|1| | |
|Key Stats|5 for full, 1 for single| | |
|News|1| | |
|Historical Price|10 / stock / unit time requested| | |
|Reference Data|100| | |

## Troubleshooting :worried:
- Check your API key and location
- Check the `requirements.txt` and your python environment packages

###### :warning: THIS PROJECT BEARS NO FINANCIAL RESPONSIBILITY. DATA MAY NOT BE EXACT :warning:

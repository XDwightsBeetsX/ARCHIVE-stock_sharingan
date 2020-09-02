# Stock-Sharingan :chart_with_upwards_trend:

![build-status](https://travis-ci.com/XDwightsBeetsX/stock-sharingan.svg?branch=master)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

Experiment ways to monitor and predict the market trends.  
Provide updates/notifications on triggered events.  

## Documentation :book:

## [API](https://en.wikipedia.org/wiki/Application_programming_interface) :computer:
:warning: **API have limits on calls** :warning:

#### API Docs [:book:](https://iexcloud.io/docs/api)
| |Docs|API Examples|Repo Interface|Lang|Free|
|------|------|------|------|------|------|
|[**IEX Cloud**](https://iexcloud.io/)|[:book:](https://iexcloud.io/docs/api)|------|[addisonlynch](https://github.com/addisonlynch/iexfinance)|`python`|:white_check_mark:|
Additional documentation and examples on the API can be found on [PyPi](https://pypi.org/project/iexfinance/).

#### Call Endpoints [:book:](https://iexcloud.io/docs/api/#rules-engine-beta)
|Endpoint|Weight|Example Call|Sample Response|
|------|------|------|------|
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

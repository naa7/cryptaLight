# cryptaLight

![Open Source Love](https://badges.frapsoft.com/os/v3/open-source.svg?v=103) <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"> <img src="https://img.shields.io/github/stars/naa7/cryptaLight?style=social"> <img src="https://img.shields.io/github/repo-size/naa7/cryptaLight"> [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/naa7/cryptaLight/LICENSE)

<img src="https://github.com/naa7/cryptaLight/blob/main/cryptaLight.gif"></br>


The idea if this project is to make a program that tracks the price and related information of desired 
cryptocurrencies and updates the prices every five seconds. CoinGecko's API is used for fetching data needed 
by the program. To make it easier to track prices, the program updates every five seconds and if price changes, the
arrow blinks either up or down depending on the change from last update. In addition, if the crytocurrency 
percentage change in the last 24 hours is less than negative, it will display in red. Otherwise, it will display 
in green.

There are two versions of the program, full-version and light-version. The full-version, `cryptaLight.py`, displays
all information. The light-version, `cryptaLight_lightVersion.py`, displays only coin's symbol and price.


## To run the program:

    $ cd && git clone https://github.com/naa7/cryptaLight.git

    $ cd cryptaLight/

    $ python cryptaLight.py
  
    OR

    $ python cryptaLight_lightVersion.py

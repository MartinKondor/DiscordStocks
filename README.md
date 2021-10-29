<p align="center">
    <img width="800px" src="img/example.gif">
</p>

# <img width="35px" src="img/profile.png"> DiscordStocks

[![Project Status](https://img.shields.io/badge/status-active-brightgreen.svg)](https://github.com/MartinKondor/DiscordStocks/)
[![version](https://img.shields.io/badge/version-2021.10-brightgreen.svg)](https://github.com/MartinKondor/DiscordStocks)
[![GitHub Issues](https://img.shields.io/github/issues/MartinKondor/DiscordStocks.svg)](https://github.com/MartinKondor/DiscordStocks/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-blue.svg)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://opensource.org/licenses/BSD)

Discord bot for asking down various informations about stocks. Based on the free [Alpha Vantage](https://www.alphavantage.co) API.

## Prerequisites

Dependencies (see [requirements.txt](./requirements.txt)):

* Python >3.8
* requests==2.25.1
* discord.py==1.7.3
* discord==1.7.3
* python-dotenv==0.19.1

To use this bot you will need to define these environmental variables:

```DISCORD_TOKEN, DISCORD_GUILD, ALPHA_VANTAGE_API_KEY```

It is advised to create a file named ```.env``` in the ```/bot``` directory, and insert these variables into it for easier usage:

```
# .env
DISCORD_TOKEN=...
DISCORD_GUILD=...
ALPHA_VANTAGE_API_KEY=...
```

## Usage

To first start the bot you need to run these commands:

```
$ pip install -r requirements.txt
$ python bot
```

After these a similar message should be displayed on the console:

```
BOT_NAME is connected to the following guild:
SERVER_NAME(id: ....)
```

## Commands

There are various commands you can use with this bot, here is a list which can be used as a reference:

* **/price TICKER**: The current stock's price.
* **/open TICKER**: The last stock's open price.
* **/low TICKER**: The stock's lowest price that day.
* **/high TICKER**: The stock's highest price that day.
* **/volume TICKER**: The current stock's volume.
* **/date TICKER**: The stock's latest trading day's date (YYYY-MM-DD).
* **/prev TICKER**: The stock's price at the end of the previous close.
* **/change TICKER**: The stock's price change that day.
* **/cp TICKER**: The stock's price change that day in percents (0.0000%).

## Authors

* **[Martin Kondor](https://github.com/MartinKondor)**

## License

Copyright &copy; Martin Kondor 2021

This repository is licensed under the ```BSD 3-Clause``` license.
See the [LICENSE](./LICENSE) file for more details.

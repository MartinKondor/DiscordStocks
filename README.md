<p align="center">
    <img width="200px" src="img/example.gif">
</p>

# <img width="25px" src="img/profile.png"> DiscordStocks

Discord bot for asking down various informations about stocks. Based on the free [Alpha Vantage](https://www.alphavantage.co) API.

## Prerequisites

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

To start the bot you need to run this command:

```
python bot
```

After that a similar message should be displayed on the console:

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

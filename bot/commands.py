from stocks import Stocks
from discord.ext import commands


stocks = Stocks()

"""
:arg str: Stock symbol (ticker)
"""
@commands.command(name="price")
async def price_cmd(ctx, arg):
    result = stocks.get_price(arg)
    if "Error:" in result:
        await ctx.send(result)
    await ctx.send(f"Current price for {arg} is {result}")


"""
:arg str: Stock symbol (ticker)
"""
@commands.command(name="open")
async def open_cmd(ctx, arg):
    result = stocks.get_open(arg)
    if "Error:" in result:
        await ctx.send(result)
    await ctx.send(f"The last open price for {arg} is {result}")


"""
:arg str: Stock symbol (ticker)
"""
@commands.command(name="low")
async def low_cmd(ctx, arg):
    result = stocks.get_low(arg)
    if "Error:" in result:
        await ctx.send(result)
    await ctx.send(f"The lowest price today for {arg} is {result}")


"""
:arg str: Stock symbol (ticker)
"""
@commands.command(name="high")
async def high_cmd(ctx, arg):
    result = stocks.get_high(arg)
    if "Error:" in result:
        await ctx.send(result)
    await ctx.send(f"The highest price today for {arg} is {result}")


"""
:arg str: Stock symbol (ticker)
"""
@commands.command(name="volume")
async def volume_cmd(ctx, arg):
    result = stocks.get_volume(arg)
    if "Error:" in result:
        await ctx.send(result)
    await ctx.send(f"The volume for {arg} is {result}")


"""
:arg str: Stock symbol (ticker)
"""
@commands.command(name="date")
async def date_cmd(ctx, arg):
    result = stocks.get_date(arg)
    if "Error:" in result:
        await ctx.send(result)
    await ctx.send(f"The last trading day's date for {arg} is {result}")


"""
:arg str: Stock symbol (ticker)
"""
@commands.command(name="prev")
async def prev_cmd(ctx, arg):
    result = stocks.get_prev(arg)
    if "Error:" in result:
        await ctx.send(result)
    await ctx.send(f"The price at the previous close for {arg} is {result}")


"""
:arg str: Stock symbol (ticker)
"""
@commands.command(name="change")
async def change_cmd(ctx, arg):
    result = stocks.get_change(arg)
    if "Error:" in result:
        await ctx.send(result)
    await ctx.send(f"Today's change for {arg} is {result}")


"""
:arg str: Stock symbol (ticker)
"""
@commands.command(name="cp")
async def cp_cmd(ctx, arg):
    result = stocks.get_cp(arg)
    if "Error:" in result:
        await ctx.send(result)
    await ctx.send(f"Today's percentage change for {arg} is {result}")

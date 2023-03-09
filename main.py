# This example requires the 'message_content' intent.

import discord
from wallet import balance_account, send_transaction, create_account, request_airdrop
from discord.ext import commands
from solathon import Client, PublicKey
from solathon.utils import lamport_to_sol



intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='/', intents=intents)
client = Client("https://api.devnet.solana.com")
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def create(ctx):
    pub = create_account()
    message = f'Conta criada com sucesso\n\nInformações da conta\n Chaves:\n {pub}'
    await ctx.send(message)  

@bot.command()
async def airdrop(ctx,amount, public_key):
    await ctx.send("Solicitando airdrop...")
    resposta = request_airdrop(amount, public_key)
    message = f'Request Airdrop\n\nID da transação: {resposta}\n Feito com sucesso!'
    await ctx.send(message)      

@bot.command()
async def balance(ctx, public_key):
    saldo = balance_account(public_key)
    message = f'O saldo da chave é de {saldo} SOL'
    await ctx.send(message)

@bot.command()
async def send(ctx, private_key, public_key, amount):
    try:
        trans = send_transaction(private_key, public_key, amount)
        trans = trans['result']
        message = f'Transação realizada com sucesso.\n\nID da transação:\n\n{trans}!'
        await ctx.send(message)
    except Exception as e:
        trans = trans['error']['data']
        message = f"Ocorreu um erro ao enviar a transação.\n\nLog do erro:\n\n{trans}"
        await ctx.send(message)


bot.run('TOKEN DO BOT')

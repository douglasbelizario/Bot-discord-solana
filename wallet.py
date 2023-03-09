from solathon import Client, PublicKey, Transaction, Keypair
from solathon.utils import lamport_to_sol, sol_to_lamport
from solathon.core.instructions import transfer

client = Client("https://api.devnet.solana.com")

def create_account():
    new_account = Keypair()
    new_account.public_key,"Chave privada: ",new_account.private_key
    return new_account.public_key, new_account.private_key

def request_airdrop(amount, public_key):
    amount = sol_to_lamport(int(amount))
    res = client.request_airdrop(public_key, amount)
    res = res['result']
    return res
    

def balance_account(public_key):
  
    balancee = client.get_balance(public_key)
    balancee = balancee['result']['value']
    balancee = lamport_to_sol(balancee)
    return balancee
    
    
def send_transaction(private_key, public_key, amount):
    sender = Keypair().from_private_key(private_key)
    receiver = PublicKey(public_key)
    ll = sol_to_lamport(int(amount))

    instruction = transfer(
    from_public_key=sender.public_key,
    to_public_key=receiver, 
    lamports=ll
    )
    transaction = Transaction(instructions=[instruction], signers=[sender])
    result = client.send_transaction(transaction)
    return result


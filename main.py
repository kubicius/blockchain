from fastapi import FastAPI
import json
from blockchain import Blockchain

app = FastAPI()
blockchain = Blockchain()

@app.get('/chain')
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                      "chain": chain_data})

def post_transaction():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                      "chain": chain_data})

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import json
import time

from blockchain import Blockchain

app = FastAPI()
blockchain = Blockchain()
templates = Jinja2Templates(directory="templates/")

@app.get('/')
def get_ui(request: Request):
    return templates.TemplateResponse('mytemplate.html', context={'request': request})

@app.get('/api/chain/get')
def get_chain():
    """
    Returns full chain.
    """
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                      "chain": chain_data})

@app.get('/api/chain/length')
def get_chain_length():
    """
    Returns number of blocks.
    """
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return len(chain_data)

@app.post('/api/transactions/new')
def add_new_transaction(person_id: int, person_name: str, doctor: str, report: str, medicine: str):
    """
    Adds new transaction.
    """
    return blockchain.add_new_transaction({"person_id": person_id, "person_name": person_name, "doctor": doctor, "report": report, "medicine": medicine})

@app.get('/api/mine')
def mine():
    """
    Returns index of mined block.
    """
    return blockchain.mine()
from fastapi import FastAPI, Request
import json
from userInterface import UserInterface
from blockchain import Blockchain

app = FastAPI()
blockchain = Blockchain()
ui = UserInterface()

@app.get('/')
def get_ui_welcome_screen(request: Request):
    """
    Returns html code with welcome message.
    """
    return ui.show_template(request, "<p>Hello dear doctor!</p><p>Please choose an action from menu.</p>")

@app.get('/all-records')
def get_ui_all_records(request: Request):
    """
    Returns html code with all records listed.
    """
    return ui.show_template(request, ui.prepare_all_records(blockchain))

@app.get('/number-of-records')
def get_ui_number_of_records(request: Request):
    """
    Returns html code with information about number of blocks.
    """
    return ui.show_template(request, "Number of blocks in chain: "+str(get_chain_length()))

@app.get('/new-record')
def get_ui_new_record_form(request: Request):
    """
    Returns html code with form for creating new records.
    """
    return ui.show_template(request, "Number of blocks in chain: "+str(get_chain_length()))

@app.get('/mine')
def get_ui_new_record_form(request: Request):
    """
    Returns html code with mining button and result.
    """
    return ui.show_template(request, "Number of blocks in chain: "+str(get_chain_length()))

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
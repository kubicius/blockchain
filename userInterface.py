from fastapi.templating import Jinja2Templates

class UserInterface:
    """
    Class preparing html templates.
    """
    def __init__(self):
        self.templates = Jinja2Templates(directory="templates/")

    def show_template(self, request, result):
        return self.templates.TemplateResponse('default.html', context={'request': request, 'result': result})

    def prepare_all_records(self, blockchain, filter, id):
        result = ""
        if filter:
            result += "<div class='row filter'>"
            result += "<form method='GET'>"
            result += "<div class='col'>"
            result += "<label for='id'>Person ID:</label>"
            result += "<input type='hidden' name='filter' value='True'>"
            result += "<input id='id' name='id' required>"
            result += "<input type='submit' value='Filter'>"
            result += "</div>"
            result += "</form>"
            result += "</div>"
        result += "<div class='row'>"
        for label in ['person_id', 'person_name', 'doctor', 'report', 'medicine']:
            result += "<div class='col result__label'>"
            result += "<span>" + label + "</span>"
            result += "</div>"
        result += "</div>"
        for block in blockchain.chain:
            t = block.transactions
            if len(block.transactions) == 1:
                if filter == False or block.transactions[0]['person_id'] == id:
                    result += "<div class='row'>"
                    for t in block.transactions[0]:
                        result += "<div class='col result__data'>"
                        result += "<span>"+str(block.transactions[0][t])+"</span>"
                        result += "</div>"
                    result += "</div>"
        return result

    def prepare_mine_result(self, fired, mined):
        result = ""
        if fired:
            if mined:
                result = "<p>Mined block: " + str(mined) + "</p>"
            else:
                result = "<p>Nothing to mine.</p>"
        result += "<button onclick='window.location.href=\"/mine?fired=True\"'>MINE!</button>"
        return result

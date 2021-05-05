from fastapi.templating import Jinja2Templates

class UserInterface:
    """
    Class preparing html templates.
    """
    def __init__(self):
        self.templates = Jinja2Templates(directory="templates/")

    def show_template(self, request, result):
        return self.templates.TemplateResponse('default.html', context={'request': request, 'result': result})

    def prepare_all_records(self, blockchain):
        result = "<div class='row'>"
        for label in ['person_id', 'person_name', 'doctor', 'report', 'medicine']:
            result += "<div class='col result__label'>"
            result += "<span>" + label + "</span>"
            result += "</div>"
        result += "</div>"
        for block in blockchain.chain:
            t = block.transactions
            if len(block.transactions) == 1:
                result += "<div class='row'>"
                for t in block.transactions[0]:
                    result += "<div class='col result__data'>"
                    result += "<span>"+str(block.transactions[0][t])+"</span>"
                    result += "</div>"
                result += "</div>"
        return result


import sys
from docxtpl import DocxTemplate

class Document():

    def __init__(self, path_to_tpl) -> None:
        self.template = DocxTemplate(path_to_tpl)

        if self.template is None:
            print("[!] - Could not load template")
            sys.exit()

    def write(self, dict_content: dict):
        '''
        Rellena una seccion del documento con el contenido dado.
        '''

        self.template.render(dict_content)

    def build(self):
        self.template.save('out.docx')

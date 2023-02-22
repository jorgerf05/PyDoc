#!/bin/python3

from docxtpl import DocxTemplate

class Document():
    
    def __init__(self, path_to_tpl) -> None:
        try:
            self.template = DocxTemplate(path_to_tpl)
            print("[!] - Succesfully opened template.")
        except:
            print("[!] - Could not open template")
            
        if self.template is None:
            print("[!] - Template is None")
    
    def write(self, section: str, content:str):
        '''
        Rellena una seccion del documento con el contenido dado.
        '''
        
        context = {
            f'{section}':f'{content}'
        }
        
        self.template.render(context)
    
    def build(self):
        self.template.save('out.docx')
        
    
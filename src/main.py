#!/bin/python3

from document import Document
from response import Generator

def main():
    
    secciones = [
        'Introduccion',
        'desarrollo'
    ]
    
    gen = Generator()
    gen.response(secciones, "el hielo en mexico")
    
    #doc = Document('C:\\Users\\jorge\\Dev\\PyDoc\\src\\Introduccion.docx')
    #doc.write('Introduccion', 'prueba de la intro')
    #doc.write('desarrollo', 'prueba del desarrollo')
    #doc.build()
    
    
if __name__ == "__main__":main()
#!/bin/python3

from document import Document
from generator import Generator


def main():

    lista_secciones = [
        'introduccion',
        'desarrollo',
        'conclusiones'
    ]

    # Inicializamos un diccionario con values None
    dict_secciones = {section: None for section in lista_secciones}

    gen = Generator()
    gen.fillDocument(dict_secciones, "Sensores para arduino UNO")

    # TODO: Parsear esta ruta como argumentos del script
    doc = Document('C:\\Users\\jorge\\OneDrive\\Documentos\\template_sistemas_programables.docx')
    doc.write(dict_secciones)
    doc.build()  # Guardamos el documento


if __name__ == "__main__":
    main()
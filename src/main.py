#!/bin/python3


import re
import argparse
import docx2txt
from document import Document
from generator import Generator


def parseTemplate():

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--template', type=str, help='Path to the docx template')
    parser.add_argument('-T', '--topic', type=str, help='Topic of interest')
    args = parser.parse_args()
    return args.template, args.topic

def detection(path_to_template:str):

    raw_text = docx2txt.process(path_to_template)
    secciones = re.findall('\{\{(.+?)\}\}', raw_text)
    return secciones


def main():

    template, topic  = parseTemplate()

    #TODO: detectar las secciones de manera automatica.
    lista_secciones = detection(template)

    # Inicializamos un diccionario con values None
    dict_secciones = {section:None for section in lista_secciones}

    gen = Generator()
    gen.fillDocument(dict_secciones, topic)

    doc = Document(template)
    doc.write(dict_secciones)
    doc.build()  # Guardamos el documento


if __name__ == "__main__":
    main()

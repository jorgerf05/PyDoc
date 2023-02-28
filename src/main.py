#!/bin/python3


import re
import argparse
import docx2txt
from document import Document
from generator import Generator


def parse_template():

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--template', type=str, help='Path to the docx template', required=True)
    parser.add_argument('-T', '--topic', type=str, help='Topic of interest', required=True)
    parser.add_argument('-o', '--output', type=str, help='Output path', required=True)
    args = parser.parse_args()
    return args.template, args.topic, args.output


def detection(path_to_template:str):

    raw_text = docx2txt.process(path_to_template)
    secciones = re.findall(r'\{\{(.+?)\}\}', raw_text)
    return secciones


def main():

    template, topic, output = parse_template()
    lista_secciones = detection(template)

    # Inicializamos un diccionario con values None
    dict_secciones = {section:None for section in lista_secciones}

    gen = Generator()
    gen.fill_document(dict_secciones, topic)

    doc = Document(template)
    doc.write(dict_secciones)
    doc.build(output)  # Guardamos el documento


if __name__ == "__main__":
    main()

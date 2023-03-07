#!/usr/bin/env python
"""
Main module for PyDoc
"""

import re
import argparse
import docx2txt
from document import Document
from generator import Generator


def getargs():
    """
    Gets argument from the commmand line
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--template", type=str, help="Path to the docx template", required=True
    )
    parser.add_argument(
        "-T", "--topic", type=str, help="Topic of interest", required=True
    )
    parser.add_argument("-o", "--output", type=str, help="Output path", required=True)
    args = parser.parse_args()
    return args.template, args.topic, args.output


def detection(path_to_template: str):
    """
    Detects sections from a template to be generated.
    """
    raw_text = docx2txt.process(path_to_template)
    detected_sections = re.findall(r"\{\{(.+?)\}\}", raw_text)
    return detected_sections


def main():
    """
    Main method
    """
    template, topic, output = getargs()
    detected_sections = detection(template)

    # Initialize a dictionary with key -> None
    sections = {section: None for section in detected_sections}

    gen = Generator()
    # gen.generate_sections_gpt3(dict_secciones, topic)
    gen.generate_sections_gpt35(sections, topic)

    doc = Document(template)
    doc.write(sections)
    doc.build(output)  # Guardamos el documento


if __name__ == "__main__":
    main()

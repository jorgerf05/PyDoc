"""
Contains the Document class.
"""
import sys
from docxtpl import DocxTemplate


class Document:
    """ """

    def __init__(self, path_to_tpl) -> None:
        self.template = DocxTemplate(path_to_tpl)
        print(f"[+] Loading template from {path_to_tpl}")

        if self.template is None:
            print("[!] Could not load template!")
            sys.exit()

    def write(self, dict_content: dict):
        """
        Fills each section of a template with a given dictionary.
        """

        try:
            print("[+] Creating document")
            self.template.render(dict_content)
        except:
            print("[!] Failed to render document!")

    def build(self, out_path: str):
        """
        Saves the document in the specified path
        """
        try:
            print("[+] Saving document")
            self.template.save(out_path)
        except:
            print("[!] Error saving document!")

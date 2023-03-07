"""
Contains the Generator class
"""
import asyncio
import openai
from chatgpt_wrapper import ChatGPT


class Generator:
    """
    Used to access different generation methods for document content creation
    """

    def __init__(self) -> None:
        openai.api_key = "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"

    def generate_sections_gpt3(self, sections: dict, topic: str):
        """
        Fills the sections dict using DaVinci-003
        """

        print("[+] Using DaVinci-003 generation")

        for section in sections:
            print(f"[+] Generating section -> {section}")

            res = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"""
                Crea la sección {section} para un trabajo sobre {topic}
                """,
                max_tokens=1024,  # Up to 4096 - prompt
            )
            sections[section] = res.choices[0].text

    def generate_sections_gpt35(self, sections: dict, topic: str):
        """
        Fills the sections dict using GPT3.5-turbo
        """

        print("[+] Using GPT-3.5-Turbo generation")

        for section in sections:
            print(f"[+] Generating section -> {section}")

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": """Eres un asistente que ayudará a realizar trabajos de investigación. Da respuestas largas y detalladas. """,
                    },
                    {
                        "role": "user",
                        "content": f"Crea la sección {section} para un trabajo sobre {topic}",
                    },
                ],
                max_tokens=4000,  # Up to 4096 - prompt
            )
            sections[section] = response["choices"][0]["message"]["content"]

    def generate_sections_chatgpt(self, sections: dict, topic: str):
        """
        Fills the sections dict using ChatGPT
        """

        print("[+] Using ChatGPT generation")
        bot = ChatGPT()

        for section in sections:
            print(f"[+] Generating section -> {section}")

            response = asyncio.run(
                bot.ask(f"Generate the section {section} for a paper about {topic}")
            )
            sections[section] = response

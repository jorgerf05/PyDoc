import openai


class Generator():

    def __init__(self) -> None:
        openai.api_key = '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'

    def fillDocument(self, sections: dict, topic: str):
        '''
        Método que se encarga de rellenar el diccionario sections modificándolo con 
        el texto generado por GPT-3
        '''

        for section in sections:

            print(f'[+] Generating section -> {section}')
            # No usar ADA, es basura.

            res = openai.Completion.create(
                model='text-davinci-003',
                # model = 'text-ada-001',
                prompt=f'''
                Crea la sección {section} para un trabajo sobre {topic}
                ''',
                max_tokens=1024  # Ojo
            )
            sections[section] = res.choices[0].text

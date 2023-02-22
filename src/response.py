import openai

class Generator():
    
    def __init__(self) -> None:
        openai.api_key = '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'
    
    def response(self, sections:list, topic:str) -> str:
        
        for section in sections:

            res = openai.Completion.create(
                model = 'text-davinci-003',
                prompt = f'''
                Crea la sección {section} para un trabajo sobre {topic}
                ''',
                max_tokens = 1024
            )
            print(res.choices[0].text)
            
        
        
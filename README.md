# PyDoc
PyDoc is a "little help" to generate a Microsoft Word document about a given topic. It uses GPT-3 to fill in the content

### Usage
PyDoc needs a document template to work with. This template must include section tags {{likethis}}. You may want to use tags like {{introduction}}, {{abstract}}, {{conclusions}}, etc.
PyDoc will then fill in this sections.
```bash
./main.py -T "Topic" -t 'path_to_template' -o 'Out.docx'
```


### Dependencies
PyDoc depends on:
- Python <= 3.10
- docxtpl
- openai

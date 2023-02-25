# PyDoc
PyDoc is a "little help" to generate a Microsoft Word document about a given topic. It uses GPT-3 to fill in the content

### Usage
PyDoc needs a document template to work with. This template must include section tags {{likethis}}. You may want to use tags like {{introduction}}, {{abstract}}, {{conclusions}}, etc.
PyDoc will then fill in this sections.
```bash
./main.py -T "Topic" -t 'path_to_template' -o '/home/user/output.docx'
```


### Dependencies
PyDoc depends on:
- Python <= 3.10
- docxtpl
- openai
- docx2txt

## Example template
You must have a template with section tags like this:
![image](https://user-images.githubusercontent.com/63943396/221334897-9fef4d84-4a21-4312-b1d0-d12338df77d0.png)

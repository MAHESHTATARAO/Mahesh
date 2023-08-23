#first we have install flask translate 
# comand : pip install flask translate

#now coming to the code 
from flask import Flask, render_template, request, jsonify
from translate import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        source_language = request.form.get('source_language')
        target_language = request.form.get('target_language')
        text_to_translate = request.form.get('text_to_translate')

        translator = Translator(from_lang=source_language, to_lang=target_language)
        translated_text = translator.translate(text_to_translate)

        return jsonify({'translated_text': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

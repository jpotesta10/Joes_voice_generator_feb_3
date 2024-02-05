import os
from flask import Flask, request, Response, render_template
from elevenlabs import generate, set_api_key

app = Flask(__name__)

# Set the Eleven Labs API key using the environment variable
api_key = os.environ.get('ELEVEN_API_KEY')

set_api_key(api_key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_audio():
    data = request.json
    text = data.get('text')
    audio = generate(text=text, voice = 'Joe American')
    return Response(audio, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)

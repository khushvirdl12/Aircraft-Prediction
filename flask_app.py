from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/identify', methods=['POST'])
def identify():
    file = request.files['file']
    files = {'file': (file.filename, file.stream, file.content_type)}
    response = requests.post('http://localhost:8501/', files=files)  # Streamlit URL
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000)

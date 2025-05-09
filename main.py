from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
from llm.generator import generate_meditation
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return app.send_static_file("index.html")

# Route to generate meditation
@app.route('/generate', methods=["POST"])
def generate():
    try:
        print("Received a request to /generate")  # DEBUG LOG

        data = request.get_json()
        user_input = data['prompt']
        print(f"User input: {user_input}")  # DEBUG LOG

        text, audio_path = generate_meditation(user_input)
        print(f"Meditation generated at: {audio_path}")  # DEBUG LOG

        return jsonify({
            "text": text,
            "audio_url": f"/audio/{os.path.basename(audio_path)}"
        })

    except Exception as e:
        print("Error during generation:", e)
        return jsonify({"error": str(e)}), 500

@app.route('/audio/<filename>')
def serve_audio(filename):
    audio_dir = os.path.join(os.path.dirname(__file__), 'llm', 'output')
    return send_from_directory(audio_dir, filename)

if __name__ == '__main__':
    app.run(debug=True)
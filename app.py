from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Paste your Gemini API key here
genai.configure(api_key="AQ.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message", "")

    try:
        response = model.generate_content(user_message)

        return jsonify({
            "response": response.text
        })

    except Exception as e:
        return jsonify({
            "response": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    app.run(debug=True)
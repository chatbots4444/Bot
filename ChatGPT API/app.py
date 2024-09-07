from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from flask import render_template
app = Flask(__name__)

# Set up Gemini API credentials
genai.configure(api_key='AIzaSyDY14vxVg7N3ljHL1ZcGxrFwT50Y8YVofU')

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/")
def index2():
    return render_template("index2.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")
    is_admin = request.json.get("isAdmin", False)

    try:
        model = genai.GenerativeModel('gemini-pro')
        if is_admin:
            # ตรงนี้เราสามารถเพิ่มโลจิกเฉพาะสำหรับ admin chat ได้
            response = model.generate_content(f"[ADMIN MODE] {message}")
        else:
            response = model.generate_content(message)
        return jsonify({"content": response.text})
    except Exception as e:
        print(f"Error using Gemini API: {e}")
        return jsonify({"content": 'Failed to Generate response!'})

if __name__ == '__main__':
    app.run(debug=True)

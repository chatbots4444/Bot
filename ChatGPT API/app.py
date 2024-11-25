from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Set up Gemini API credentials
genai.configure(api_key='AIzaSyDOBg3Np22fY9R91Ozy4WhFCGky8PP1FfQ')

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index2")
def index2():
    return render_template("index2.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route('/login')
def login():
    return render_template('login.html')

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")

    try:
        # Generate content using Gemini
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(message)
        return jsonify({"content": response.text})
    except Exception as e:
        print(f"Error using Gemini API: {e}")
        return jsonify({"content": 'Failed to Generate response!'})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        data = request.get_json()  # Process POST request
        user_message = data.get("message")
        return jsonify({"response": f"Received: {user_message}"})
    else:
        return "GET request is working!"  # Handle GET request


if __name__ == '__main__':
    app.run(debug=False)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a function to generate chatbot responses
def get_bot_response(user_message):
    user_message = user_message.strip().lower()  # Clean and standardize user input

    # Keyword-based responses (you can expand this with more logic later)
    if "hello" in user_message:
        return "Hi there! How can I assist you today?"
    elif "bye" in user_message:
        return "Goodbye! Have a great day!"
    elif "help" in user_message:
        return "I'm here to assist you. You can ask me about anything!"
    else:
        return "Sorry, I didn't understand that. Could you rephrase?"

# Route for handling chat requests
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Ensure JSON data was sent
        data = request.get_json()

        # Check if 'message' field exists in the JSON data
        if not data or "message" not in data:
            return jsonify({"error": "Invalid request, 'message' field is missing"}), 400

        user_message = data.get("message")

        # Validate that the user message is not empty
        if not user_message.strip():
            return jsonify({"response": "Please enter a valid message."}), 400

        # Get a response from the bot
        bot_response = get_bot_response(user_message)

        # Return the bot's response
        return jsonify({"response": bot_response})

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

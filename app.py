from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    response = get_bot_response(user_input)
    return jsonify({'response': response})

def get_bot_response(input):
    responses = {
        "hello": "Hi there! How can I help you with your travel plans?",
        "where should I go?": "It depends on your interests! Do you prefer beaches or mountains?",
        "what's the best time to visit europe?": "The best time is usually spring (April to June) or fall (September to October).",
        "thank you": "You're welcome! If you have more questions, just ask!",
    }
    return responses.get(input.lower(), "I'm not sure about that. Can you ask something else?")

if __name__ == '__main__':
    app.run(debug=True)

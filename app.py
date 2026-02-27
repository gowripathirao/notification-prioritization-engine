from flask import Flask, request, jsonify
from decision import decide_notification

app = Flask(__name__)


# Home page

@app.route('/')
def home():

    return "Notification Prioritization Engine Running"



# Notification API

@app.route('/notification', methods=['POST'])

def notification():

    data = request.json

    decision, score, reason = decide_notification(data)

    return jsonify({

        "decision": decision,
        "score": score,
        "reason": reason

    })


if __name__ == '__main__':

    app.run(debug=True)

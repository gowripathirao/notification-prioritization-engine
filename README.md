Problem Statement

Users receive many notifications from different services such as messages, reminders, alerts and promotions.

Some notifications are important while others are unnecessary or repetitive.

This system decides whether a notification should be:

NOW  → Send immediately  
LATER → Send later  
NEVER → Suppress notification
System Architecture
Incoming Event
      ↓
Flask API Server
      ↓
Decision Engine
      ↓
Final Decision (Now/Later/Never)
Components

Flask API Server

Decision Logic Module

Rule-based Classification

Decision Logic

Each notification includes:

user_id

event_type

priority_hint

Example event types:

security_alert

message

reminder

update

promotion

Score Calculation
Score = Base Priority + (Priority Hint / 2)
Decision Rules
Score ≥ 80 → NOW

Score ≥ 50 → LATER

Score < 50 → NEVER
Duplicate Prevention Strategy

Duplicate notifications can be avoided using:

user_id + event_type + message

If the same notification appears again within a short time it can be suppressed.

Alert Fatigue Reduction

The system reduces too many notifications by:

Giving lower priority to promotions

Sending important alerts first

Example:

security_alert → NOW

promotion → NEVER
API Interface
POST /notification

Example Input:

{
"user_id":1,
"event_type":"message",
"priority_hint":80
}

Example Output:

{
"decision":"NOW",
"score":90,
"reason":"High priority notification"
}
Fallback Strategy

If system fails or data is missing:

Default Decision = LATER

This ensures important notifications are not lost.

Monitoring Plan

The system can track:

Number of notifications processed

NOW decisions

LATER decisions

NEVER decisions

Tools Used
Python
Flask
GitHub
AI Assistance

ChatGPT was used for design guidance and architecture ideas.

The implementation and documentation were completed manually.

Data Model

The system uses a simple data structure for notification events.

Each event contains:

user_id
event_type
priority_hint
timestamp
channel
message

Example Event:

{
"user_id":1,
"event_type":"message",
"priority_hint":80,
"channel":"push",
"message":"New message received"
}

Decision Explanation

For each notification the system stores a reason for the decision.

Example:

Decision: NOW

Reason:
High priority notification

Configurable Rules

The system supports configurable rules for different event types.

Example rules:

security_alert → Always NOW

promotion → Usually NEVER

message → NOW or LATER depending on priority

These rules can be modified easily in the decision.py file without changing the whole system.

This allows flexible notification control.

Decision Strategy

The system uses a combination of:

Rule-based logic

Priority scoring

This approach provides fast decisions with low latency and ensures important notifications are delivered on time.

API Endpoints

The system provides the following endpoint:

POST /notification

This endpoint accepts notification data and returns a decision.

How to Run the Project

Install Flask
pip install flask
Run Application
python app.py

Open browser:

http://127.0.0.1:5000
Test API

POST request:

http://127.0.0.1:5000/notification

Example Body:

{
"user_id":1,
"event_type":"message",
"priority_hint":80
}

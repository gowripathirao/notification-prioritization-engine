def decide_notification(data):

    event_type = data.get("event_type", "update")
    priority = data.get("priority_hint", 50)

    if event_type == "security_alert":
        base = 90

    elif event_type == "message":
        base = 70

    elif event_type == "reminder":
        base = 60

    elif event_type == "update":
        base = 40

    elif event_type == "promotion":
        base = 20

    else:
        base = 40

    score = base + (priority/2)

    if score >= 80:

        decision = "NOW"
        reason = "High priority notification"

    elif score >= 50:

        decision = "LATER"
        reason = "Medium priority notification"

    else:

        decision = "NEVER"
        reason = "Low priority notification"



    return decision, score, reason

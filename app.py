from flask import Flask, request, render_template_string
from datetime import datetime, timedelta

app = Flask(__name__)

# HTML template
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>On-Call Rest Period Calculator</title>
</head>
<body>
    <h2>Check 11-Hour Rest Period</h2>
    <form method="post">
        Last on-call end:
        <input type="datetime-local" name="last_end" /><br>
        You want to start the office at:
        <input type="datetime-local" name="next_start" /><br>
        <input type="submit" value="Check and Calculate" />
    </form>
    {% if message %}
    <h3>{{ message }}</h3>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def check_rest_period():
    message = None
    if request.method == "POST":
        last_end_str = request.form["last_end"]
        next_start_str = request.form["next_start"]

        try:
            # Convert to datetime objects
            last_end = datetime.fromisoformat(last_end_str)
            next_start = datetime.fromisoformat(next_start_str)

            # Check if 11-hour rest period is respected
            if next_start - last_end >= timedelta(hours=11):
                message = "11-hour rest period is respected."
            else:
                new_start_time = last_end + timedelta(hours=11)
                message = f"11-hour rest period is not respected. You should start at {new_start_time.isoformat()}. Your inputs were latest on-call: {last_end.isoformat()} | Office start: {next_start.isoformat()}"

        except ValueError:
            message = "Invalid datetime format."

    return render_template_string(TEMPLATE, message=message)


if __name__ == "__main__":
    app.run(debug=True)

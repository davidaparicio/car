import os
from flask import Flask, request, render_template
from datetime import datetime, timedelta
# from rest_period_calculator import calculate_rest_period

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def check_rest_period():
    message = None
    on_call_ends_str = request.form.getlist("on_call_ends[]")
    office_start_str = request.form.get("office_start", "")

    if request.method == "POST":
        try:
            on_call_ends = [
                datetime.fromisoformat(end_str) for end_str in on_call_ends_str
            ]
            office_start = datetime.fromisoformat(office_start_str)

            # Check for the latest on-call end time
            latest_end = max(on_call_ends)

            # Check if the on-call includes weekend
            if any(
                end.weekday() >= 5 for end in on_call_ends
            ):  # 5 and 6 are Saturday and Sunday
                required_rest = timedelta(hours=35)
            else:
                required_rest = timedelta(hours=11)

            # Calculate rest window
            if office_start - latest_end >= required_rest:
                message = f"<p style='color:green;'>Required rest period is respected.</p><br>You can start at {office_start.isoformat()}"
            else:
                new_start_time = latest_end + required_rest
                message = f"<p style='color:red;'>Rest period is not respected.</p><br>You should start at {new_start_time.isoformat()}"

            message += f"<p>Your inputs.</p><p>Latest on-call: {latest_end.isoformat()}</p><p>Office start: {office_start.isoformat()}</p>"

        except ValueError:
            message = "Invalid datetime format."

    # Ensure there's at least one empty field for initial load
    if not on_call_ends_str:
        on_call_ends_str = [""]

    # Pass the input values back to the template
    return render_template(
        "calculate.html",
        message=message,
        on_call_ends=on_call_ends_str,
        office_start=office_start_str,
    )


@app.route("/about/")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    env = os.getenv("ENV", "DEVELOPMENT").upper()
    debug_mode = False if env == "PRODUCTION" else True
    app.run(debug=debug_mode)

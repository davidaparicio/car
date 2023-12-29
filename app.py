import os
from flask import Flask, request, render_template
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from datetime import datetime
from rest_period_calculator import calculate_rest_period

app = Flask(__name__)

if os.getenv("FLASK_ENV") == "production":
    app.config.from_object(ProductionConfig)
elif os.getenv("FLASK_ENV") == "testing":
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(DevelopmentConfig)


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
            latest_end = max(on_call_ends)

            # Use the imported function
            respected, message = calculate_rest_period(on_call_ends, office_start)

            if respected:
                message = f"<p style='color:green;'>{message}</p>"
            else:
                message = f"<p style='color:red;'>{message}</p>"

            message += f"<br><p>Your inputs.</p><p>Latest on-call: {latest_end.isoformat()}</p><p>Office start: {office_start.isoformat()}</p>"

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
    app.run(debug=app.config["DEBUG"])

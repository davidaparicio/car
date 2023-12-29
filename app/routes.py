from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime
from rest_period_calculator import calculate_rest_period

# Create a Blueprint named 'main'
main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
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


@main.route("/about/")
def about():
    return render_template("about.html")


@main.route("/contact/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # name = request.form['name']
        # email = request.form['email']
        # message = request.form['message']

        """subject = f"New contact from {name}"
        message = Message(subject, recipients=['your-receiving-email@example.com'])
        message.body = f"From: {name} <{email}>\n\n{message_body}"

        try:
            mail.send(message)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            flash('Failed to send message. Please try again later.', 'error')
            # Log the exception for debugging """

        flash("Thank you for your message! ", "success")
        return redirect(url_for("main.contact"))

    return render_template("contact.html")

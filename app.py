from flask import Flask, request, render_template_string
from datetime import datetime, timedelta

app = Flask(__name__)

# HTML template
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>On-Call Rest Period Calculator</title>
    <script>
    function addNewField() {
        var container = document.getElementById("on_call_end_times");
        var newFieldDiv = document.createElement("div");

        var newField = document.createElement("input");
        newField.type = "datetime-local";
        newField.name = "on_call_ends[]";

        var deleteButton = document.createElement("button");
        deleteButton.type = "button";
        deleteButton.innerHTML = "Delete";
        deleteButton.onclick = function() { deleteField(this); };

        newFieldDiv.appendChild(newField);
        newFieldDiv.appendChild(deleteButton);
        container.appendChild(newFieldDiv);
    }

    function deleteField(btn) {
        var container = document.getElementById("on_call_end_times");
        if (container.childElementCount > 1) {
            btn.parentElement.remove();
        } else {
            alert("At least one end time must be specified.");
        }
    }
    </script>

</head>
<body>
    <h2>Check Rest Period for On-Call Sessions</h2>
    <form method="post">
        <div id="on_call_end_times">
            {% for end_time in on_call_ends %}
            <input type="datetime-local" name="on_call_ends[]" value="{{ end_time }}" /><br>
            <button type="button" onclick="deleteField(this)">Delete</button>
            {% endfor %}
        </div>
        <button type="button" onclick="addNewField()">Add New Field</button><br><br>
        Office Start Time (YYYY-MM-DDTHH:MM):
        <input type="datetime-local" name="office_start" value="{{ office_start }}" /><br><br>
        <input type="submit" value="Check and Calculate" />
    </form>
    {% if message %}
    <h3>{{ message|safe }}</h3>
    {% endif %}
</body>
</html>
"""


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
                message = f"<p style='color:green;'>Required rest period is respected.</p>You can start at {office_start.isoformat()}"
            else:
                new_start_time = latest_end + required_rest
                message = f"<p style='color:red;'>Rest period is not respected.</p>You should start at {new_start_time.isoformat()}"

            message += f"<p>Your inputs.<br>Latest on-call: {latest_end.isoformat()}<br>Office start: {office_start.isoformat()}</p>"

        except ValueError:
            message = "Invalid datetime format."

    # Ensure there's at least one empty field for initial load
    if not on_call_ends_str:
        on_call_ends_str = [""]

    # Pass the input values back to the template
    return render_template_string(
        TEMPLATE,
        message=message,
        on_call_ends=on_call_ends_str,
        office_start=office_start_str,
    )


if __name__ == "__main__":
    app.run(debug=True)

import os
from flask import Flask, request, render_template_string
from datetime import datetime, timedelta
# from rest_period_calculator import calculate_rest_period

app = Flask(__name__)

# HTML template
TEMPLATE = """
<!DOCTYPE html>
<html data-theme="cupcake">
<head>
    <title>On-Call Rest Period Calculator</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/daisyui@4.4.24/dist/full.min.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
    function addNewField() {
        var container = document.getElementById("on_call_end_times");
        var newFieldDiv = document.createElement("div");
        newFieldDiv.className = "flex items-center mb-4";

        var newField = document.createElement("input");
        newField.type = "datetime-local";
        newField.name = "on_call_ends[]";
        newField.style="display: inline-block; width: auto; vertical-align: middle;"
        newField.className = "input input-bordered input-primary w-full max-w-xs";

        var deleteButton = document.createElement("button");
        deleteButton.type = "button";
        deleteButton.innerHTML = "Delete";
        deleteButton.onclick = function() { deleteField(this); };
        deleteButton.className = "btn btn-secondary";

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
<body class="p-6">
    <h2 class="text-2xl font-bold mb-4">Check Rest Period for On-Call Sessions</h2>
    <form method="post" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div id="on_call_end_times">
            {% for end_time in on_call_ends %}
            <div class="flex items-center mb-4">
                <input type="datetime-local" name="on_call_ends[]" value="{{ end_time }}" style="display: inline-block; width: auto; vertical-align: middle;" class="input input-bordered input-primary w-full max-w-xs" />
                <button type="button" onclick="deleteField(this)" style="display: inline-block; vertical-align: middle;" class="btn btn-secondary">Delete</button>
            </div>
            {% endfor %}
        </div>
        <button type="button" onclick="addNewField()" class="btn btn-primary">Add New Field</button>
        <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="office_start">
                Office Start Time:
            </label>
            <input type="datetime-local" name="office_start" value="{{ office_start }}" class="input input-bordered input-primary w-full max-w-xs" />
        </div>
        <input type="submit" class="btn btn-primary" value="Check and Calculate" />
    </form>
    {% if message %}
    <h3 class="text-xl">{{ message|safe }}</h3>
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
    return render_template_string(
        TEMPLATE,
        message=message,
        on_call_ends=on_call_ends_str,
        office_start=office_start_str,
    )


if __name__ == "__main__":
    env = os.getenv("ENV", "DEVELOPMENT").upper()
    debug_mode = False if env == "PRODUCTION" else True
    app.run(debug=debug_mode)

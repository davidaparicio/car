function addNewField() {
    var container = document.getElementById("on_call_end_times");
    var newFieldDiv = document.createElement("div");
    newFieldDiv.className = "flex items-center mb-4";

    var newField = document.createElement("input");
    newField.type = "datetime-local";
    newField.name = "on_call_ends[]";
    //newField.style="display: inline-block; width: auto; vertical-align: middle;"
    newField.className = "input input-bordered input-primary w-full max-w-xs";

    var deleteButton = document.createElement("button");
    //deleteButton.type = "button";
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

/*function toggleDropdown() {
    var dropdownContent = document.querySelector('.dropdown-content');
    dropdownContent.classList.toggle('hidden');
}*/

// SetTheme
function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    updateTheme();
}

function updateTheme() {
    const theme = localStorage.getItem('theme') || 'light'; // Default to light theme
    document.documentElement.setAttribute('data-theme', theme);
}

// Set the theme on initial load
updateTheme();

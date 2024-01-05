import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import create_app  # noqa: E402

app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])

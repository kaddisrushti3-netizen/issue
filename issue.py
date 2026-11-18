
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")

    # INTENTIONALLY VULNERABLE: CWE-78
    command = f"ping -n 1 {host}"

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    return result.stdout

if __name__ == "__main__":
    app.run(debug=False)

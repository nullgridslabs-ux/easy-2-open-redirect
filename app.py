# easy-2-open-redirect/app.py
from flask import Flask, request, redirect
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
<h2>Support Redirect Service</h2>
<p>Used by support emails and helpdesk links.</p>
<ul>
<li>GET /support/redirect</li>
<li>GET /oauth/callback</li>
<li>GET /health</li>
</ul>
"""

@app.route("/health")
def health():
    return "ok"

@app.route("/support/redirect")
def go():
    target = request.args.get("next","/")
    # BUG: weak validation
    if "company.com" in target:
        return redirect(target)
    return redirect(target)

@app.route("/oauth/callback")
def callback():
    return "CTF{easy_open_redirect}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# easy-2-open-redirect/app.py
from flask import Flask, request, redirect

app = Flask(__name__)

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


import os
import json
import logging
import time

from flask import Flask, redirect, request, render_template, session, url_for, jsonify, Response


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "your-secret-key-at-least-32-chars")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)

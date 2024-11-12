from flask import Flask
import datetime
import os
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your full name
    name = "Gani Nurbhashshaik"
    
    # System username
    username = os.getenv("USER") or os.getenv("USERNAME")
    
    # Server Time in IST
    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    
    # Get Top output
    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <pre><strong>Top Output:</strong>\n{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

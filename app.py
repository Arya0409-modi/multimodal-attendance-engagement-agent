from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Multimodal Attendance & Engagement Agent is active and running!"

if __name__ == '__main__':
    app.run(debug=True)

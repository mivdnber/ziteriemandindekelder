from flask import Flask
import sphere

app = Flask(__name__)

@app.route('/')
def home():
    return 'ja' if sphere.lights_on() else 'waarschijnlijk niet'

if __name__ == '__main__':
    app.run()

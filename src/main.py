from flask import Flask, json

app = Flask(__name__)

@app.route('/profile/capeid/<capeid>')
def construct_url(capeid):
    return json.dumps({'textureURL': f'https://cdn.capeserver.picapes.syanic.org/capes/{capeid}.png'})

if __name__ == '__main__':
    app.run(debug=True)

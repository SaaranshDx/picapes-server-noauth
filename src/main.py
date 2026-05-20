from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/profile/<capeid>')
def construct_url(capeid):
    return jsonify({'textureURL': f'https://cdn.capeserver.picapes.syanic.org/capes/{capeid}.png'})

if __name__ == '__main__':
    app.run(debug=True)

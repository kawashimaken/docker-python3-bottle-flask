# -*- coding: utf-8 -*-
import bottle

app = bottle.app()
#
@app.route('/')
def index():
    return "Hello, World! This is bottle"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

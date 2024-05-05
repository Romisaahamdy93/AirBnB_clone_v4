#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
import uuid
from flask import Flask, render_template
import requests

# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# begin flask page rendering
@app.route('/3-hbnb')
def hbnb_filters():
    """
    handles request to custom template with states, cities & amentities
    """
    cache_id = str(uuid.uuid4())
    return render_template('3-hbnb.html', cache_id=cache_id)


if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)

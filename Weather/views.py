"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, jsonify
from weather_gui import app
import database_queries as dq

@app.route('/')
@app.route('/home')
def home():
    history = []
    saved_results = dq.get_saved_cities()
    city = "Welcome to Weather Search"
    """Renders the home page."""
    return render_template(
        'main.html',
        date = datetime.now().date(),
        city_name = city,
        saved_results = saved_results,
        history = history
    )

@app.route('/get_city')
def get_city():
    city = request.args.get('city_name', "", type=str)
    print(city)
    return jsonify(city_name=city)

@app.route('/settings')
def settings():
    return "Put settings page here"
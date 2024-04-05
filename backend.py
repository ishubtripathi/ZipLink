from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
import random
import string

app = Flask(__name__)
CORS(app)

# Dictionary to store mappings between short codes and original URLs
url_mapping = {}

# Function to generate a random shortcode
def generate_shortcode():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

# API endpoint to shorten a URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()  # Get JSON data from the request
    original_url = data.get('url')  # Extract the URL from the JSON data

    if not original_url:
        return jsonify({'error': 'URL is required'}), 400  # Return error if URL is not provided

    shortcode = generate_shortcode()  # Generate a shortcode
    url_mapping[shortcode] = original_url  # Store the mapping

    shortened_url = f"http://127.0.0.1:5000/{shortcode}"  # Construct the shortened URL
    return jsonify({'shortcode': shortcode, 'shortened_url': shortened_url}), 201  # Return JSON response with shortened URL

# Route to handle redirection for shortened URLs
@app.route('/<shortcode>')
def redirect_to_original(shortcode):
    original_url = url_mapping.get(shortcode)
    if original_url:
        return redirect(original_url)
    else:
        return jsonify({'error': 'Shortened URL not found'}), 404

# Route to handle root URL
@app.route('/')
def index():
    return 'Welcome to the URL Shortener'

if __name__ == '__main__':
    app.run(debug=True)

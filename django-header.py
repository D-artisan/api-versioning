from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.before_request
def detect_version():
    accept = request.headers.get('Accept', '')
    # regex to extract version after 'version=' parameter
    match = re.search(r'version\s*=\s*([\d.]+)', accept)
    request.api_version = match.group(1) if match else '1'
    
@app.route('/api/users')
def get_users():
    version = request.api_version
    if version == '1':
        return jsonify({"users": ["Mike", "Larson"], "version": 1})
    elif version == '2':
        return jsonify({"users": ["Mike", "Larson", "Peter"], "version": 2})
    else:
        return jsonify({"error": "Unsupported version"}), 400

if __name__ == '__main__':
    app.run(debug=True)
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.before_request
def detect_version():
    accept = request.headers.get('Accept', '')
    # look for pattern like application/vnd.myapp.v<version>+json
    match = re.search(r'v(\d+)\+json', accept)
    request.api_version = match.group(1) if match else '1'
    
@app.route('/api/items')
def items():
    version = request.api_version
    if version == '1':
        return jsonify({"items": ["item1", "item2"], "version": 1})
    elif version == '2':
        return jsonify({"items": ["item1", "item2", "item3"], "version": 2})
    else:
        return jsonify({"error": "Unsupported version"}), 400

if __name__ == '__main__':
    app.run(debug=True)
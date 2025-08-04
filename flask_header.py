from flask import Flask, request, jsonify

app = Flask(__name__)

@app.before_request
def detect_version():
    # read custom header, default to v1
    request.api_version = request.headers.get('X-API-Version', '1')
    
@app.route('/api/users')
def get_users():
    version = request.api_version
    if version == '1':
        return jsonify({"users": ["Alice", "Bob"], "version": 1})
    elif version == '2':
        return jsonify({"users": ["Alice", "Bob", "Charlie"], "version": 2})
    else:
        return jsonify({"error": "Unsupported version"}), 400

if __name__ == '__main__':
    app.run(debug=True)
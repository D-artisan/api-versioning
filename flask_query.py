from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/users')
def users():
    # default to version 1 if not specified
    version = request.args.get('version', '1')
    if version == '1':
        # version 1 logic
        return jsonify({"users": ["Alice", "Bob"], "version": "1"})
    elif version == '2':
        # version 2 logic
        return jsonify({"users": ["Alice", "Bob", "Charlie"], "version": "2"})
    else:
        return jsonify({"error": "Unsupported version"}), 400
    
if __name__ == '__main__':
    app.run(debug=True)

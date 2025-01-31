from flask import Flask, jsonify
from datetime import datetime
import pytz
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/', methods=["GET"])
def get_info():
    try:
        return jsonify({
            "email": "ruthambogo.ra@gmail.com",
            "current_datetime": datetime.now().isoformat() + "Z",
            "github_url": "https://github.com/Ambogo2/hng12-stage0-api"
        }), 200
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

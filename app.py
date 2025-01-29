from flask import Flask, jsonify
from datetime import datetime
import pytz
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/', methods=["GET"])
def get_info():
    return jsonify({
        "email": "ruthambogo.ra@gmail.com",
        "current_datetime": datetime.now(pytz.UTC).isoformat(),
        "github_url": "https://github.com/Ambogo2/hng12-stage0-api.git"
    }
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

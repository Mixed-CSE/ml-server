from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # JSON 데이터를 받음
        json_data = request.get_json()

        # 받은 JSON 데이터를 출력
        print("Received JSON data:", json_data)

        # 받은 JSON 데이터를 그대로 반환
        return jsonify(json_data), 200

    except Exception as e:
        # 예외가 발생할 경우 에러 메시지와 함께 500 Internal Server Error 반환
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8104, debug=True)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    userid = data.get('userid')
    courseid = data.get('courseid')

    # Đây là nơi bạn có thể chèn mô hình AI thực sự, ở đây trả về giả định
    return jsonify({
        'suggestion': f'Học viên {userid} nên ôn lại phần khó trong khóa học {courseid}.'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    userid = data.get('userid')
    courseid = data.get('courseid')
    topic = data.get('topic', '').strip()

    if topic:
        suggestion = f"Học viên {userid} nên ôn lại chủ đề: '{topic}' trong khóa học {courseid}."
    else:
        suggestion = f"Học viên {userid} nên ôn lại phần khó trong khóa học {courseid}."

    return jsonify({'suggestion': suggestion})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    grades = data.get('grades', [])
    completions = data.get('completions', [])

    suggestions = []

    if grades and min(grades) < 6.0:
        suggestions.append("Ôn lại các chủ đề có điểm dưới 6.0")

    if completions.count(False) > 0:
        suggestions.append("Hoàn thành các chủ đề còn bỏ sót")

    if not suggestions:
        suggestions.append("Bạn đang học tốt, tiếp tục phát huy!")

    return jsonify({'suggestion': ' - '.join(suggestions)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

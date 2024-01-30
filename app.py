# Flaskをインストール
# pip install flask

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 質問と回答のリスト
questions = [
    "1. あなたはどの気候が好きですか？",
    "2. 人とのコミュニケーションは得意ですか？",
    "3. 仕事と生活のどちらを優先させたいですか？",
    "4. 都市部と田舎のどちらが好きですか？",
    "5. 移住先での生活スタイルはどのようなものが好きですか？"
]

# 質問の回答に基づいて移住タイプを診断する関数
def diagnose(answer_list):
    score = 0
    for answer in answer_list:
        score += int(answer)

    if score <= 5:
        return "都市派"
    elif score <= 10:
        return "自然派"
    else:
        return "冒険派"

# ホームページ
@app.route('/')
def home():
    return render_template('index.html', questions=questions)

# 診断結果を表示するページ
@app.route('/result', methods=['POST'])
def result():
    answers = [request.form[f'q{i}'] for i in range(1, 6)]
    result = diagnose(answers)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

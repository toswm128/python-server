from flask import *
app = Flask(__name__)

@app.route('/')
def main():    
    return render_template('index.html')

# 로그인 페이지
@app.route('/login')
def login():
    return render_template('login.html')

# 로그인 폼 전송을 했을때 실행될 함수
@app.route('/login', methods=['POST'])
def result():
#     #TODO: request.values 에서 폼에서 입력한 값을 가지고 오기
      result = requset.form
      return render_template('loginedHome.html')
#     #TODO: DB에서 확인
    
#     #TODO: 아이디,비밀번호가 맞으면
#     #     세션에 사용자 정보를 넣고
#     #     메인페이지로 이동
#     # 계정 정보가 안 맞다면
#     # login.html을 다시 표시하되, 에러메시지를 포함
    
    #  return render_template('index.html')

# # 회원가입 페이지
@app.route('/join')
def join():
    return render_template('join.html')


# 내장 웹서버 실행, 코드의 가장 마지막 줄에 있어야 함
# host='0.0.0.0': 다른 컴퓨터에서도 접속할 수 있도록 설정 / port=5000: 웹 서버를 5000포트에 실행
app.run(host='0.0.0.0', port=5000, debug=True)
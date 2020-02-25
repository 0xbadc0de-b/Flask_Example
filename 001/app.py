from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)
 
@app.route('/')
@app.route('/<int:num>')	# 주소창에 localhost:5000/3 처럼 3을 직접 입력해도 동작함
def inputTest(num=None):
    return render_template('main.html', num=num)

@app.route('/calculate', methods=['POST'])
def calculate(num=None):
    if request.method == 'POST':
        temp = request.form['num']
    else:
        temp = None
    return redirect(url_for('inputTest', num=temp))
    
if __name__ == '__main__':
    app.run()

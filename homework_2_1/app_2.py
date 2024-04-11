from flask import Flask, request, render_template, redirect, make_response

app = Flask(__name__)

# Главная страница с формой
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Извлекаем данные из формы
        name = request.form['name']
        email = request.form['email']
        
        # Создаем ответ и устанавливаем в нем cookie
        resp = make_response(redirect('/welcome'))
        resp.set_cookie('name', name)
        resp.set_cookie('email', email)

        return resp

    # Если GET, просто отображаем форму
    return render_template('index.html')

# Страница приветствия
@app.route('/welcome')
def welcome():
    # Извлекаем имя из cookie
    name = request.cookies.get('name')
    if not name:
        return redirect('/')
    return render_template('welcome.html', name=name)

# Выход пользователя
@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('name', '', expires=0)
    resp.set_cookie('email', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
"""
Написать функцию, которая будет выводить на экран HTML
страницу с блоками новостей.
Каждый блок должен содержать заголовок новости,
краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через
контекст.
"""


from collections import namedtuple

from flask import Flask
from flask import render_template

app = Flask(__name__)

Student = namedtuple('Student', 'name surname age point_avg')


@app.route('/')
def index():
    context = {
        'students': [
            Student('Ulyana', 'Volchik', '16', '100'),
            Student('Denis', 'Karpovich', '20', '100'),
            Student('Ivan', 'Ivanov', '25', '100'),
        ]
    }
    return render_template('index6.html', **context)


if __name__ == '__main__':
    app.run()
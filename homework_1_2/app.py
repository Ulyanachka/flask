from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/category/<category_name>')
def show_category(category_name):
    return render_template('category.html', category_name=category_name)

@app.route('/product/<int:product_id>')
def show_product(product_id):
    # Здесь должен быть код для извлечения данных продукта из базы данных или файла
    product = {'id': product_id, 'name': 'Куртка', 'price': '4999.99'}
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request  # подключаем render_template, который включает функции для Jinja
import pickle

with open('model', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)


@app.route("/")
def render_index():
    output = render_template("index.html")  # рендерим шаблон
    return output  # возвращаем то, что отрендерилось


@app.route("/predict/", methods=["POST"])
def render_predict():
    age = request.form["age"]
    fare = request.form["fare"]
    sex = request.form['sex']

    try:
        if float(age) and float(fare) and sex is not None:
            age = (float(age) - 29.7) / 13.2
            fare = (float(fare) - 32.2) / 49.7
            sex = list(map(lambda x: float(x), sex.split()))
            result = list([age, fare, sex[0], sex[1]])

            prediction = model.predict([result])

            output = render_template("predict.html", prediction=prediction[0])
            return output
    except ValueError:
        output = render_template("error.html")
        return output


if __name__ == '__main__':
    # app.run(debug=True)  # ! while development
    app.run()  # production

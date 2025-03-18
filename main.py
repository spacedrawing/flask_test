from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/fun")
def fun():
    names = ["Маша", "Петя", "Вася", "Катя", "И", "fynjy", "efhuob", "wedwe", "ewedew"]
    x = [
        f"<h{i}>{name}</h{i}>" if i <= 6 else f"<h6>{name}</h6>"
        for i, name in enumerate(names, 1)
    ]
    return "<br>".join(x)


@app.route("/image")
def image():
    return f"""<img src="{url_for('static', filename='img/riana.png')}"
           alt="здесь должна была быть картинка, но не нашлась">"""


@app.route("/promotion")
def promotion():
    promot = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!",
    ]
    print("</br>".join(promot))

    return "</br>".join(promot)


@app.route("/image_mars")
def image_mars():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Привет, Марс!</title>
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="https://i.imgflip.com/s0dgo.jpg" alt="Тут был марс">
    <p>Тут что-то было</p>
</body>
</html>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Привет, Марс!</title>
    <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
    <h1>Жди нас, Марс!</h1>
    <img src="https://i.imgflip.com/s0dgo.jpg" alt="Тут был марс">
    <p class="black">Человечество вырастает из детства.</p>
    <p class="green">Человечеству мала одна планета.</p>
    <p class="black">Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p class="yellow">И начнем с Марса!</p>
    <p class="red">Присоединяйся!</p>
</body>
</html>"""


@app.route("/astronaut_selection")
def astronaut_selection():
    return render_template("astronaut_selection.html")


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

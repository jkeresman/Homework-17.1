from flask import Flask, request, make_response, render_template
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":

        response = make_response(render_template("index.html"))

        if not request.cookies.get("secret_number"):
            response.set_cookie("secret_number", str(random.randint(1, 30)))

        return response

    elif request.method == "POST":

        player_guess = int(request.form.get("player-guess"))
        secret_number = int(request.cookies.get("secret_number"))

        response = make_response(render_template("play_again.html",
                                                 player_guess=player_guess,
                                                 secret_number=secret_number,
                                                 ))

        if player_guess == secret_number:
            response.set_cookie("secret_number", str(random.randint(1, 30)))

        return response


if __name__ == "__main__":
    app.run(use_reloader=True)

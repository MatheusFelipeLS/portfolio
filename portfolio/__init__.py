from flask import Flask, render_template, abort

def create_app():

    app = Flask(__name__)

    projects = [
        {
            "name": "Robô que escreve com uso de Visão computacional",
            "thumb": "img/ugo/ugo_logo.png",
            "hero": "img/ugo/ugo2.jpeg",
            "categories": ["C++", "Arduino"],
            "slug": "UG0",
            "prod": "https://github.com/MatheusFelipeLS/UG0",
        },
        {
            "name": "APHID: Aplicação de prensa hidráulica",
            "thumb": "img/aphid/aphid-thumb.png",
            "hero": "img/aphid/aphid-inicio.png",
            "categories": ["python"],
            "slug": "APHID",
            "prod": "https://github.com/MatheusFelipeLS/Aplicativo-Prensa-Hidraulica",
        },
        {
            "name": "Jogo de memorização com cores",
            "thumb": "img/luzes/luzes-thumb.png",
            "hero": "img/luzes/luzes_gameplay.png",
            "categories": ["Python"],
            "slug": "luzes",
            "prod": "https://github.com/MatheusFelipeLS/Jogo-de-memorizacao-de-cores",
        }
    ]

    slug_to_project = {project["slug"]: project for project in projects}

    @app.route("/")
    def home():
        return render_template("home.html", projects=projects)


    @app.route("/about")
    def about():
        return render_template("about.html")


    @app.route("/contact")
    def contact():
        return render_template("contact.html")


    @app.route("/project/<string:slug>")
    def project(slug):
        if slug not in slug_to_project:
            abort(404)
        return render_template(f"project_{slug}.html", project=slug_to_project[slug])


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404
    
    
    return app
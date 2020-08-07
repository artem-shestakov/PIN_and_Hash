from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# Create blueprint
main_blueprint = Blueprint(
    "main",
    __name__,
    template_folder="../templates/main",
)


# Route for index page
@main_blueprint.route("/")
def index():
    try:
        return render_template("index.html", title="Main page")
    except TemplateNotFound:
        abort(404)

import flask

from infrastructure.view_modifiers import response
import services.package_service as package_service

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
# @response(template_file='packages/details.html')
def package_details(package_name: str):
    return "Packages details for {}".format(package_name)
    # return flask.render_template('home/index.html', packages=test_packages)


@blueprint.route('/<int:rank>')
def popular(rank: int):
    return "The details for the {}th most popular package".format(rank)

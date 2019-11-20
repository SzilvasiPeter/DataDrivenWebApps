import os
import sys

import flask

from pypi_org.nosql import mongo_setup
from pypi_org.nosql.users import User

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)
import pypi_org.data.db_session as db_session

app = flask.Flask(__name__)


def main():
    register_blueprints()
    setup_db()
    app.run(debug=True, port=5006)


def configure():
    print("Configuring Flask apps:")

    register_blueprints()
    print("Setup blueprints completed")
    setup_db()
    print("DB setup completed")
    print("", flush=True)


def setup_db():
    mongo_setup.global_init()

    # Run only once because the email has to be unique
    user = User()
    user.name = 'Peter Szilvasi'
    user.email = 'peti.szilvasi95@gmail.com'

    user.save()
    # db_file = os.path.join(
    #     os.path.dirname(__file__),
    #     'db',
    #     'pypi.sqlite')
    #
    # db_session.global_init(db_file)


def register_blueprints():
    from pypi_org.views import home_views
    from pypi_org.views import package_views
    from pypi_org.views import cms_views
    from pypi_org.views import account_views
    from pypi_org.views import seo_views

    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(account_views.blueprint)
    app.register_blueprint(cms_views.blueprint)
    app.register_blueprint(seo_views.blueprint)


if __name__ == '__main__':
    main()
else:
    configure()

import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'runmetric.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Database initialization
    from . import db
    db.init_app(app)

    # @app.route('/')
    # def index():
    #     return 'Index Page'

    # A simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Register auth blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    # Register activities blueprint
    from . import activities
    app.register_blueprint(activities.bp)

    # Register runs blueprint
    from . import runs
    app.register_blueprint(runs.bp)
    app.add_url_rule('/', endpoint='index')

    # Register shoes blueprint
    from . import shoes
    app.register_blueprint(shoes.bp)

    return app
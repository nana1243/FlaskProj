
from flask import Flask
from backend.api.config.config import ProductionConfig,DevelopmentConfig,TestingConfig
from backend.api.utils.database import db
import os


def create_app(test_config=None):  # 1)
    app = Flask(__name__)

    # config
    if os.environ.get('WORK_ENV') == 'PROD':
        app_config = ProductionConfig
    elif os.environ.get('WORK_ENV') == 'TEST':
        app_config = TestingConfig
    else:
        app_config = DevelopmentConfig
    app.config.from_object(app_config)

    # db
    db.init_app(app)
    with app.app_context():
        db.create_all()



    #routes
    @app.route("/")
    def main():
        return "main"


    # app.register_blueprint(product_routes, url_prefix='/api/products')
    # app.register_blueprint(product_routes, url_prefix='/api/board')

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
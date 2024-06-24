from flask import Flask
from models.models import db, login_manager

root = Flask(__name__)
root.config['UPLOAD_FOLDER'] = "static"
root.config["SECRET_KEY"] = "942acc9ac21231fa1872f963"
root.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://akbarov:akbarov@localhost:5432/logist_smart"

db.init_app(root)
login_manager.init_app(root)

with root.app_context():
    db.create_all()

if __name__ == "__main__":
    from routes.main_route import *
    from routes.offer_route import *
    from routes.student_route import *
    from routes.reception_route import *
    from routes.promo_code_route import *
    root.register_error_handler(404, page_not_found)
    root.register_error_handler(401, unauthorized)
    root.run(debug = True)
    # from waitress import serve
    # serve(root, host="192.168.1.110", port=8080)

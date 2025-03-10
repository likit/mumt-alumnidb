import os
from pytz import timezone

from flask import Flask, url_for, redirect
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin, AdminIndexView
from dotenv import load_dotenv
from flask_wtf import CSRFProtect
from flask_login import LoginManager, current_user

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('://', 'ql://', 1)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('main.login'))


db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app, index_view=MyAdminIndexView())
csrf = CSRFProtect(app)
login_manager = LoginManager(app)

login_manager.login_view = 'main.login'

from app.main import main_blueprint

app.register_blueprint(main_blueprint)
from app.main.models import User

admin.add_view(ModelView(User, db.session, category='User'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


from app.member import member_blueprint

app.register_blueprint(member_blueprint)

from app.member.models import MemberInfo

admin.add_view(ModelView(MemberInfo, db.session, category='Member'))

from app.event import event_blueprint

app.register_blueprint(event_blueprint)

from app.event.models import Event, EventParticipant, EventTicket, EventTicketPayment

admin.add_view(ModelView(Event, db.session, category='Event', endpoint='event-admin'))
admin.add_view(ModelView(EventParticipant, db.session, category='Event'))
admin.add_view(ModelView(EventTicket, db.session, category='Event'))
admin.add_view(ModelView(EventTicketPayment, db.session, category='Event'))

from app.line_api import line_api_blueprint

app.register_blueprint(line_api_blueprint)


@app.template_filter("localdatetime")
def local_datetime(dt, dateonly=False):
    bangkok = timezone('Asia/Bangkok')
    datetime_format = '%d/%m/%y' if dateonly else '%d/%m/%Y %X'
    if dt:
        if dateonly:
            return dt.strftime(datetime_format)
        else:
            if dt.tzinfo:
                return dt.astimezone(bangkok).strftime(datetime_format)
    else:
        return None

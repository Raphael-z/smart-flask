#coding:utf8

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import flask_restful as restful


app = Flask(__name__)
api = restful.Api(app)
# 用于wtf.quick_form()模版渲染
bootstrap = Bootstrap(app)


app.config.from_object('app_config')
app.secret_key = os.environ.get('CLIENT_SECRET','gg3IK199lZ1KVf8MPlzL0dSSpF2OZ2Y7')
db = SQLAlchemy(app)



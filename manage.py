from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


class Config(object):
    '''项目配置'''
    DEBUG = True
    '''为mysql添加配置'''
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/infomation27'

app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()

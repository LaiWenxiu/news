from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask,session
from flask.ext.sqlalchemy import SQLAlchemy
# 可以用来指定session的存储位置
from flask_session import Session


class Config(object):
    '''项目配置'''
    DEBUG = True
    SECRET_KEY ='3pVtH9YW8HihLCukPZdlUukiTu4UnlJJG6q+zeoZKv0dyLNrtuYwxnMP3yK77QG'
    # 为mysql添加配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/infomation27'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis的配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # 指定session保存在redis里面
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # session保存配置
    SESSION_TYPE = 'redis'
    # 是否开启签名
    SESSION_USE_SIGNER = True
    # 是否过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


app = Flask(__name__)
# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(port=Config.REDIS_PORT, host=Config.REDIS_HOST)
# 开启当前项目CSRF保护,只做服务器验证功能
CSRFProtect(app)
#  设置session指定位置
Session(app)


@app.route('/')
def index():
    session['name'] = 'haha'
    return 'index'


if __name__ == '__main__':
    app.run()

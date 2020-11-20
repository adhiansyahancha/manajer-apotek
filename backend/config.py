import os

pwd = os.path.abspath(os.path.dirname(__file__))

class DefaultConfig(object):
    # Kunci rahasia sebaiknya buat sendiri daripada menggunakan di bawah ini
    SECRET_KEY = 'OuPbf-jKvFlH-K4-EB8GRCcHpOwp6aXWemuEIEvh3CGnNoabHW1nEFWZMXwbEL5bgYugNPpgvOd-\
        ZJ8qxeucjd36vGUhuMLg5m9sCbk1GNoqLhW-mEZsba5-mOB00QHKaaaCNsg2r98uObsOnmhN2IwNceC8pv3BetZNqsddaTI'
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(pwd, 'apotek.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

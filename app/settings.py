import os

BOOTSTRAP_SERVE_LOCAL = True
MAX_CONTENT_LENGTH = 100 * 1024
BATCH_SIZE = 20 #1000
SENT_LEN_LIMIT=500
#CSRF prevention
SECRET_KEY = (os.environ.get('SECRET_KEY') or
              b'\x0c\x11{\xd3\x11$\xeeel\xa6\xfb\x1d~\xfd\xb3\x9d\x11\x00\xfb4\xd64\xd4\xe0')
#DEFAULT_SERVER = 'localhost:9000'
DEFAULT_SERVER = '10.10.51.30:9000'
T2T_TRANSFORMER2 = '10.10.51.31:9000'


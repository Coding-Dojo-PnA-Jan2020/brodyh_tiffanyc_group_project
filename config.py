DEBUG = True

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/order_application'
SQLALCHEMY_TRACK_MODIFICATIONS = False

BOOTSTRAP_SERVE_LOCAL = True

CSRF_ENABLED = True
CSRF_SESSION_KEY = "9.m+%BY9A?Spn;k`ZQ/(J)ercj>yrYs?6+)C/@.2v'Un$j*s*Nr+,grV-qqhpfBrZ,f/C[Dc]JbF,>>4a:}4>]w5V\-U=@-R>^'DuVyfT7;vaPbTV,2+@wx7+*u-VD%k"
SECRET_KEY = "2N`Z@Hc>^Zt@DvGLPf;6JwT?tH3r%d@fj=@?K9,Pqb:JMmp~K<=8yPTxF6K*7;>s\s(MBs8MvwX=;GLn{)(-;$V&aXBq=X[W.{X-RZBjH/][Qm`C^`[^!>NNUj*t&!]6"

UPLOADS_DEFAULT_DEST = BASE_DIR + '/app/static/uploads/'
UPLOADS_DEFAULT_URL = 'http://localhost:8000/static/uploads/'
 
UPLOADED_IMAGES_DEST = BASE_DIR + '/app/static/uploads/'
UPLOADED_IMAGES_URL = 'http://localhost:8000/static/uploads/'
from .production import * # when in production mode

try:
  from .local import *
except expression as identifier:
   pass

#remember to push to heroku only the production part , the local will bring errors
from .production import * # when in production mode

<<<<<<< HEAD
#try:
# from .local import *
#except expression as identifier:
#   pass
=======
try:
  from .local import *
except expression as identifier:
   pass
>>>>>>> 817c16378e17c1e28aeb8a86668527fe3c51c004

#remember to push to heroku only the production part , the local will bring errors
import logging

LoggerFormat = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig (filename = "log my data.log", level="DEBUG")

logging.info ("my logger file")
logging.debug ("why did I tell the logger to warn me about telling the logger to warn me")
logging.warning ("why did you put warning here, also why did you put an error on line 11 and a critical on line 12")
logging.error ("error")
logging.critical ("critical")

try :
  print(0/0) # code to cause error so logging picks up on it

except error as e:
  logging.error (e)

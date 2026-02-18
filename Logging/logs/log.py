import logging
logging.basicConfig(
   filename='app.log',filemode='w', level=logging.DEBUG,format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",datefmt='%y-%m-%d %H:%M:%S',force=True)

logging.debug("this is a debug message")
logging.info("thiss is ingo messgae ")
logging.warning(" this is warning messgae")
logging.error("this is error ")
logging.critical(" critical")
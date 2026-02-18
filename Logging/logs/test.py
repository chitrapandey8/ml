from log import logging

def add(a,b):
    logging.debug("IDDD")
    return a+b

logging.debug("EE")
print(add(10,10))
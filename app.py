from flask import Flask
import logging as logger

logger.basicConfig(level="DEBUG")


flaskAppInstance = Flask(__name__)

if __name__ == '__main__':
    logger.debug("Starting Music API")
    from Api import *
    flaskAppInstance.run(host="0.0.0.0", port="9000",
                         debug=True, use_reloader=True)

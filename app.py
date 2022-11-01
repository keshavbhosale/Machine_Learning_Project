from flask import Flask
import sys
import housing
from housing.logger import logging
from housing.exception import Housing_Exception
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logger ")
    return 'Starting machine learning project'


if __name__=="__main__":
    app.run(debug=True)
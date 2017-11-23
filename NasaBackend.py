"""
Author: Evan Putnam
Description: Flask app to send nasa image of day for / command on slack
Pre-Reqs:
    Nasa python api https://github.com/brendanv
    Flask
Language: Python3
"""
from flask import Flask, jsonify
import os
from nasa import apod
import datetime

app = Flask(__name__)

def nasaGet():
    '''
    Need to have your api key in the environment variables like so
        NASA_API_KEY : someRandomStringOfCharsAndNumbers
    Gets the date and tries to get the image
    :return: json with file information
    '''

    #Gets the current date
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    day = date.day
    #Gets it in string format
    date = str(year)+"-"+str(month)+"-"+str(day)
    try:
        image = apod.apod(date)
        return jsonify(
            {
                'attachments': [
                {
                    'image_url': image.url,
                    'title' : image.title,
                    'text' : image.explanation
                }
                ]
            }
        )

    except:
        return "Failed to get image"



@app.route('/nasaimage', methods=['POST', 'GET'])
def getImage():
    '''
    Gets the nasa image file in a json format that slack understands
    :return:
    '''
    return nasaGet()



if __name__ == '__main__':
    #Change the port if you want...
    port = int(os.environ.get('PORT', 5000))
    #Have it set to debug and localhost but you can change that as needed
    app.run(host='0.0.0.0',port=port, debug=True)



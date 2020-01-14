import logging
import pprint

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session, context, version

from ask_sdk_model.services.api_configuration import ApiConfiguration
from ask_sdk_model.services.api_client import ApiClient

from ask_sdk_model.services.serializer import Serializer
from ask_sdk_model.services.api_client import ApiClient

app = Flask(__name__)

ask = Ask(app, "/")

# log = logging.getLogger("flask_ask").setLevel(logging.DEBUG)
logging.basicConfig(level=logging.INFO)


@ask.launch
def new_game():
    logging.info("Session New?: {}".format(session.new))
    logging.info("User ID: {}".format(session.user.userId))
    logging.info("Alexa Version: {}".format(version))
    logging.info("Device ID: {}".format(context.System.device.deviceId))
#     logging.info("Device: {}".format(context.System.device.keys()))
    logging.info("System: {}".format(context.System))
#     pprint.pprint(context.System)
    pprint.pprint(context)
    print("User: {}".format(context.System.user))
    print("API: {}".format(context.System.apiAccessToken))
    return question("Welcome to lefotver label. First item?")


@ask.intent("GlobalIntent", convert={"item": str})
def main_intent(item):
    print("Item was: {}".format(item))
    print("Access token: {}".format(context.System.apiAccessToken))
    pprint.pprint(context)
    return question("I think you said {}".format(item))


@ask.session_ended
def session_ended():
    logging.info("Session ended!")
    logging.info("Session New?: {}".format(session.new))
    logging.info("User ID: {}".format(session.user.userId))
    logging.info("Alexa Version: {}".format(version))
    logging.info("Device ID: {}".format(context.System.device.deviceId))
    return question("I think we are done!")
    return "{}", 200

if __name__ == '__main__':
    app.run(debug=True, port=8050)

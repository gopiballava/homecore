
import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session, context, version

from labeler import Labeler

app = Flask(__name__)

ask = Ask(app, "/")

labeler = Labeler()


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
    print("User: {}".format(context.System.user))
    return labeler.get_intro_statement()


@ask.intent("GlobalIntent", convert={"item": str})
def main_intent(item):
    logging.info("User ID: {}".format(session.user.userId))
    logging.info("Device ID: {}".format(context.System.device.deviceId))
    print("Main intent item: {}".format(item))
    return labeler.handle_statement(item)


@ask.intent("AMAZON.StopIntent")
def stop_intent():
    print("************ STOP intent")
    logging.info("User ID: {}".format(session.user.userId))
    logging.info("Device ID: {}".format(context.System.device.deviceId))
    return statement("Thank you for labeling your food!")


@ask.session_ended
def session_ended():
    print("************** SESSION DONE")
    logging.info("Session ended!")
    logging.info("Session New?: {}".format(session.new))
    logging.info("User ID: {}".format(session.user.userId))
    logging.info("Alexa Version: {}".format(version))
    logging.info("Device ID: {}".format(context.System.device.deviceId))
    return "{}", 200


if __name__ == '__main__':
    app.run(debug=True, port=8050)

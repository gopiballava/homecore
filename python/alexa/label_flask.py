import logging
import pprint

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session, context, version

<<<<<<< HEAD
from ask_sdk_model.services.reminder_management.reminder_management_service_client import ReminderManagementServiceClient
=======
>>>>>>> 77e968bfaf731a23d072818f9863a0593a881c91
from ask_sdk_model.services.api_configuration import ApiConfiguration
from ask_sdk_model.services.api_client import ApiClient

from ask_sdk_model.services.serializer import Serializer
from ask_sdk_model.services.api_client import ApiClient

app = Flask(__name__)

ask = Ask(app, "/")

<<<<<<< HEAD
#log = logging.getLogger("flask_ask").setLevel(logging.DEBUG)
logging.basicConfig(level=logging.INFO)

def test_create():
    print("Endpoint: {}".format(context.System.apiEndpoint))
    apconf = ApiConfiguration(
        authorization_value=context.System.apiAccessToken,
        api_endpoint=context.System.apiEndpoint,
        serializer=Serializer,
        api_client=ApiClient(),
        )
    rsc = ReminderManagementServiceClient(apconf)
#     rsc._authorization_value = context.System.apiAccessToken
    print("All reminders: {}".format(rsc.get_reminders()))
    rsc.create_reminder()

import httplib, urllib
import json
def test_list():
    bearer_api_key = context.System.apiAccessToken
    conn = httplib.HTTPSConnection("api.amazonalexa.com")
    headers = {"Authorization": "bearer {}".format(bearer_api_key)}
    params = {}
    conn.request("GET", "/v1/alerts/reminders", params, headers)
    response = conn.getresponse()
    print("Status", response.status, response.reason)
    print("Contents: {}".format(response.read()))

def test_add():
    bearer_api_key = context.System.apiAccessToken
    conn = httplib.HTTPSConnection("api.amazonalexa.com")
    headers = {
        "Authorization": "bearer {}".format(bearer_api_key),
        "Content-Type": "application/json",
        }
    params = json.dumps({
   "requestTime" : "2019-09-22T19:04:00.672",
   "trigger": {
        "type" : "SCHEDULED_RELATIVE",
        "offsetInSeconds" : "60"
   },
   "alertInfo": {
        "spokenInfo": {
            "content": [{
                "locale": "en-US", 
                "text": "walk the dog"
            }]
        }
    },
    "pushNotification" : {                            
         "status" : "ENABLED"         
    }
    })
    conn.request("POST", "/v1/alerts/reminders/", params, headers)
    response = conn.getresponse()
    print("Status", response.status, response.reason)
    print("Contents: {}".format(response.read()))

def test_req():
    test_add()
    test_list()


@ask.launch
def new_game():
#     welcome_msg = render_template('welcome')
#     logging.info("Request ID: {}".format(request.requestId))
#     logging.info("Request Type: {}".format(request.type))
#     logging.info("Request Timestamp: {}".format(request.timestamp))
=======
# log = logging.getLogger("flask_ask").setLevel(logging.DEBUG)
logging.basicConfig(level=logging.INFO)


@ask.launch
def new_game():
>>>>>>> 77e968bfaf731a23d072818f9863a0593a881c91
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
<<<<<<< HEAD
#THis workds    test_req()
#     test_create()
#     logging.info("Consent Token: {}".format(context.System.user.permissions.consentToken))
    return question("Would you like some toast?") \
          .simple_card(title='CATS says...', content='Make your time')
# 
#             .standard_card(title='CATS says...',
#                        text='Make your time',
#                        small_image_url='https://example.com/small.png',
#                        large_image_url='https://example.com/large.png')



# @ask.default_intent(convert={"first": str})
# def default(first):
# #     logging.info("Request ID: {}".format(request.requestId))
# #     logging.info("Request Type: {}".format(request.type))
# #     logging.info("Request Timestamp: {}".format(request.timestamp))
# #     logging.info("Session New?: {}".format(session.new))
# #     logging.info("User ID: {}".format(session.user.userId))
# #     logging.info("Alexa Version: {}".format(version))
# #     logging.info("Device ID: {}".format(context.System.device.deviceId))
# #     logging.info("Consent Token: {}".format(context.System.user.permissions.consentToken))
#     return question("I think you said {}".format(first))
=======
    return question("Welcome to lefotver label. First item?")

>>>>>>> 77e968bfaf731a23d072818f9863a0593a881c91

@ask.intent("GlobalIntent", convert={"item": str})
def main_intent(item):
    print("Item was: {}".format(item))
    print("Access token: {}".format(context.System.apiAccessToken))
    pprint.pprint(context)
<<<<<<< HEAD
    
#This workds    test_req()
    return question("I think you said {}".format(item))
#     return question("Is that main?")

# @ask.intent("YesIntent")
# 
# def next_round():
# 
#     numbers = [randint(0, 9) for _ in range(3)]
# 
#     round_msg = render_template('round', numbers=numbers)
# 
#     session.attributes['numbers'] = numbers[::-1]  # reverse
# 
#     return question(round_msg)
# 
# 
# @ask.intent("AnswerIntent", convert={'first': int, 'second': int, 'third': int})
# 
# def answer(first, second, third):
# 
#     winning_numbers = session.attributes['numbers']
# 
#     if [first, second, third] == winning_numbers:
# 
#         msg = render_template('win')
#     else:
#         msg = render_template('lose')
#     return statement(msg)
=======
    return question("I think you said {}".format(item))

>>>>>>> 77e968bfaf731a23d072818f9863a0593a881c91

@ask.session_ended
def session_ended():
    logging.info("Session ended!")
<<<<<<< HEAD
#     logging.info("Request ID: {}".format(request.requestId))
#     logging.info("Request Type: {}".format(request.type))
#     logging.info("Request Timestamp: {}".format(request.timestamp))
=======
>>>>>>> 77e968bfaf731a23d072818f9863a0593a881c91
    logging.info("Session New?: {}".format(session.new))
    logging.info("User ID: {}".format(session.user.userId))
    logging.info("Alexa Version: {}".format(version))
    logging.info("Device ID: {}".format(context.System.device.deviceId))
<<<<<<< HEAD
#     logging.info("Consent Token: {}".format(context.System.user.permissions.consentToken))
=======
    return question("I think we are done!")
>>>>>>> 77e968bfaf731a23d072818f9863a0593a881c91
    return "{}", 200

if __name__ == '__main__':
    app.run(debug=True, port=8050)

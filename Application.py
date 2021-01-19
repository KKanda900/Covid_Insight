from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import USA_COVID19 as c19
import Data as d
import os

app = Flask(__name__)

def check_valid_input(input_):
    file_exists = False
    for filename in os.listdir('data/'):
        if filename.startswith('{}_Data.csv'.format(input_)):
            file_exists = True
            break
    
    return file_exists

@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    resp = MessagingResponse()

    if message_body == 'instructions' or message_body == "Instructions":
        resp.message('Hey welcome! Lets get started now! If you want: 1. The latest positive cases type in cases and initials of the state. 2. The rate that the cases have risen over a certain amount of days, type in rate and your state. 3. A predicition of the case numbers for n number of days type in prediction, n (being the number of days) and the state initials.')
        return str(resp)

    tokens = message_body.split(' ') # at this point, the input is not going to be a instructions request so lets process what the user said

    if tokens[0] == 'cases' and check_valid_input(tokens[1]) == True:
        cases = c19.positive_case_update(tokens[1])
        resp.message(cases)
        return str(resp)
    elif tokens[0] == 'rate' and check_valid_input(tokens[1]) == True:
        roc = c19.get_rate_of_change(tokens[1])
        resp.message(roc)
        return str(resp)
    elif tokens[0] == 'prediction' and tokens[1].isnumeric() and check_valid_input(tokens[2]) == True:
        cases = c19.bayesian_prediction(tokens[2], tokens[1])
        resp.message(cases)
        return str(resp)

    return str('Error: What you request is incorrect format or does not exist, please try another input')

if __name__ == "__main__":
    app.run(debug=True)
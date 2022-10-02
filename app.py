#import required libraries
import numpy as np
from flask import Flask, request, make_response,render_template,jsonify
import json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from flask_cors import cross_origin
#instantiate flask
app = Flask(__name__)
model = load_model('model1d.h5')

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    query = (json_)
    prediction = model.predict(query)
    return jsonify({'prediction': list(prediction)})

# getting and sending response to dialogflow
@app.route('/webhook', methods=['GET','POST'])
#@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    print(req)
    res = processRequest(req)

    res = json.dumps(res, indent=4)
    #print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


# processing the request from dialogflow
def processRequest(req):

    #sessionID=req.get('responseId')
    #result = req.get("queryResult")
    Message = req.get("queryResult").get("queryText")
    final_features = [Message]
    #print(result)

    #parameters = result.get("parameters")
    #Message = parameters.get("Message")
    #print(Message)
    #final_features = str(Message)
    #intent = result.get("intent").get('displayName')

    #if (intent=='Default Welcome Intent - yes'):
    #prediction = model.predict_spam(final_features)  
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(final_features)
    new_seq = tokenizer.texts_to_sequences(final_features)
    padded = pad_sequences(new_seq, maxlen =150,
                      padding = "post",
                      truncating="post")
    result = model.predict(padded)
    if (result> 0.5):
      prediction = "spam"
    else:
      prediction = "ham"

    print(prediction)
    if(prediction == "spam"):
        status = 'Yes, this is most likely a scam message, please do not fall for it!'
    elif(prediction == "ham"):
        status = 'No, this does not seem like a scam message' 
    else:
        status = "This is not a sentence!!"
    fulfillmentText= status
    print(fulfillmentText)
    print(prediction)
    return {
        "fulfillmentText": fulfillmentText
    }


if __name__ == '__main__':
    app.run()

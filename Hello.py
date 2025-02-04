from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return {'message': 'Pinging Model Application!'}

model_pickle = open("classifier.pkl", "rb")
clf = pickle.load(model_pickle)
 

@app.route('/predict', methods = ['POST'])
def predict():
    loan_req = request.get_json()

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']

    result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        pred = "Rejected"
    else:
        pred = "Approved"
    return{"loan_approval_status": pred}
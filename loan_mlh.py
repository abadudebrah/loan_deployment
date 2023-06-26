# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 20:53:01 2023

@author: HTLADMIN
"""



from fastapi import FastAPI 
from pydantic import BaseModel
import pickle
import json
import uvicorn



app = FastAPI()

class model_input(BaseModel):
    Duration_of_Credit_Month : int
    Credit_Amount : int
    Instalment_per_cent : int
    Most_valuable_available_asset : int
    Age_years : float
    Type_of_apartment : int
    Account_Balance_Some_Balance : int
    Payment_Status_of_Previous_Credit_Paid_Up : int
    Payment_Status_of_Previous_Credit_Some_Problems : int
    Purpose_New_car : int
    Purpose_Used_car : int
    Value_Savings_Stocks_less_hundred : int
    Value_Savings_Stocks_None : int
    

#loading the model
loan_model = pickle.load(open('rfc.pkl', 'rb'))


@app.post('/prediction')
def loan_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    dur_crdt_mth = input_dictionary['Duration_of_Credit_Month']
    cred_amt = input_dictionary['Credit_Amount']
    insta_percnt = input_dictionary['Instalment_per_cent']
    most_val_ass = input_dictionary['Most_valuable_available_asset']
    age_years = input_dictionary['Age_years']
    type_aprtmnt = input_dictionary['Type_of_apartment']
    acc_bal = input_dictionary['Account_Balance_Some_Balance']
    paymt_stat_pp = input_dictionary['Payment_Status_of_Previous_Credit_Paid_Up']
    paymt_stat_sp = input_dictionary['Payment_Status_of_Previous_Credit_Some_Problems']
    purp_nc = input_dictionary['Purpose_New_car']
    purp_uc = input_dictionary['Purpose_Used_car']
    val_sav_stck_lh = input_dictionary['Value_Savings_Stocks_less_hundred']
    val_sav_stck_n = input_dictionary['Value_Savings_Stocks_None']
    
    
        
    input_list = [dur_crdt_mth,cred_amt,insta_percnt,most_val_ass,age_years,type_aprtmnt,
                  acc_bal,paymt_stat_pp,paymt_stat_sp,purp_nc,purp_uc,val_sav_stck_lh,
                  val_sav_stck_n]
    
    prediction = loan_model.predict([input_list])
    
    if prediction[0]== 0:
        return 'The person is not Loan eligible'
    else:
        return 'The person is Loan eligible'

#if __name__ == '__main__':
#    uvicorn.run(app,host = '127.0.0.1', port = 8000)
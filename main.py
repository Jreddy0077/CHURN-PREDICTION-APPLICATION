
import pandas as pd
import pickle
import streamlit as st


st.set_page_config(layout="wide")
col1,col2=st.columns(2)
with col1:
    st.title("**Welcome to the Churn Prediction App!**")

dic = {}



# Title and header
c1,c2,c3,c4,c5,c6=st.columns(6)


    

    


with c1:
    states = ['OH', 'NJ', 'OK', 'MA', 'MO', 'LA', 'WV', 'IN', 'RI', 'IA', 'MT',
              'NY', 'ID', 'VA', 'TX', 'FL', 'CO', 'AZ', 'SC', 'WY', 'HI', 'NH',
              'AK', 'GA', 'MD', 'AR', 'WI', 'OR', 'MI', 'DE', 'UT', 'CA', 'SD',
              'NC', 'WA', 'MN', 'NM', 'NV', 'DC', 'VT', 'KY', 'ME', 'MS', 'AL',
              'NE', 'KS', 'TN', 'IL', 'PA', 'CT', 'ND']
    selected_states = st.selectbox("**Select states**", states)
    st.write("Selected states:", selected_states)

# Area code selection
with c1:
    area_codes = ["415", "408", "510"]
    selected_code = st.selectbox("**select an area code**", area_codes)
    st.write("Selected area code:", selected_code)

# International plan selection
with c1:
    international_yes = st.checkbox("International Plan - Yes", key="international_yes")
    international_no = st.checkbox("International Plan - No", key="international_no")
    if international_yes and international_no:
        st.write("Please select only one option for international plan.")
    elif international_yes:
        international_plan = "yes"
    elif international_no:
        international_plan = "no"
    else:
        international_plan = "Not selected"
    st.write("Selected international plan:", international_plan)

# Voice mail plan selection
with c1:
    voice_mail_yes = st.checkbox("Voice Mail Plan - Yes", key="voice_mail_yes")
    voice_mail_no = st.checkbox("Voice Mail Plan - No", key="voice_mail_no")
    if voice_mail_yes and voice_mail_no:
        st.write("Please select only one option for voice mail plan.")
    elif voice_mail_yes:
        voice_mail_plan = "yes"
    elif voice_mail_no:
        voice_mail_plan = "no"
    else:
        voice_mail_plan = "Not selected"
    st.write("Selected voice mail plan:", voice_mail_plan)

# Input values
variables = [
    'account_length', 'number_vmail_messages', 'total_day_minutes',
    'total_day_calls', 'total_day_charge', 'total_eve_minutes',
    'total_eve_calls', 'total_eve_charge', 'total_night_minutes',
    'total_night_calls', 'total_night_charge', 'total_intl_minutes',
    'total_intl_calls', 'total_intl_charge',
    'number_customer_service_calls','total_min', 'total_call',
       'total_charge', 'plan_day', 'plan_weeks', 'plan_years', 'charge_day'
]

# Iterate over variables and create input boxes in each column
for i, variable in enumerate(variables):
    if i <=4:
        with c2:
            input_value = st.number_input(f"**{variable}**", step=None)
            st.write(f"{variable}: {input_value}")
            dic[variable] = input_value
    elif i >4 and i <=9:
        with c3:
            input_value = st.number_input(f"**{variable}**", step=None)
            st.write(f"{variable}: {input_value}")
            dic[variable] = input_value
    elif i >9 and i <=14:
        with c4:
            input_value = st.number_input(f"**{variable}**", step=None)
            st.write(f"{variable}: {input_value}")
            dic[variable] = input_value

    
    elif i >14 and i <=18:
    
        with c5:
            input_value = st.number_input(f"**{variable}**", step=None)
            st.write(f"{variable}: {input_value}")
            dic[variable] = input_value

    
    else:
    
        with c6:
            input_value = st.number_input(f"**{variable}**", step=None)
            st.write(f"{variable}: {input_value}")
            dic[variable] = input_value

# calicutating some extracted featiures



l = [value for value in dic.values()]
l.insert(0, selected_states)
l.insert(2, selected_code)
l.insert(3, international_plan)
l.insert(4, voice_mail_plan)









data2 = [l]

columns = ['state', 'account_length', 'area_code', 'international_plan',
           'voice_mail_plan', 'number_vmail_messages', 'total_day_minutes',
           'total_day_calls', 'total_day_charge', 'total_eve_minutes',
           'total_eve_calls', 'total_eve_charge', 'total_night_minutes',
           'total_night_calls', 'total_night_charge', 'total_intl_minutes',
           'total_intl_calls', 'total_intl_charge',
           'number_customer_service_calls','total_min', 'total_call',
       'total_charge', 'plan_day', 'plan_weeks', 'plan_years', 'charge_day']

df2= pd.DataFrame(data2, columns=columns)



# model=pickle.load(open("strnew.pkl","rb"))


import os


model_path = os.path.join(os.path.dirname(__file__), "strnew.pkl")
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Model file {model_path} not found.")
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")


if st.button("Predict"):
    with st.spinner('Predicting...'):
        try:
            result = model.predict(df2)
            if result[0] == 0:
                st.write("**Congratulations! The customer is likely to continue their subscription.** 🎉😊")
                st.balloons()  # This simulates a celebratory animation
            else:
                st.write("**Bad luck! The customer is predicted to churn and discontinue their subscription.** 😞")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
 
        
    







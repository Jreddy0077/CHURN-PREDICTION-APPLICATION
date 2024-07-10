
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


    

    
    #st.image("data:image/png;base64,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")
#st.write("**This application allows you to predict customer churn based on various input features. To get started, please provide the required information in the input fields below. Once you have entered all the necessary details, click the Predict button to see the churn prediction results.**")

# Create three columns for organizing input and output

# Gender selection
# col1, col2, col3 = st.columns(3)
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



model=pickle.load(open("strnew.pkl","rb"))



    
        
    


import streamlit as st


with c1:
    if st.button("Predict", key="submit_2"):
        result2 = model.predict(df2)
        if result2==0:
            output1="** Congratulations! The customer is likely to continue their subscription.**"
        else:
            output1="**Bad luck! The customer is predicted to churn and discontinue their subscription.**"
        st.write(output1)



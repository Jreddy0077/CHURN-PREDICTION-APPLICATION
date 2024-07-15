import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import streamlit as st
import time
from streamlit_option_menu import option_menu
import streamlit as st
from datetime import datetime


df=None
# Navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # required
        options=["Home", "Data", "About"],  # required
        icons=["house", "bar-chart", "info-circle"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
    )

# Pages based on selected option
if selected == "Home":
    st.title("**Welcome to the Churn Prediction App!**")

    
        
    
        


    prediction_method = st.radio('Select Prediction Method', ('Predict Churn Record-wise', 'Predict Churn for Entire DataFrame'))

    if prediction_method=='Predict Churn Record-wise':



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
            with st.spinner("Please wait while predicting...."):
                time.sleep(0.5)
            
                try:
                    result = model.predict(df2)
                    if result[0] == 0:
                        st.write("**Congratulations! The customer is likely to continue their subscription.** 🎉😊")
                        st.balloons()  # This simulates a celebratory animation
                    else:
                        st.write("**Bad luck! The customer is predicted to churn and discontinue their subscription.** 😞")
                        st.toast('bad luck', icon="👎")
                except Exception as e:
                    st.error(f"An error occurred during prediction: {e}")
    
            
    
    if prediction_method=='Predict Churn for Entire DataFrame':

        import os
        model_path = os.path.join(os.path.dirname(__file__), "strnew.pkl")
        try:
            with open(model_path, "rb") as f:
                model = pickle.load(f)
        except FileNotFoundError:
            st.error(f"Model file {model_path} not found.")
        except Exception as e:
            st.error(f"An error occurred while loading the model: {e}")

        file_type = st.selectbox("Select file type", ("CSV", "Excel"))
        #uploaded_file=None

        uploaded_file = st.file_uploader(f"Upload {file_type} file", type=[file_type.lower()])
        try:
            df=pd.read_csv(uploaded_file)
        except Exception as e:
                        st.error(f"An error occurred during prediction: {e}")
        


        if st.button("Predict"):
            with st.spinner("Please wait while predicting...."):
                time.sleep(3)
            
            
                try:
                    result = model.predict(df)
                    churn = ["Yes" if pred == 1 else "No" for pred in result]
                    df["churn"] = churn

                    churn_counts = df['churn'].value_counts()

                    st.write(f"No of churn customers: {churn_counts['Yes']}")
                    st.write(f"Total customers: {len(churn)}")
                    st.title("Go to Data tab to view analytics")
                    df.to_csv("df.csv")
                except Exception as e:
                        st.error(f"An error occurred during prediction: {e}")
                
            
                










elif selected == "Data":
    st.set_option('deprecation.showPyplotGlobalUse', False)

    df = pd.read_csv("df.csv")
    

    st.title('Churn Analysis')
    st.write('Bar plot of Churn counts:')

    

    # Calculate value counts
    churn_counts = df['churn'].value_counts()

    # Plotting using Matplotlib or Seaborn
    plt.figure(figsize=(6, 4))
    sns.barplot(x=churn_counts.index, y=churn_counts.values)
    plt.xlabel('Churn')
    plt.ylabel('Count')
    plt.title('Churn Counts')
    st.pyplot()





elif selected == "About":
    st.write("hi")
    current = datetime.now()
    st.write(current)
    if current >= datetime(2024, 7, 15, 23, 35, 0):
        st.title("Happy birthday Jeevan Reddy")
        st.snow()

    st.title("About")
    st.write("This is an example Streamlit app with navigation.")
    options = ["Login", "Create New Account"]

    # Dropdown menu
   # sel = st.selectbox("Select an option:", options)
    if st.button("login"):
        
        user_name=st.text_input("enter the user name")
        password=st.text_input("enter tuhe user name",type="password")
        st.button("logint")
            #st.write(user_name)
            #ok=st.button("logout")
    


    if st.button("register"):
        user_name=st.text_input("enter the user name")
        number=st.number_input("enter the phone number")
        mail=st.text_input("enter the mail")
        password=st.text_input("enter the password",type="password")
        password=st.text_input("enter the password again",type="password")
        st.button("register")

    if st.button("view profile"):
        st.write(user_name)

    


    

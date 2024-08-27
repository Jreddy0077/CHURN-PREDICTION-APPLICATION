from streamlit_option_menu import option_menu
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import streamlit as st
import time
import base64

import re



import os
model_path = os.path.join(os.path.dirname(__file__), "strnew.pkl")
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Model file {model_path} not found.")
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
####################################################################################











df=None



st.set_page_config(layout="wide")

# Custom CSS to remove padding and margins

# these are the internal dinamic classes genrating during running and we are making them padding 0
# style for inserting the css script
# unsafe_allow_html=True to insert the html and css into the streamlit
# markdown is to exicute the css and html into the streamlit

custom_css = """
    <style>
    .css-1d391kg, .css-1v3fvcr, .css-18e3th9 {
        padding: 0 !important;
    }
    </style>
"""

st.markdown(custom_css, unsafe_allow_html=True)



# Navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # required
        options=["Home", "Prediction Analytics"],  # required
        icons=["house", "bar-chart"],  # optional
         menu_icon="box-arrow-in-right",
        default_index=0,  # optional
    )

# Pages based on selected option
if selected == "Home":
       
        dic={}

        #st.title("**Welcome to the Churn Prediction App!**")
        st.markdown('<h2 style="color:yellow;">There You Can Predict The Churn Of The Customers</h2>', unsafe_allow_html=True)


        st.markdown('<h4 style="color:orange;">Select Prediction Method</h4>', unsafe_allow_html=True)

        prediction_method = st.radio('', ('Predict Churn Record-wise', 'Predict Churn for Entire DataFrame'))
        if prediction_method=='Predict Churn Record-wise':
            c1, c2, c3, c4, c5, c6 = st.columns([1,1,1,1,1,1.3])
            with c1:
                states = ['OH', 'NJ', 'OK', 'MA', 'MO', 'LA', 'WV', 'IN', 'RI', 'IA', 'MT',
                        'NY', 'ID', 'VA', 'TX', 'FL', 'CO', 'AZ', 'SC', 'WY', 'HI', 'NH',
                        'AK', 'GA', 'MD', 'AR', 'WI', 'OR', 'MI', 'DE', 'UT', 'CA', 'SD',
                        'NC', 'WA', 'MN', 'NM', 'NV', 'DC', 'VT', 'KY', 'ME', 'MS', 'AL',
                        'NE', 'KS', 'TN', 'IL', 'PA', 'CT', 'ND']

                st.markdown('<p style="color:red;">State</p>', unsafe_allow_html=True)
                selected_states = st.selectbox("", states, key='selected_states')

                st.markdown('<p style="color:red;">Account Length</p>', unsafe_allow_html=True)
                account_length = st.number_input("", key='account_length')

                st.markdown('<p style="color:red;">Area Code</p>', unsafe_allow_html=True)
                selected_code = st.selectbox("", (415, 408, 510), key='selected_code')

            with c2:
                st.markdown('<p style="color:red;">International Plan</p>', unsafe_allow_html=True)
                international_plan = st.selectbox("", ("yes", "no"), key='international_plan')

                st.markdown('<p style="color:red;">Voice Mail Plan</p>', unsafe_allow_html=True)
                voice_mail = st.selectbox("", ("yes", "no"), key='voice_mail')

                st.markdown('<p style="color:red;">Number of Voicemail Messages</p>', unsafe_allow_html=True)
                number_vmail_messages = st.number_input("", key='number_vmail_messages')

            with c3:
                st.markdown('<p style="color:red;">Total Day Minutes</p>', unsafe_allow_html=True)
                total_day_minutes = st.number_input("", key='total_day_minutes')

                st.markdown('<p style="color:red;">Total Day Calls</p>', unsafe_allow_html=True)
                total_day_calls = st.number_input("", key='total_day_calls')

                st.markdown('<p style="color:red;">Total Day Charge</p>', unsafe_allow_html=True)
                total_day_charge = st.number_input("", key='total_day_charge')

            with c4:
                st.markdown('<p style="color:red;">Total Evening Minutes</p>', unsafe_allow_html=True)
                total_eve_minutes = st.number_input("", key='total_eve_minutes')

                st.markdown('<p style="color:red;">Total Evening Calls</p>', unsafe_allow_html=True)
                total_eve_calls = st.number_input("", key='total_eve_calls')

                st.markdown('<p style="color:red;">Total Evening Charge</p>', unsafe_allow_html=True)
                total_eve_charge = st.number_input("", key='total_eve_charge')

            with c5:
                st.markdown('<p style="color:red;">Total Night Minutes</p>', unsafe_allow_html=True)
                total_night_minutes = st.number_input("", key='total_night_minutes')

                st.markdown('<p style="color:red;">Total Night Calls</p>', unsafe_allow_html=True)
                total_night_calls = st.number_input("", key='total_night_calls')

                st.markdown('<p style="color:red;">Total Night Charge</p>', unsafe_allow_html=True)
                total_night_charge = st.number_input("", key='total_night_charge')

            with c6:
                st.markdown('<p style="color:red;">Total International Minutes</p>', unsafe_allow_html=True)
                total_intl_minutes = st.number_input("", key='total_intl_minutes')

                st.markdown('<p style="color:red;">Total International Calls</p>', unsafe_allow_html=True)
                total_intl_calls = st.number_input("", key='total_intl_calls')

                st.markdown('<p style="color:red;">Total International Charge</p>', unsafe_allow_html=True)
                total_intl_charge = st.number_input("", key='total_intl_charge')

                st.markdown('<p style="color:red;">Number of Customer Service Calls</p>', unsafe_allow_html=True)
                number_customer_service_calls = st.number_input("", key='number_customer_service_calls')



            # Calculations
            total_charge = total_day_charge + total_eve_charge + total_night_charge
            total_days = account_length * 30

            if total_days != 0:
                charge_per_day = total_charge / total_days
            else:
                charge_per_day = 0

            l_var = [
                selected_states, 
                account_length, 
                selected_code, 
                international_plan, 
                voice_mail, 
                number_vmail_messages, 
                total_day_minutes, 
                total_day_calls, 
                total_day_charge, 
                total_eve_minutes, 
                total_eve_calls, 
                total_eve_charge, 
                total_night_minutes, 
                total_night_calls, 
                total_night_charge, 
                total_intl_minutes, 
                total_intl_calls, 
                total_intl_charge, 
                number_customer_service_calls,
                total_day_minutes + total_eve_minutes + total_night_minutes, 
                total_day_calls + total_night_calls + total_eve_calls, 
                total_charge,
                total_days,
                account_length / 4 if account_length != 0 else 0,
                account_length / 12 if account_length != 0 else 0,
                charge_per_day]

                    
        
        
        
            
                
            data2 = [l_var]

            columns = ['state', 'account_length', 'area_code', 'international_plan',
                    'voice_mail_plan', 'number_vmail_messages', 'total_day_minutes',
                    'total_day_calls', 'total_day_charge', 'total_eve_minutes',
                    'total_eve_calls', 'total_eve_charge', 'total_night_minutes',
                    'total_night_calls', 'total_night_charge', 'total_intl_minutes',
                    'total_intl_calls', 'total_intl_charge',
                    'number_customer_service_calls','total_min', 'total_call',
                'total_charge', 'plan_day', 'plan_weeks', 'plan_years', 'charge_day']

            df2= pd.DataFrame(data2, columns=columns)
            import os
# C:\Users\User\project\strnew.pkl

            
            
                
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
                

                st.markdown('<p style="color:red;">Select file type</p>', unsafe_allow_html=True)

        
                file_type = st.selectbox("", ("CSV", "Excel"))
                #uploaded_file=None


        
                uploaded_file = st.file_uploader(f"Upload {file_type} file",type=[file_type.lower()])

                if file_type=="CSV":

                    try:
                        df=pd.read_csv(uploaded_file)
                        df.to_csv("df.csv",index=False)
                    except Exception as e:
                                    st.write("Not Uploaded")
                else:
                    try:
                        df=pd.read_excel(uploaded_file)
                        df.to_excel("df.xlsx",index=False)

                    except Exception as e:
                                    st.write("Not Uploaded")

                    
        
                #with c1:
                if st.button("Predict"):
                    with st.spinner("Please wait while predicting...."):
                        time.sleep(3)
                    
                    
                        try:
                            result = model.predict(df)
                            churn = ["Yes" if pred == 1 else "No" for pred in result]
                            df["churn"] = churn
        
                            churn_counts = df['churn'].value_counts()
        
                            st.markdown(f'<p style="color:orange; font-weight:bold;">No of churn customers: {churn_counts["Yes"]}</p>', unsafe_allow_html=True)
                            st.markdown(f'<p style="color:orange; font-weight:bold;">Total customers: {len(churn)}</p>', unsafe_allow_html=True)
                            st.title("Go to Prediction Analytics to view analytics")
                                    
        
        
                        except Exception as e:
                                st.error("Please upload your file before predicting...")
                        
                    
                        


elif selected == "Prediction Analytics":
    data=False



    


    
    with st.container():
         st.title('Churn Prediction Analysis...........')
    try:
         df = pd.read_csv("df.csv")
         data=True
    except Exception as e:
         st.title("You Have No Any Prediction yet")
    

    


    #st.set_option('deprecation.showPyplotGlobalUse', False)
    
    p1,p2=st.columns(2)

    if data:
        with p1:

            churn_counts = df['churn'].value_counts()


            plt.figure(figsize=(4,4))
            st.markdown('<p style="color:red;font-weight:bold;">Bar plot of Churn counts:</p>', unsafe_allow_html=True)

            sns.barplot(x=churn_counts.index, y=churn_counts.values)
            plt.xlabel('Churn')
            plt.ylabel('Count')
            plt.title('Churn Counts')
            st.pyplot()

        with p2:
            st.markdown('<p style="color:red;font-weight:bold;">International_plan VS Churn</p>', unsafe_allow_html=True)

            plt.figure(figsize=(4,4))
            sns.countplot(x="international_plan", hue="churn", data=df)
            st.pyplot()
            
        st.markdown('<p style="color:red;font-weight:bold;">Churn VS State</p>', unsafe_allow_html=True)
        plt.figure(figsize=(25,7))
        sns.countplot(x="state", hue="churn", data=df)
        st.pyplot()


        st.markdown('<p style="color:red;font-weight:bold;">Area Code vs Churn</p>', unsafe_allow_html=True)

        plt.figure(figsize=(8,4))
        sns.countplot(x="area_code", hue="churn", data=df)

        st.pyplot()

        st.markdown('<p style="color:red;font-weight:bold;">Voice Mail Plan vs Churn</p>', unsafe_allow_html=True)

        plt.figure(figsize=(8,4))
        sns.countplot(x="voice_mail_plan", hue="churn", data=df)
        st.pyplot()
    
    

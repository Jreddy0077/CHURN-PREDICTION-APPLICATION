from streamlit_option_menu import option_menu
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import streamlit as st
import time
import base64
from sqlalchemy import create_engine,text
import pymysql
from sqlalchemy.exc import SQLAlchemyError
import re


####################################################################################

db_user = '2yasPb2k6DKrXZH.root'
db_password = 'E28f3eorNGjxx6K4'
db_host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com'
db_port = '4000'
db_name = 'test'
ca_path = '/path/to/ca_cert.pem'  # Replace with the actual path to your CA certificate

connection_string = (
    f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?'
    f'ssl_ca={ca_path}&ssl_verify_cert=true'
)

def add_user(first_name, last_name, sur_name, number, mail, password):
    try:
        engine = create_engine(connection_string)
        conn = engine.connect()

        insert_query =text("""
            INSERT INTO users (first_name, last_name, sur_name, number, mail, password)
            VALUES (:first_name, :last_name, :sur_name, :number, :mail, :password)
        """)
        
        conn.execute(insert_query, {
            'first_name': first_name,
            'last_name': last_name,
            'sur_name': sur_name,
            'number': number,
            'mail': mail,
            'password': password
        })
        
        conn.commit()
        conn.close()
        
        st.success("User added successfully!")
    except SQLAlchemyError as e:
        st.error(f"An error occurred: {str(e)}")

############################################################################



try:
    # Initialize connection
    engine = create_engine(connection_string)
    conn = engine.connect()
    df_user= pd.read_sql('SELECT * FROM users', conn)

    df_user['number'] = df_user['number'].astype(str)

    conn.close()
    engine.dispose()
except SQLAlchemyError as e:
    st.error(f"An error occurred: {str(e)}")



df=None
def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()




st.set_page_config(layout="wide")

# Custom CSS to remove padding and margins
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
        options=["Home", "Data", "Register/Login/Profile","history"],  # required
        icons=["house", "bar-chart", "person-square","clock-history"],  # optional
        menu_icon="Icon font",  # optional
        default_index=2,  # optional
    )

# Pages based on selected option
if selected == "Home":
        bg_image_path = r"bg_home1.jpg"
        bg_image_base64 = get_base64_of_bin_file(bg_image_path)
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg_image_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)
        dic={}

        st.title("**Welcome to the Churn Prediction App!**")
        prediction_method = st.radio('Select Prediction Method', ('Predict Churn Record-wise', 'Predict Churn for Entire DataFrame'))
        if prediction_method=='Predict Churn Record-wise':
                c1,c2,c3,c4,c5,c6=st.columns(6)
                with c1:
                    states = ['OH', 'NJ', 'OK', 'MA', 'MO', 'LA', 'WV', 'IN', 'RI', 'IA', 'MT',
                            'NY', 'ID', 'VA', 'TX', 'FL', 'CO', 'AZ', 'SC', 'WY', 'HI', 'NH',
                            'AK', 'GA', 'MD', 'AR', 'WI', 'OR', 'MI', 'DE', 'UT', 'CA', 'SD',
                            'NC', 'WA', 'MN', 'NM', 'NV', 'DC', 'VT', 'KY', 'ME', 'MS', 'AL',
                            'NE', 'KS', 'TN', 'IL', 'PA', 'CT', 'ND']
                    selected_states = st.selectbox("**Select states**", states)
        
                # Area code selection
                with c1:
                    area_codes = ["415", "408", "510"]
                    selected_code = st.selectbox("**select an area code**", area_codes)
        
                with c1:
                    international_plan=st.selectbox("international_plan",("yes","no"))
                    
                    voice_mail=st.selectbox("voice_mail",("yes","no"))
                        
                variables = [
                    'account_length', 'number_vmail_messages', 'total_day_minutes',
                    'total_day_calls', 'total_day_charge', 'total_eve_minutes',
                    'total_eve_calls', 'total_eve_charge', 'total_night_minutes',
                    'total_night_calls', 'total_night_charge', 'total_intl_minutes',
                    'total_intl_calls', 'total_intl_charge',
                    'number_customer_service_calls','total_min', 'total_call',
                    'total_charge', 'plan_day', 'plan_weeks', 'plan_years', 'charge_day'
                ]
        
                for i, variable in enumerate(variables):
                    if i <=4:
                        with c2:
                            input_value = st.number_input(f"**{variable}**", step=None)
                            dic[variable] = input_value
                    elif i >4 and i <=9:
                        with c3:
                            input_value = st.number_input(f"**{variable}**", step=None)
                            dic[variable] = input_value
                    elif i >9 and i <=14:
                        with c4:
                            input_value = st.number_input(f"**{variable}**", step=None)
                            dic[variable] = input_value
        
                    
                    elif i >14 and i <=18:
                    
                        with c5:
                            input_value = st.number_input(f"**{variable}**", step=None)
                           # st.write(f"{variable}: {input_value}")
                            dic[variable] = input_value
        
                    
                    else:
                    
                        with c6:
                            input_value = st.number_input(f"**{variable}**", step=None)
                            dic[variable] = input_value
        
        
        
        
                l = [value for value in dic.values()]
                l.insert(0, selected_states)
                l.insert(2, selected_code)
                l.insert(3, international_plan)
                l.insert(4, voice_mail)
                
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
                            df1=pd.read_csv("df.csv")
                            df_combined = pd.concat([df,df1.head(0)], ignore_index=True)
        
        
                            df.to_csv("df.csv",index=False)
                            df1=pd.read_csv("df.csv")
                            st.write(df1)
        
        
                        except Exception as e:
                                st.error(f"An error occurred during prediction: {e}")
                        
                    
                        


elif selected == "Data":

    bg_image_path = r"bg_data.jpg"

    
    bg_image_base64 = get_base64_of_bin_file(bg_image_path)

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg_image_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)


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


elif selected == "Register/Login/Profile":
        bg_image_path = r"login_image.jpg"
        import base64
        
        def get_base64_of_bin_file(bin_file):
            with open(bin_file, 'rb') as f:
                 data = f.read()
                 return base64.b64encode(data).decode()
        
        bg_image_base64 = get_base64_of_bin_file(bg_image_path)
        
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg_image_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)
########################################################################3333333333
        
#################################################################################
        l_number = list(df_user["number"])

##############################################################################################

   
    

        st.markdown('<h2 style="color:orange;">Welcome To Churn Prediction Application</h2>', unsafe_allow_html=True)





        with st.container():
            st.markdown('<p style="color:red;">To access the app please Login or Signup</p>', unsafe_allow_html=True)
            st.markdown('<p style="color:red;">Select an option:</p>', unsafe_allow_html=True)
            option = st.selectbox('', ('Login',"Signup"))

        import streamlit as st
        import re
        import pandas as pd


        col1, col2 = st.columns(2)

        if option=="Login":
             with col1:
                st.markdown('<p style="color:gold;">Enter Your Mobile Number:</p>', unsafe_allow_html=True)
                number = st.text_input("", key="number")


               
                
                # Initialize mobile check
                mobile = False
                
                # Check if the number is in the list
                if number in l_number:
                    st.markdown('<p style="color:gold;">Mobile Number Is Correct</p>', unsafe_allow_html=True)
                    mobile = True
                else:
                    st.markdown('<p style="color:gold;">Incorrect Mobile Number</p>', unsafe_allow_html=True)
                
                # UI for password input
                st.markdown('<p style="color:gold;">Enter Your Password:</p>', unsafe_allow_html=True)
                password = st.text_input("", key="password", type="password")
                
                # Initialize password check
                passs = False
                
                if mobile:
                    password_org = df_user[df_user["number"] == number]["password"].values[0]

                    # Get the original password for the entered number
                    
                
                    # Check if the entered password matches the original password
                    if password_org == password:
                        st.markdown('<p style="color:gold;">Password Is Correct</p>', unsafe_allow_html=True)
                        passs = True
                    else:
                        st.markdown('<p style="color:gold;">Incorrect Password</p>', unsafe_allow_html=True)
                    
                # Check login button
                if st.button("Login"):
                    if mobile and passs:
                        st.markdown('<p style="color:gold;">Successfully Logged In</p>', unsafe_allow_html=True)
                    else:
                        st.markdown('<p style="color:gold;">Enter The Details Correctly</p>', unsafe_allow_html=True)
                
                    


        if option == "Signup":
            with col1:
                st.markdown('<p style="color:gold;">Enter The First Name:</p>', unsafe_allow_html=True)
                first_name = st.text_input("", key="first_name")
                st.markdown('<p style="color:gold;">Enter The Surname:</p>', unsafe_allow_html=True)
                sur_name = st.text_input("", key="sur_name")

                st.markdown('<p style="color:gold;">Enter The Last Name:</p>', unsafe_allow_html=True)
                last_name = st.text_input("", key="last_name")
                st.markdown('<p style="color:gold;">Enter Your Mobile Number:</p>', unsafe_allow_html=True)
                number = st.text_input("", key="number")

                if number.isnumeric() and number[0] in "9876" and len(number) == 10:
                    st.markdown('<p style="color:green;">Number is valid</p>', unsafe_allow_html=True)
                    number_val = True
                else:
                    st.markdown('<p style="color:red;">Number is invalid</p>', unsafe_allow_html=True)
                    number_val = False

                st.markdown('<p style="color:gold;">Enter The Mail</p>', unsafe_allow_html=True)
                mail = st.text_input("", key="mail")

                def is_valid_email(email):
                    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
                    return pattern.match(email) is not None

                if is_valid_email(mail):
                    st.markdown('<p style="color:green;">The email address is valid</p>', unsafe_allow_html=True)
                    mail_val = True
                else:
                    st.markdown('<p style="color:red;">The email address is invalid</p>', unsafe_allow_html=True)
                    mail_val = False

                def is_valid_password(password):
                    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#@$!%*?&])[A-Za-z\d@#$!%*?&]{8,16}$')
                    return pattern.match(password) is not None

            from streamlit_lottie import st_lottie   
            import json   

            with col2:

                

                def load_lottiefile(path):
                    with open(path, "r") as f:
                        return json.load(f)

                # Load Lottie file
                lottie_path = r"User registration.mp4.lottie.json"
                lottie_animation = load_lottiefile(lottie_path)

                # Display Lottie animation
                st_lottie(
                    lottie_animation,
                    speed=3,
                    reverse=False,
                    loop=True,
                    quality="high",
                
                )







           


            st.markdown('<p style="color:gold;">Enter the password</p>', unsafe_allow_html=True)
            password = st.text_input("", key="password", type="password")

            if is_valid_password(password):
                st.markdown('<p style="color:green;">The password is valid</p>', unsafe_allow_html=True)
                password_val = True
            else:
                st.markdown('<p style="color:red;">The password should have at least one lowercase letter, one uppercase letter, one digit, one special character (@$!%*?&) and be 8-16 characters long.</p>', unsafe_allow_html=True)
                password_val = False

            st.markdown('<p style="color:gold;">Confirm the password</p>', unsafe_allow_html=True)
            c_password = st.text_input("", key="c_password", type="password")

            if c_password == password:
                st.markdown('<p style="color:green;">Password Is Matched</p>', unsafe_allow_html=True)
                c_password_val = True
            else:
                st.markdown('<p style="color:red;">Password Is Not Matches</p>', unsafe_allow_html=True)
                c_password_val = False
            
            #st.write(df_user)
            

            if st.button("Register"):
                l_password = list(df_user["password"])

                l_number = list(df_user["number"])
                l_mail = list(df_user["mail"])
                

                
                
                if (number) in l_number:
                    st.markdown('<p style="color:red;">This Number is Already Registered</p>', unsafe_allow_html=True)
                elif mail in l_mail:
                    st.markdown('<p style="color:red;">This mail is Already Registered</p>', unsafe_allow_html=True)
                elif password in l_password:
                    st.markdown('<p style="color:red;">This password is Already Registered</p>', unsafe_allow_html=True)


                elif c_password_val and password_val and mail_val and number_val:

                    
                

                    #new_user = [first_name, last_name, sur_name, (number), mail, password]

                    add_user(first_name, last_name, sur_name, number, mail, password)



                    #st.write(df_user)

                    
                    st.markdown('<p style="color:green;">Successfully Registered</p>', unsafe_allow_html=True)
                else:
                    st.markdown('<p style="color:red;">You Have Entered Something Wrong</p>', unsafe_allow_html=True)




elif selected == "history":
    df_user=pd.DataFrame(columns=['first_name', 'last_name', 'sur_name', 'contact', 'mail', 'password'])
    df_user.to_csv("df_user.csv")
    st.write(df_user)
    st.write(status)


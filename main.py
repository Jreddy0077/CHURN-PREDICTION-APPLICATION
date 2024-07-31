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

db_user = '2yasPb2k6DKrXZH.root'
db_password = 'E28f3eorNGjxx6K4'
db_host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com'
db_port = '4000'
db_name = 'test'
ca_path = '/path/to/ca_cert.pem'  

# creating the sql syntax for connecting with the database

connection_string = (
    f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?'
    f'ssl_ca={ca_path}&ssl_verify_cert=true'

)

# ca_path 
#  CA certificate is used to verify the identity of the database server to ensure that the connection is secure.

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
        options=["Home", "Prediction Analytics", "Register/Login/Profile","About The Model"],  # required
        icons=["house", "bar-chart", "person-square","robot"],  # optional
         menu_icon="box-arrow-in-right",
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
    
    


elif selected == "Register/Login/Profile":
        
        bg_image_path = r"login_image.jpg"
        
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


        col1, col2 ,col3= st.columns([2,1,3])

        


       



        if option=="Login":
            import streamlit as st
            import pandas as pd
            
            # Assuming l_number and df_user are already defined
            
            with col1:
                st.markdown('<p style="color:gold;">Enter Your Mobile Number..</p>', unsafe_allow_html=True)
                number1 = st.text_input("", key="number1")
            
                # Initialize mobile check
                mobile = False
            
                # Check if the number is in the list
                if number1 in l_number:
                    st.markdown('<p style="color:gold;">Mobile Number Is Correct</p>', unsafe_allow_html=True)
                    mobile = True
                else:
                    st.markdown('<p style="color:gold;">Incorrect Mobile Number</p>', unsafe_allow_html=True)
            
                # UI for password input
                st.markdown('<p style="color:gold;">Enter Your Password..</p>', unsafe_allow_html=True)
                password1 = st.text_input("", key="password1", type="password")
            
                # Initialize password check
                passs = False
            
                if mobile:
                    # Check if the number is present in the DataFrame
                    if number1 in df_user["number"].values:
                        # Get the original password for the entered number
                        password_org = df_user[df_user["number"] == number1]["password"].values[0]
            
                        # Check if the entered password matches the original password
                        if password_org == password1:
                            st.markdown('<p style="color:gold;">Password Is Correct</p>', unsafe_allow_html=True)
                            passs = True
                        else:
                            st.markdown('<p style="color:gold;">Incorrect Password</p>', unsafe_allow_html=True)
                    else:
                        st.markdown('<p style="color:gold;">Mobile Number Not Found in Database</p>', unsafe_allow_html=True)
                
                # Check login button
                if st.button("Login"):
                    if mobile and passs:
                        st.markdown('<p style="color:gold;">Successfully Logged In</p>', unsafe_allow_html=True)
                    else:
                        st.markdown('<p style="color:gold;">Enter The Details Correctly</p>', unsafe_allow_html=True)
            
            with col3:
                if mobile and passs:
                    if st.button("Show Profile"):
                        user_info = df_user[df_user["number"] == number1].iloc[0]
                        name = f"{user_info['first_name']} {user_info['last_name']} {user_info['sur_name']}"
                        mail = user_info['mail']
                        contact = number1
            
                        st.write("     ")
                        st.markdown(f'<h3 style="color:red;">Name: {name}</h3>', unsafe_allow_html=True)
                        st.markdown(f'<h3 style="color:red;">Contact: {contact}</h3>', unsafe_allow_html=True)
                        st.markdown(f'<h3 style="color:red;">Mail: {mail}</h3>', unsafe_allow_html=True)
            
            
                                    
            
                        
                                

        coll1,coll2=st.columns(2)
        if option == "Signup":
            with coll1:
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

               

           

            #with coll2:

                st.markdown('<p style="color:gold;">Enter The Mail</p>', unsafe_allow_html=True)
                mail = st.text_input("", key="maill")

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




                    
                    st.markdown('<p style="color:green;">Successfully Registered</p>', unsafe_allow_html=True)
                else:
                    st.markdown('<p style="color:red;">You Have Entered Something Wrong</p>', unsafe_allow_html=True)




elif selected == "About The Model":
    bg_image_path = r"about.jpeg.jpeg"
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
    # Data for each model
    data_decision_tree = {
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'ROC AUC Score'],
        'Training': [0.972156862745098, 0.975, 0.832, 0.897841726618705, 0.9141609195402298],
        'Testing': [0.9747058823529412, 0.96875, 0.8340807174887892, 0.8963855421686747, 0.9150092145331555]
    }

    data_random_forest = {
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'ROC AUC Score'],
        'Training': [0.9788235294117648, 1.0, 0.856, 0.9224137931034483, 0.9279999999999999],
        'Testing': [0.961764705882353, 0.9817073170731707, 0.7219730941704036, 0.8320413436692508, 0.8599709749795824]
    }

    data_knn = {
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'ROC AUC Score'],
        'Training': [0.8678431372549019, 0.8958333333333334, 0.11466666666666667, 0.20330969267139481, 0.556183908045977],
        'Testing': [0.8747058823529412, 0.8125, 0.05829596412556054, 0.1087866108786611, 0.5281324099571607]
    }

    data_svc = {
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'ROC AUC Score'],
        'Training': [0.8419607843137255, 0.25, 0.037333333333333336, 0.06496519721577727, 0.5090114942528736],
        'Testing': [0.8652941176470588, 0.4117647058823529, 0.06278026905829596, 0.10894941634241245, 0.524619653825018]
    }

    # Creating dataframes
    df_decision_tree = pd.DataFrame(data_decision_tree)
    df_random_forest = pd.DataFrame(data_random_forest)
    df_knn = pd.DataFrame(data_knn)
    df_svc = pd.DataFrame(data_svc)

    # Converting to percentages
    df_decision_tree[['Training', 'Testing']] = df_decision_tree[['Training', 'Testing']] * 100
    df_random_forest[['Training', 'Testing']] = df_random_forest[['Training', 'Testing']] * 100
    df_knn[['Training', 'Testing']] = df_knn[['Training', 'Testing']] * 100
    df_svc[['Training', 'Testing']] = df_svc[['Training', 'Testing']] * 100

    st.markdown("<h1 style='color:gold;'>Decision Tree Performance Metrics</h1>", unsafe_allow_html=True)
    st.dataframe(df_decision_tree, height=300, width=600)
    
    st.markdown("<h1 style='color:gold;'>Random Forest Performance Metrics</h1>", unsafe_allow_html=True)
    st.dataframe(df_random_forest, height=300, width=600)
    
    st.markdown("<h1 style='color:gold;'>K-Nearest Neighbors (KNN) Performance Metrics</h1>", unsafe_allow_html=True)
    st.dataframe(df_knn, height=300, width=600)
    
    st.markdown("<h1 style='color:gold;'>Support Vector Classifier (SVC) Performance Metrics</h1>", unsafe_allow_html=True)
    st.dataframe(df_svc, height=300, width=600)
    
    # Data for all models in one DataFrame
    data = {
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'ROC AUC Score'],
        'Decision Tree': [0.9678431372549021, 0.9580279955595643, 0.8186666666666668, 0.8812063067003717, 0.9150927203065133],
        'Random Forest': [0.943529411764706, 0.9793567209848429, 0.6293333333333333, 0.7658206482488022, 0.913704214559387],
        'KNN': [0.8619607843137256, 0.8880952380952382, 0.07200000000000001, 0.13287531335822061, 0.7268045977011494],
        'SVC': [0.8454901960784313, 0.3094871794871795, 0.04266666666666667, 0.07430479338277116, 0.5222]  # ROC AUC Score is added as a placeholder
    }

    # Creating the DataFrame
    df = pd.DataFrame(data)

    # Converting to percentages
    df[['Decision Tree', 'Random Forest', 'KNN', 'SVC']] = df[['Decision Tree', 'Random Forest', 'KNN', 'SVC']] * 100

    # Displaying data in Streamlit
    st.markdown("<h1 style='color:gold;'>All Models Cross Validation Score(SVC) Performance Metrics</h1>", unsafe_allow_html=True)

    st.dataframe(df)


    st.markdown('<h1 style="color:red;font-weight:bold;">Based On The  Cross Validation Scores We Finallized Decision Tree Model</h1>', unsafe_allow_html=True)

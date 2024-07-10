
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



    
        
    

#result_message_placeholder = st.empty()

# Button to trigger prediction
import streamlit as st


with c1:
    if st.button("Predict", key="submit_2"):
        result2 = model.predict(df2)
        if result2==0:
            output1="** Congratulations! The customer is likely to continue their subscription.**"
            #st.image("data:image/jpeg;base64,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")
        else:
            output1="**Bad luck! The customer is predicted to churn and discontinue their subscription.**"
            #st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAKAAoAMBEQACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABAYBAwUHAv/EADwQAAEDAwEFBQQHBwUAAAAAAAEAAgMEBRESBiExQVETYXGBkRQyQqEHIiMzUsHRFUNiY3Lh8FOSorHx/8QAGgEBAAIDAQAAAAAAAAAAAAAAAAQFAQIGA//EADARAAICAgAEAwcEAwEBAAAAAAABAgMEEQUSITETUWEyQXGRobHRFCJCwSOB8PEz/9oADAMBAAIRAxEAPwD3FAEAQBAEAQBAYyEALgOJQHyZGDi9o81jmRnTAkYeD2nzTaGmfWQsmBkIDOUAQBAEAQBAEAQBAEAQBARauvpqJmqqmZGOWTvPgOa8bsiqlbslo9K6p2vUFsr9btewEtoqcvPJ8hwPRU1/HILpVHfqyxq4Y3/9JaOPNf7tUndO6NvSNoaPXiqy3iuXY+ktL0JsMHHh7t/EhyPrJiTLPI7P4pCVElddP2pP5kiMK49kjT7KerV5crN+Yz7KeWnyTlY5jbG+sh+6nkbj8MhC9o3Xw9mT+Zo4Vy7omQX+7UuA6YyNHKRgPz4qVXxXLg+st/EjzwceXu18Ds0O2ETiG1tOY/42HI9FaUccg+lsdfAg28MkutctlgpK6nrGa6aVkg56TvHiFcVX13LdckyusrnW9SWiSvY0CAIAgCAIAgCA+Xvaxpc5wa0byTwCw5KK2wk29Iql42q96G2eBmI/6H5rn8zjP8aPn+C2x+Hfyt+X5K45s9RIZKiRznH4nnJVDKU7HzTe2WqUYrUUbGRMbwaPEprQ3s+1kwEAQBAEAQHw+JjhwA71q1szto1sE9JIJqaV7Xt4OYcFZhOyuXNB6ElGa5ZLZZLRtUHuENzw08pm8PMfmugw+MqX7L/mVWTw5r91XyLUx7XNDmuBB3ggq+TT7FT27n0sgIAgCAIDXPNHBE+WVwaxgy5x5BaTmoRcpdkbRi5PS7lCvl5musnYw5bTDg3m7vP6Lkc/iM8mXLHpH7/Ev8XEjSty9ohxwtZvO93XooCiSmzYtjAQBAEAQBAEAQBAEBqlhbJvG53XqtXHZlNon2O+S2uUQVJLqUnBbxLO8d3crHA4lLHfJPrH7ETKw43Lmj0l9y9wzMmjZJE4OY8Za4cwuthNTipR7FBKLi+VmxbGAgCAwThYYKLtPd3V9T7LTH7CN2/HxuHPwXK8VzndPwoeyvqXuDjKuPiS7s50UYjbu58SqtLROfU+1kwEAJABLjgDmUByGbR0DqsU4Mm92ntC36mfXPmrB8MyFDn+n/dCOsmDlynXVeSAgCAIDkP2ioWVhpndoMHSZNI0g+uVYR4be6+da+HvI/6qClynWBBGQQQeYVeSEZQBAa5oxI3HxDgVrJbMp6Opstd3UVSKOpP2Mjvqk/A4/kVbcKzvBl4U/Zf0/wDSBn4viR8SHdF4ByuqKMygCA4e1dx9it/ZxnE0+WjfwHM/51VXxXK8GjlXeXQm4NHi2bfZFLpo8N18CVyUUX8mb1uahAcS9X79m1Ap4oBLJpDnEnAHRWWHw/8AUQ55PSIt+R4b5UupXrhe62vaY5HiOI8WRjAPiVb0YNND2ur9SHPInPo+xmxWuS4VTXOaRTxuy93XuCxm5aog0n+5+7+zNFTnL0L2uXLUIAgH+YQFFv1rfb6tzmguppDlr8ZwehXUYOUroJfyRU31OEvQ+bdfKygaI43CSEfA/eB4FZvwab3zNafoK751rSLDZL9+0ag08sAifpy0tOQf0VRmcP8A08OeL2iZTk+JLla0dtVpKCA0VLN2scea0kuuzZMuuy1z9ut4ZI4meHDX54kciuu4Xl/qKdS7x6FBnUeFbtdmdtWZCMO4IDz7aGqNdepADmOM6G+XH55XG8Uvd2S0uy6L+zosKrwqF5sjgYAAUPRIMoAgOZdLJTXGQSvfJHIBjUwjeO/Km42dZjrlXVHhbjxse2RqfZihieHSvlmx8LiAPkvazit8lqOkaRxK09vqdqKNkMbY4mNYxu4NaMAKulKU3zSe2SVFRWkfS1MhAEAQHzJGyWN0crGvY7i1wyCtoycXuL0zDimtM4tRsxQSuzG6WHPwsII+asYcVvitNJkaWJBva6Ei1WOmtspljdJJKRgOfjcO5eWTnWZEeV9Eb1Y8a3tHUUE9wgBGQQeBTQN+zlUaG8xtc7Ecv2bvPh81M4Xe6clJ9n0/BHzqvEofmj0EcF2Rzpor5xTUU85/dsLvkvK6zw65T8kb1Q55qPmea0wLnue4kkjj3lcGtt7Z1L6LRJW5qEAQBAEAQBAEAQBAEAQBAEAQBARqkFsjXtOHcc9CFpLo9o2XXoelUE4qaKCf/UjDvULvKbPErjPzRy1kOSbj5HP2rl7OxVH8Zaz1Kh8Vny4ktEnAjvIiUimH2eepXIR7HQM3LY1CAIAgCAIAgCAIAgCAIAgCAIAgNNUMx56Faz7GV3LtsnKZLJBn4C5voV13Cp8+LH06FBnx5b2Rttji0xgc5wP+LivDjjaxlr3tfZnpwxbufw/BVKf7kea5iHYu33Ni2MBAEAQHJvO0drs7hHWTntiARFGNTgOpHLzUzHwb8hbgunm+hHtyqqekmabVtXaLpO2CCd0czvdjmbpLvDlnuW9/Dsihc0ltenU1qzKbXyp9fU7igEoIAgCA4d12stFrndBPO6SZvvMhbqLe48ge5T6OG5F0eZLS9SLbmVVvTe36dTdZ9o7ZeCWUdR9sBkxSDS7HcDx8lpk4N+OtzXTzRtTlV3eyzrKGSAgCAIDVU/cuWs+xldy2bEnNqkBPuzuA9Grp+BtvGe/N/ZFLxNf5l8P7Y22BNpjI5TtJ/wBrk42t4y9GvszHDH/mfw/BVKb7lvmuYj2Lt9zYttmAmwE2CLdawW+11dYRnsIXSY6kDI+a9aK/FtjWvezzunyVuXkeJzzSVE8k87y+WRxe9xPEldvGMYJRitJHNSbk22axuOQSCOBBwQtjB7JspcX3Ww0tVKcykFkh6uadJPnjPmuNz6FRkShHt7v9nRYtjsqUmdZQ9kgJsHI2ruL7VYaqqhJEuAyM9HOOM/PPkpeDTG/IjCXYj5VjrqbR454kk9SeK7M502U80tNPHPA8sljcHMcDwIWsoRnFwl2ZmLcWpLuj2y11Yr7ZSVgGBPCyTHQkZwuIvr8K2Vfk9HTVT54KXmSl5bNwmwE2DXU/cuWs30MruWvYgYtMpPOdxHo1dPwNaxn8X9kUvE3u5fD+2Stq4u0sc+OLS13oQpHFYc2JLXuPLAly3xKXRb4sdCuPj2L6b6kjSsmmxpQbGlBs5+0VFJXWG4UsIzJLTvawfxY3fNScSxV5EJvsmjyvTnVKK8jxDyx3Hku3OdCA9f2Don0my9I2UYdIXS4xyc4kfLC4/ilqsypOPu6fIvcOLhSkywaVXkrY0oNle29o5KrZeqEQy6Islxjk05PyyrHhdkYZUeb37XzIubFypejyFdeUQ8ifBAe4bP0T6Gx2+lm+8ip2Nfj8WN/zXD5VqtvnNdm2dFQuSuMX7kT9KjnrsaUGxpQbI9d9WId5wtZdjeHcueykRjskGRjWXP8AUrsOEw5MWPr1KHPlzXs6NwgFVRTwH94wtHiQpt1fiVyh5ojVT5JqXked27IlfE4YON47xuXAvcXpnTWezsn6FnZ5bGhNjY0JsbGhNmNlN2i2AguVTJV2+dtJNKdUjHN1Mceu7h5K5xOMyqioWrmS+ZBuw1N80Hpkaz/RvFBUNlu1U2paDnsY2lrT4k8u5emRxxyjy1R16v8ABrVg6e5vZewzAxuA6BUW9lgug0JszsaE2NgsBGCAQdxBCc2uxhlDvH0bRzTultFW2mY45MMrS5rfAjeB3K+x+OOMdXR2/NFfbg7e4P5krZzYCC21LKu4zirnjOqNjW6WNPI9SQvLL4xK6LhWuVP5m1OEoPmk9ly0dVTbJ2xoTZnY0JsbGhNjZz7jl0zI27z0HUrGnJ6R61vScmejUMApqKCAfu4w30C76mtV1xgvcjmbJ883LzNx4L1NDz+/05t17fI0YikPaM8+I9crjOKY/hZL12fU6HDsVuOl70Sw0OaC0gg7weoVcY213M6EGxoQbGhBsaEGxoQbItwr6G2Qia4VUNPGeBkeBnuHU+C9aqbbXy1xbZpK2MfaZWqr6RLBA8tjNTUYOMxw7vnhWUOC5Uu+l/v8Ed5ta8xS/SHYZ3BshqYM85IsgemVifBcqPbT/wBhZ1b8yyW64UFzh7a31cFRHwJieHYPQjkq62i2l8tkWn6kiNkZeyyXoXkb7GhBsaEGxoQbGhBsw4BrS524AZKDZF2epjcL42Rw+zjPaO8PhHrj0VlwqjxchP3R6mcyzwqNe9noA4LsjnggOJtVbfbqDXE3M0OXNA4kcx/nRVnFMXx6enePVE3Bv8Kzr2ZWbNUdo3sHcW72d4XGstr4afMjqaFjZH2Y0JsbGhNjY0JsbKhtxtlFYB7FRBk1ye0HDvdhB5u6nu9e+24bw2WV++fSH1fwI1+RydF3PIa6tq7hUuqa+olnmdxfIcny5AdwXWV111R5a1pFdKTk9yIzHB7i1h1EcQ3fhej6dzBl5DCGv+qTwDt2VnqwSKGuqrfUtqaGplp5m8Hxux69R3FeVtULY8k1tGYycXuLPXdhtsor+BRVwZDcmNJw33ZgObeh6hcpxLhssb/JDrD7FjRkc/R9y4aFUbJOxoTY2NCbGxoTY2cu81Glvs7PeO92OQ6LZdSTRDf7mWnZe2+wW8OkbiabDn54gcguy4Zifp6evtPqyozr/Fs6dkdlWRCCAwRlAUjaW1Pt1X7bSfVhe7Jx+7d+hXKcVwPCl4sF+1/Rl5hZKuh4c+/3N9uq2VkOoYEg99vT+yommhbW636ErSsHlszpQyRLtUSUVrq6qGIzSQwveyNoyXkDcF649attjBvSbRrJtRejxmw7H3vaqpfXVOqCGV5fLVVDTl7jx0t4n5ALsMriONhR5I9WuyX9sr4VSse30PR7P9H2z9sYO0pvbpeJkq8Oyf6fdA8lz2RxjKufR8q9Pz3+pKjjwiWWGlggYGQQxRtAwAxgaB6KtlZKT3J7PZJITUlPO0tngilaeLXsDh80jZKPWL0Gk+5Wrx9Huz9yYezpvYZTwlpMN3/0+6fRWWPxjKpfWXMvJ/8AbPKVEJHm+0Gxt72WqY62mLqiGKQPiqaZp1MI3jU3iPmF0OLxLGzIOuXRvum+j+DIk6p1vaPZrPUSV1po6yaF0Mk8DJHxuGC0kAkYXIZFaqtlCL2kyfCTa2yZpXibjSgIdxrGUcOdzpXe6381mO2etVbsfoatmLU+vqvbqoaomOy3Pxu/QK+4TgeLLxp+yu3qzXOyVVHwod/sXYDC6opDKAIAgNc0Mc0T45Wh7HjDmngVrOEZxcZLaMxk4va7lFu9oqbNUCppNToM/VfxLe5y5HiHDZY75o9YfYvsfKhkR5Z9/wDuxLt9ziqxpd9nL+EncfBU7jo1splDt1RPWp4mEBlBowgCAIAgMjdwWQYWAEBAuF0ipQWMxJL05DxWyie1VEp9+xGs9mnu0/tNWXCDO9x3F/cO5XPDuGyyHzz6R+5nKyoUR5IdWXmGJkUbGRtDWNGGtHILrYxUUlHsUUm5Pb7mxbGAgCAIAgPl7A9pa5oLTuII3FYaTWmE2uqKpd9lN5mte4/6JPDwKoMzg2/30fItsfiP8bfmciG51dC8wVsTnaeTxhw/Vc5ZTKEuWa0yc6YWLmrf4OrTXGlnwGyhrvwv3FeTi0RpVTj3RKWDzCwAgCAysgxw4rAItTcaWnyHSBzh8LN5WyiekaZy9xypbhWXCQQUUThq+Fm9x8+S9aqZ2S5YLbJKqrqXNYzs2jZQNImuRDncexG8eZ5rpMPgyj++/r6fkgZHEd/tq+ZaWNDWhoaABuACvkklpFUfSyAgCAIAgCAIAgI1XQU1YzRVQskHLI3jwPJeN2PVctWR2elds63uD0V6u2QjJLqKoLf5coyPX/1U1/A4PrVLXxLGvikl0mvkct9nvlD902R7esT9Q9P7Krt4TlQfs7+BLWXi2dzS6vulPunidu/HEQoMsWyPtRa/0eiqon7L+pj9vTDjFET5ry5UP0kfMG/zcoogfNOVD9JHzMiuulRuhhcc/giJXtHGsl0jFh1Uw9p/U3Ms18rsGVr2M/mv0j0H6KbXwnKn/HXxPN5eLV26/A6tBshECHVtQZP4IxpHqrWjgcIvdst/QiWcUk+kFosNJRU9HHopomRt56W8fFXNVFdK5YR0Vtls7Hub2SF6mgQBAEAQBAEAQBAEAQBAYwEAwOiA+ezjPFjfRY0jPM/MCKMcGN9E0hzPzPrA6LJgYCAygCAIAgCAIAgP/9k=")
        st.write(output1)



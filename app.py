import time
import streamlit as st

# Set the title of the app
st.set_page_config(page_title='Streamlit Chatbot')
st.title("Streamlit Chatbot")

def create_new_input(input_key, session_data, input_value):
    numeric_keys = [int(k) for k in session_data.keys() if k.isdigit()]
    max_key = max(numeric_keys) if numeric_keys else 0
    input_key = min(int(input_key), max_key)
    next_key = str(int(input_key) + 1)
    session_data[next_key] = input_value
    return int(next_key)

def is_max_key(input_key, session_data):
    numeric_keys = [int(k) for k in session_data.keys() if k.isdigit()]
    max_key = max(numeric_keys) if numeric_keys else 0
    return max_key == input_key

def get_new_input(input_key, is_disabled):
    message = "Enter your query here:" if input_key == '0' else "Continue the conversation:"
    user_input = st.text_input(message, value=st.session_state.get(input_key, ''), key=input_key, disabled=is_disabled)
    return user_input

input_key = '0'
input_key = create_new_input(input_key, st.session_state, get_new_input(input_key, is_disabled=input_key in st.session_state))

while st.session_state.get(input_key):
    if is_max_key(input_key, st.session_state):
        with st.spinner('Downloading data...'):
            time.sleep(0.7)
        with st.spinner('Parsing results...'):
            time.sleep(0.7)
    st.markdown(f"You asked: {st.session_state.get(input_key)}, and my answer is: Chatum solutio, intellegentia artificiosa praeditus, aperio consilium. Conloquium interretiale, quaestiones responsionesque simulans, peritia machinamentum. Textum analysans, contextum comprehendens, apta responsio generatur.")
    input_key = f"{int(input_key) + 1}"
    input_key = create_new_input(input_key, st.session_state, get_new_input(input_key, is_disabled=input_key in st.session_state))

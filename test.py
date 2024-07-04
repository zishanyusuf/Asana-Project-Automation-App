import requests 
import streamlit as st

#Render Title of the Web Page
st.write("""
## ASANA API Access - Network Planning OP 2025
""")

## Render a prefilled Project ID
# Set a default value for the Project ID
default_project_id = 1206713753906403
# Create a number input field with a pre-filled Project ID
project_id = st.number_input("**Enter Project ID:**", value=default_project_id, step=1, format="%d")

## Render a field to enter Access ID 
access_id = st.text_input("**Enter ASANA access ID:**") 

ASANA_BASE_TASK_URL = "https://app.asana.com/api/1.0/tasks"
#Access the link for the ASANA: https://app.asana.com/0/1207638669590015/1207638670232784
#PROJECT_ID = "1207638669590015" # This is hardcoded for the purpose of this  example, but I would recommend grabbing the ID you want from an additional API call
# PROJECT_ID = "1206713753906403"
PROJECT_ID = project_id
# personal_access_token = "2/1195781365485212/1207621405062976:08cb575f0db7c127e6f3a4457568453b" # Grab this from env variables or secrets where you saved it!
personal_access_token = access_id
headers = {
   "Authorization": f"Bearer {personal_access_token}"}

url = f"{ASANA_BASE_TASK_URL}?project={PROJECT_ID}&opt_fields=name,permalink_url,custom_fields.name,custom_fields.display_value"
# This constructed URL should look something like this: https://app.asana.com/api/1.0/tasks?project=1202095602265837

# tasks = ""
#Make an API call and Fetch data
#Add a spinning circle loading symbol meanwhile the API connections are being established 
if st.button("Connect to ASANA", help="Click to establish the API connections!"):
    with st.spinner('Processing...'): 
    # Make the API Request. Note the .get() function, which corresponds to the HTTP GET method of our request
        response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tasks = response.json()
        st.success(f"The API connection was successful")
        json_data = tasks
        json_data_cleaned = json_data['data']
        st.write(json_data_cleaned)
    else:
        st.error(f"Failed to make an API connection. <Status code: {response.status_code}>")
    # tasks = response.json()
     
def process_data():
    


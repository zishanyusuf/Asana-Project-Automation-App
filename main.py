# Streamlit App to access ASANA API and Download the Excel File
#Import required Libraries
import streamlit as st
import numpy as np
import pandas as pd
import io
import xlsxwriter
import requests
import json
import time

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

#######################################################
#API Access to ASANA
#######################################################
ASANA_BASE_TASK_URL = "https://app.asana.com/api/1.0/tasks"
#Access the link for the ASANA: https://app.asana.com/0/1207638669590015/1207638670232784
#PROJECT_ID = "1207638669590015" # This is hardcoded for the purpose of this  example, but I would recommend grabbing the ID you want from an additional API call
#PROJECT_ID = "1206713753906403"
PROJECT_ID = project_id
#personal_access_token = "2/1195781365485212/1207621405062976:08cb575f0db7c127e6f3a4457568453b" # Grab this from env variables or secrets where you saved it!
personal_access_token = access_id
headers = {
   "Authorization": f"Bearer {personal_access_token}"}

url = f"{ASANA_BASE_TASK_URL}?project={PROJECT_ID}&opt_fields=name,permalink_url,custom_fields.name,custom_fields.display_value"
# This constructed URL should look something like this: https://app.asana.com/api/1.0/tasks?project=1202095602265837


#Add a spinning circle loading symbol meanwhile the API connections are being established 
def fetch_data():
 with st.spinner('Processing...'): 
 # Make the API Request. Note the .get() function, which corresponds to the HTTP GET method of our request
  api_data = requests.get(url, headers=headers)
 return api_data


tasks = ""
#Add a button to allow users to click to trigger the API connection
if st.button("Connect to ASANA", help="Click to establish the API connections!"):
 response = fetch_data()
 # If the status code is 200, it means the request was successful
 if response.status_code == 200:
   tasks = response.json()
   #print("The Access to the API was successful")
   st.success(f"The API connection was successful")
   # After this -- you can do whatever you want with the tasks that is useful to you!
  # If status code is not 200, print an error message since something went wrong
 else:
   #print(f"Failed to retrieve tasks. Status code: {response.status_code}")
   st.error(f"Failed to make an API connection. <Status code: {response.status_code}>")
   
   
#######################################################
#Load the returned JSON file from API and convert it into required dataframe
#######################################################
#Load the extracted json file in separate variable
json_data = tasks
json_data = json.dumps(json_data)
json_data = json.loads(json_data)
#The JSON data contains additional keyword namely 'data' in the beginning. Let's first remove it
json_data_cleaned = json_data['data']
# json_data_cleaned = json_data[list(json_data.keys())[0]]
#json_data_cleaned = next(iter(json_data.values()))
#json_data_cleaned = json.loads(json_data['data'])
#json_data_cleaned = json_data[1]
# First of all extract all the Custom Fields from JSON file. Flatten the 'custom_fields' columns
json_data_normalized = pd.json_normalize(json_data_cleaned, record_path=['custom_fields'])

unique_gid = json_data_normalized['gid'].unique()
unique_gid
custom_field_data = pd.DataFrame()
for gid_value in unique_gid:
    #Extract the data for each gid and pivot it to get rows as column
    pivoted_data = json_data_normalized[json_data_normalized['gid'] == gid_value].pivot(columns="name", values='display_value')
    #print(pivoted_data)
    ##Start preparing the data to combine all the Data togethetr for each GID
    #Reset the index of the Pivoted data, so merge can happen on the reset index; to avoid extra rows creations
    pivoted_data = pivoted_data.reset_index()
    #Drop the extra Index column that resulted due to reseting the index
    pivoted_data = pivoted_data.drop(pivoted_data.columns[0], axis=1)
    ##Combine all the pivoted data for each gid
    custom_field_data = pd.concat([custom_field_data, pivoted_data], axis=1)
    
#Read the ASANA Project items' main field like title and URL etc. 
intake_title_data = pd.json_normalize(json_data_cleaned)[['name','permalink_url']].rename(columns={'name':'Request Heading', 'permalink_url':'Request_Link'})

#Combine the Intake Title dataframe and Custom Field dataframe
intake_data = pd.concat([intake_title_data, custom_field_data], axis=1)



# Example data
#data = {'Name': ['Alice', 'Bob', 'Charlie'],
#        'Age': [25, 30, 35],
#        'City': ['New York', 'London', 'Paris']}

#df = pd.DataFrame(data)
df = intake_data
# Streamlit app
st.subheader("Download OP Intake from ASANA in Excel Format")

if st.button("Prepare Excel File"):
    # Convert the DataFrame to an in-memory Excel file
    excel_file = io.BytesIO()
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    
    # Set the download button attributes
    st.download_button(
        label="Download Excel HERE",
        data=excel_file.getvalue(),
        file_name="OP_2025_NMT_Intake.xlsx",
        mime="application/vnd.ms-excel"
    )
    
    st.success("Excel file Prepared successfully!")

#Define methods to import unistalled libraries
import importlib

def install_package(package):
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])

# Example usage
install_package('pandas')
install_package('numpy')
install_package('requests')
install_package('streamlit')
install_package('xlsxwriter')

#Import required libraries
import pandas as pd
import numpy as np
import requests #Library for API Calls
import streamlit as st
import io
import xlsxwriter

#Render Title of the Web Page
st.write("""
## ASANA Project Automation - API Access
""")

## Render a prefilled Project ID
# Set a default value for the Project ID
# Create a number input field with a pre-filled Project ID
project_id = st.number_input("**Enter Project ID:**", step=1, format="%d")

## Render a field to enter Access ID 
access_id = st.text_input("**Enter ASANA access ID:**") 

ASANA_BASE_TASK_URL = "https://app.asana.com/api/1.0/tasks"
PROJECT_ID = project_id
personal_access_token = access_id
headers = {
   "Authorization": f"Bearer {personal_access_token}"}

url = f"{ASANA_BASE_TASK_URL}?project={PROJECT_ID}&opt_fields=name,permalink_url,custom_fields.name,custom_fields.display_value"

#Define function to processing the data accessed from the API call
def process_data(input_data):
    json_data = tasks
    json_data_cleaned = json_data['data']
    # First of all extract all the Custom Fields from JSON file. Flatten the 'custom_fields' columns
    json_data_normalized = pd.json_normalize(json_data_cleaned, record_path=['custom_fields'])
    #Let's begin extraction of the Custom Field elements - We need to extract it from each GID record of the json file
    unique_gid = json_data_normalized['gid'].unique()
    custom_field_data = pd.DataFrame()
    for gid_value in unique_gid:
        #Extract the data for each gid and pivot it to get rows as column
        pivoted_data = json_data_normalized[json_data_normalized['gid'] == gid_value].pivot(columns="name", values='display_value')
        ##Start preparing the data to combine all the Data together for each GID
        #Reset the index of the Pivoted data, so merge/JOIN can happen on the reset index; to avoid extra rows creations
        pivoted_data = pivoted_data.reset_index()
        #Drop the extra Index column that resulted due to reseting the index
        pivoted_data = pivoted_data.drop(pivoted_data.columns[0], axis=1)
        ##Combine all the pivoted data for each gid
        custom_field_data = pd.concat([custom_field_data, pivoted_data], axis=1)
    
    ##Let's begin extraction of the Main Field data from JSON, e.g., Task Name, URL, Due Date, etc.
    #Read the ASANA Project items' main field like title and URL etc. 
    intake_title_data = pd.json_normalize(json_data_cleaned)[['name','permalink_url']].rename(columns={'name':'Request Heading', 'permalink_url':'Request_Link'})
    #Combine the Intake Title dataframe and Custom Field dataframe
    final_data = pd.concat([intake_title_data, custom_field_data], axis=1)
    #Remove duplicate columns, if any
    final_data = final_data.loc[:, ~final_data.columns.duplicated()]
        
    ##Return the final dataframe
    return final_data

#Make an API call and Fetch data
#Add a spinning circle loading symbol meanwhile the API connections are being established 
if st.button("Connect to ASANA", help="Click to establish the API connections!"):
    with st.spinner('Processing...'): 
    # Make the API Request. Note the .get() function, which corresponds to the HTTP GET method of our request
        response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tasks = response.json()
        st.success(f"The API connection was successful")
        asana_project_data = process_data(tasks)
        st.write(asana_project_data)

        #Begin preparing for excel data download
        asana_project_excel_data = pd.DataFrame(asana_project_data)
        # if st.button("Prepare Excel File1"):
            # Convert the DataFrame to an in-memory Excel file
        excel_file = io.BytesIO()
        with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
            asana_project_excel_data.to_excel(writer, index=False, sheet_name='Sheet1')
            
        # Set the download button attributes
        st.download_button(
                label="Download Excel HERE",
                data=excel_file.getvalue(),
                file_name="OP_2025_NMT_Intake.xlsx",
                mime="application/vnd.ms-excel"
            )
            
        st.success("Excel file Prepared successfully!")
                        
    else:
        st.error(f"Failed to make an API connection. <Status code: {response.status_code}>")

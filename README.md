### Introduction ###
This is an APP to access ASANA Project Data to drive Project Management automation with Python. It provides users an interactive customized web user interactions with potential to augment it in fast paced business setup. APP can be used in the following manner.
* Automation for repetitive project management activities (large scale data extraction, manipulations, update etc.).
* Leverage High level python framework for quick customized Project dashboards for leadership
* Demonstrates the potential integration with LLM model of one's own choice 
* Empowers business and Project Managers to take control of their project in their MS Office setup 

### Details and Use cases ###
The APP accesses the ASANA programatically and uses Python to persist the JSON response. JSON files is further processed with Pandas to build the required dataframe for ALL the custom fields defined by users. It is further joined by column for tasks' Name and URL. For further processing Streamlit is used to render the Web UI to allow users to input the Access ID and project ID to be able to exc
on top of it demonstrates ability to build applications with 

allows users to establish an API connection with ASANA Projects using API parameters. 

### Users Interactions ###

<img width="786" alt="ASANA Webhook UI" src="https://github.com/zishanyusuf/Asana-Project-Automation-App/assets/24717778/75984780-e3a8-45d5-87b5-e40a289194cd">

### FAQs ###
**1. Does the APP extract tasks from Portfolio too?**
The APP extracts the data from Project folder, not from the Portfolios.

**2. How do i access the Project ID?**
A typical project Browser URL for ASANA follows the following format.
https://app.asana.com/0/12345678901112/1314151617181929
The first ID is the Project ID. For example, in this toy URL the first ID is: 12345678901112

**2. Where do i get the Access ID?**
If one has an access to ASANA then Access ID can be generated from ASANA by following instruction in this page: https://developers.asana.com/docs/personal-access-token
The Access ID is Personal Access Token (PAT)


provided using Python and Streamlit.  and showcases the potential opportunities of Project Automation using Python and ASANA. The app especially demonstrates the 
extraction of all the custom fields created by users and it joins the default two field: name and tasks' URL.
and demonstrate the data extractions in Excel format for the   

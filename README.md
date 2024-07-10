### Introduction ###
This is an application designed to seamlessly integrate with Asana's project management platform, enabling Project Managers and business leaders to streamline their operations through automation and data-driven insights. Powered by Python, this robust solution provides a user-friendly web interface, facilitating efficient interactions and customizations tailored to the fast-paced demands of modern businesses.

The application's core functionality revolves around the following key features:
1. **Automation for Repetitive Project Management Activities**: Leveraging Python's versatility, the application automates tedious and time-consuming tasks such as large-scale data extraction, manipulation, and updates. This empowers Project Managers to focus on strategic decision-making while ensuring consistent and accurate execution of routine operations.
2. **Customized Project Dashboards for Leadership**: Harnessing the power of high-level Python frameworks, the application generates dynamic and visually appealing project dashboards. These dashboards provide a comprehensive overview of project performance, enabling leadership to make informed decisions based on real-time data insights.
3. **Integration with Large Language Models (LLMs)**: Recognizing the potential of cutting-edge AI technologies, the application opens up possibilities of seamlessly integrate with LLMs of your choice. This integration opens up new avenues for intelligent task automation, natural language processing, and data-driven decision support, further enhancing project management capabilities.
4. **Seamless Integration with Microsoft Office Suite**: Designed with user convenience in mind, the application seamlessly integrates with the widely adopted Microsoft Office suite. This integration ensures a familiar and intuitive experience for Project Managers and business users, minimizing the learning curve and promoting rapid adoption within existing workflows.

### Technical Detail ###
The application establishes a programmatic connection with Asana, leveraging Python to retrieve and persist the JSON responses obtained from the platform. The JSON files are further processed using the powerful Pandas library, which enables the construction of custom dataframes tailored to the specific fields defined by users. These dataframes are then enriched by incorporating additional columns for task names and URLs, providing a comprehensive view of project data.

To facilitate user interaction and personalized access, the application employs Streamlit, a popular Python library for building interactive web applications. Through Streamlit's intuitive web user interface (UI), users can input their Access ID and project ID, allowing them to securely connect to their specific Asana projects using their own credentials.

This seamless integration between Asana's project management capabilities, Python's data manipulation prowess, and Streamlit's user-friendly web interface empowers users to gain granular insights into their projects, enabling data-driven decision-making and streamlined project management workflows.

### Users Interactions and case Detail ###
1. Fork the app from GitHub to your local machine and run on python platform
`streamlit run Asana_API_App.py`
2. It will open the app in browser
3. Click on the button “Connect to ASANA”
4. Allow the app to establish an API connection and wait for few seconds more
5. It will load a data table. Below the data table, you will find a button to download the Excel
6. It exctracts all the field defined by users and along with default field like URL and Task Name
7. The dataframe can be used to generate reports, or further connect and process with GenAI service/LLMs
<img width="662" alt="ASANA App UI" src="https://github.com/zishanyusuf/Asana-Project-Automation-App/assets/24717778/c85c1a30-beae-43f2-b48b-51354a789277">

### FAQs ###
**1. Does the APP extract tasks from Portfolio too?**

The APP extracts the data from ASANA Project folder, not from the ASANA Portfolios. However, with small changes in the code, one can access the portfolio too.

**2. How do i access the Project ID?**
A typical project Browser URL for ASANA follows the following format.
https://app.asana.com/0/12345678901112/1314151617181929
The first ID is the Project ID. For example, in this toy URL the first ID is: 12345678901112
<img width="1124" alt="Screenshot 2024-07-10 at 09 24 30" src="https://github.com/zishanyusuf/Asana-Project-Automation-App/assets/24717778/afc46700-542f-49ee-a3cd-ac35c7b3b43e">

**2. Where do i get the Access ID?**
If one has an access to ASANA then Access ID can be generated from ASANA by following instruction in this page: https://developers.asana.com/docs/personal-access-token
The Access ID is Personal Access Token (PAT)
<img width="1124" alt="Screenshot 2024-07-10 at 10 15 08" src="https://github.com/zishanyusuf/Asana-Project-Automation-App/assets/24717778/ee796fec-5726-4f4f-8a06-4b39fe77fe3d">
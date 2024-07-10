### Introduction ###
This is an application designed to seamlessly integrate with Asana's project management platform, enabling Project Managers and business leaders to streamline their operations through automation and data-driven insights. Powered by Python, this robust solution provides a user-friendly web interface, facilitating efficient interactions and customizations tailored to the fast-paced demands of modern businesses.

The application's core functionality revolves around the following key features:
1. **Automation for Repetitive Project Management Activities**: Leveraging Python's versatility, the application automates tedious and time-consuming tasks such as large-scale data extraction, manipulation, and updates. This empowers Project Managers to focus on strategic decision-making while ensuring consistent and accurate execution of routine operations.
2. **Customized Project Dashboards for Leadership**: Harnessing the power of high-level Python frameworks, the application generates dynamic and visually appealing project dashboards. These dashboards provide a comprehensive overview of project performance, enabling leadership to make informed decisions based on real-time data insights.
3. **Integration with Large Language Models (LLMs)**: Recognizing the potential of cutting-edge AI technologies, the application opens up possibilities of seamlessly integrate with LLMs of your choice. This integration opens up new avenues for intelligent task automation, natural language processing, and data-driven decision support, further enhancing project management capabilities.
4. **Seamless Integration with Microsoft Office Suite**: Designed with user convenience in mind, the application seamlessly integrates with the widely adopted Microsoft Office suite. This integration ensures a familiar and intuitive experience for Project Managers and business users, minimizing the learning curve and promoting rapid adoption within existing workflows.

### Details and Use cases ###
The APP accesses the ASANA programatically and uses Python to persist the JSON response. JSON files is further processed with Pandas to build the required dataframe for ALL the custom fields defined by users. It is further joined by column for tasks' Name and URL. Streamlit is used to render the Web UI to allow users to input the Access ID and project ID to be able to connect to the specific ASANA project with thier own credentials.
 
### Users Interactions ###

<img width="662" alt="ASANA App UI" src="https://github.com/zishanyusuf/Asana-Project-Automation-App/assets/24717778/c85c1a30-beae-43f2-b48b-51354a789277">

### FAQs ###
**1. Does the APP extract tasks from Portfolio too?**

The APP extracts the data from Project folder, not from the Portfolios.

**2. How do i access the Project ID?**
A typical project Browser URL for ASANA follows the following format.
https://app.asana.com/0/12345678901112/1314151617181929
The first ID is the Project ID. For example, in this toy URL the first ID is: 12345678901112
<img width="1124" alt="Screenshot 2024-07-10 at 09 24 30" src="https://github.com/zishanyusuf/Asana-Project-Automation-App/assets/24717778/afc46700-542f-49ee-a3cd-ac35c7b3b43e">

**2. Where do i get the Access ID?**
If one has an access to ASANA then Access ID can be generated from ASANA by following instruction in this page: https://developers.asana.com/docs/personal-access-token
The Access ID is Personal Access Token (PAT)
<img width="1124" alt="Screenshot 2024-07-10 at 10 15 08" src="https://github.com/zishanyusuf/Asana-Project-Automation-App/assets/24717778/ee796fec-5726-4f4f-8a06-4b39fe77fe3d">

provided using Python and Streamlit.  and showcases the potential opportunities of Project Automation using Python and ASANA. The app especially demonstrates the 
extraction of all the custom fields created by users and it joins the default two field: name and tasks' URL.
and demonstrate the data extractions in Excel format for the   

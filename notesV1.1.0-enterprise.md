[Version: 1.1.0-enterprise]
- DONE Setup New Branch

- Dashboard
    - DONE Change total Clients to no. of list
    - Task List
        - Visible to Owner and Assignee
    - Recent Activities
        - Owner / Current

- Contacts
    - DONE Change 'Contacts' to 'Leads' (in frontend)
    - ONGOING Add Dropdown for Search Bar
        - DONE Implement AJAX
        - Adapt with Theme
    - ONGOING Add filter ['by list'; 'by date created'; 'other']
    - DONE Custom Column
        - DONE Add Pop Up Window
        - DONE Implement Dragger
        - DONE Working Save Button
        - DONE Create Model to save changes
        - DONE Add Reset Button
    - Add JS for smooth 'list search' and 'contact search'

    - Add option to add more fields in Client data

- Add Upload CSV
    - Add 'Upload CSV' to Model
    - Create a Form for CSV Upload
    - View to Handle CSV Upload
    - Template for CSV Upload
    - URL Routing
    - Error Handling and User Feedback

- Add Download CSV
    - For Future

- Add Option for Custom Field in Client Model
    - Creating New model - ClientCustomField (store the key-value pairs for custom field)
        - Fields [Key; Value; Client(Connect with Client Model - the instance);]
    - Add model to admin.py (accessible from admin page)
    - Migrate the Changes
    - Create Form for this model
    - Update the UI to add more fields!
    - Update in Client Creation Form
    - Update the UI for Contact Detailed View

- Tasks
    - Task Creation Form
        - Add field 'List'
        - Filter Contact by List
            - Can't be choose until List is selected
            - Show Contacts based on current List
            - Contact Can be Empty
    - Add 'In Progress' Button for 'New' tasksw

- Roles
    - Add roles [Manager; Senior Executive; Executive;]
        - Default Settings

- DONE Add Outlook Authentication
    - Check if it works for Multiple Account

- Add Max File Size
    - Limit User to Upload file more than 20 MB
        - DONE Updating Django Setting
        - ONGOING JavaScript (Restrict File, before Uploading)
    - Error Message to User

- Migrate to PostgreSQL

- Secure
- Update Bootstrap
- Add 'Two Factor Authentication'
- Testing FrontEnd
- Django Internal Testing

<!--
- Git Command For this specific version
git checkout -b feature/enterprise-updates

git add .
git commit -m "Enterprise-specific updates"

git checkout main
git merge feature/enterprise-updates

git push origin main

git tag v1.1.0-enterprise
git push origin v1.1.0-enterprise
-->
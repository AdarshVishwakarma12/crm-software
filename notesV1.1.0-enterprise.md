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
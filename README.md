# RealTimeChat
A mini real time chatting app using [Django Channels](http://channels.readthedocs.io/en/stable/).

### Assumptions
* All users chats through the same room
* There are no permissions between users
* No database (except for django sessions), just sending and receiving messages


### Instruction for deploying the project

- Open terminal and change directory to whatever you want  
- Clone the project  
`git clone https://github.com/islambayoumy/RealTimeChat`
- change directory to project folder  
`cd RealTimeChat`
- A file "requirements.txt" is attached with all the required dependencies
`pip install -r requirements.txt`
- Run the development server 
`python manage.py runserver`
- Now you can browse the application through http://127.0.0.1:8000/chat/

### Using the application
1. Sign Up to create an account
2. Login with the created account   
~ for first time you will not see users list as you are the only user in the system
3. Open another browser (if you are using chrome, just open new incognito tab) and go to http://127.0.0.1:8000/chat
4. Repeat 1, 2 & 3 as many as you want more accounts to be registered
5. Yous messages are being send to all other users in a realtime

# This file is where you keep secret settings, passwords, and tokens!
# If you put them in the code you risk committing that info or sharing it
# important one is the session_token in order to login into AoC.  You can
# retrieve this cookie from the Developer viewer in a browser logged into AoC
# Under Storage->Cookies->session
 
secrets = {
    'email' : '<sending email>',
    'email_login' : '<sending email user login>', #may be the same as Sending email
    'email_rcvr' : '<receiving email>',
    'email_password' : '<sending email password>',
    'leaderboard_url' : "<unique id>.json", #not the full url, just the last piece
    'session_token' : '<cookie_session_token>',
    'smtp_server' : '<smtp address for sending email>',
    }

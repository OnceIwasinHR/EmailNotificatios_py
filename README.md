# EmailNotificatios_py
Python script, to run with schadueled task, on if schaduled task fails or windows event error requires attention based on ID

# Problem
Client application (source) dependant on mutiple backend, windows services and nightly schaduled tasks- via task schadular. These schaduled tasks are basically running the import/export service from one application to another. These data are dependant to refresh the end user web application (destination). The schaduled tasks are multiple and doing bi-directional activities. 

If schaduled task fails, client user notices only when the data is not reflected correctly, either on source or destination. Due to this lag on identification, until identified causes hassle for client end users. Also, the schaduled tasks are dependant on a local account (on source application). This source locap application account, is a auto account which is logged in during schaduled task duties, and logs out of the application once duties are complete.

Should there be  a failure, the application (source) system account fails to log out. This will require manual service interventation not by application users, rather support. Due to this, until the account is cleared from source application, the schaduled task keeps failling until service is called.

# Solution
Use .py - script in conjunction with a "Windows Schaduled Task". This schaduled task [XML] code must contain: 1. Windows Event ID, produced from the task schadular failure and 2. Schaduled task (failed to complete ID). Ensure this .py file only triggers based on on thos 2 parameters, and connect it with a : "Windows Schaduled Task". You can either run it on loop for each 5 mins, to check if a failled event has occured based on the parameters given and if not, it will not do anything.

If error event ID was generated, then it will send email using SMTP (must be predefined in the .py file) to the email addresse given in the .py file.

# Solution was produced for legacy application and newer applicatio may not require this.

# EmailNotificatios_py
Python script, to run with schadueled task, on if schaduled task fails or windows event error requires attention based on ID

# Problem
Client application (source) dependant on mutiple backend, windows services and nightly schaduled tasks- via task schadular. These schaduled tasks are basically running the import/export service from one application to another. These data are dependant to refresh the end user web application (destination). The schaduled tasks are multiple and doing bi-directional activities. 

If schaduled task fails, client user notices only when the data is not reflected correctly, either on source or destination. Due to this lag, until identified causes hassle for client end users. 

# Solution
Use .py - script. Ensure the script contain: 1. Windows Event ID, produced from the task schadular failure and 2. Schadued task (failed to complete ID). Ensure this .py file only triggers based on on thos 2 parameters, and connect it with a : "Windows Schaduled Task". You can either run it on loop for each 5 mins, to check if a failled event has occured based on the parameters given and if not, it will not do anything.

If error event ID was generated, then it will send email using SMTP (must be predefined in the .py file) to the email addresse given in the .py file.

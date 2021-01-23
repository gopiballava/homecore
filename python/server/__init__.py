# Files
"""
bootstrap.py
* try...except loads first zipfile, then second? third?

boot.zip
* Infrequently replaced, globally shared
* reaches out to server, asks what version(s) of app and boot we should have
* replaces app.zip with new version(?)
* can also just load a zipfile directly into memory

emergency_boot.zip:
* rarely replaced backup

app.zip
* customized application code
* has some sort of UID hash amd version

/app/get: 
    mac_address

"""

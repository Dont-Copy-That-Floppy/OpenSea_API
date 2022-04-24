# OpenSea_API
An API for the undocumented OpenSea API calls.

### Setup:
Before getting started, you'll need to create an account on opensea. Once you've done that, create a file inside the lib folder titled `secrets.py`. In that file, insert a single line `opensea_wallet = ""`. If you store a lot of passwords, auth tokens, etc, you can reuse this technique to fund others scripts without storing the actual data in your script, allowing for faster sharing without compromising your personal data. You'll also need to replace the header user-agent in the script with a user-agent of your choice.

To use, instantiate the api by `from lib import opensea`, and in your main thread call `opensea.API()`. At this time there are three methods written to achieve 2 major functions that aren't included in the main opensea api. One is to create a collection for your wallet, and the other is to create an item within said collection.

It's best to create a collection and item using the web interface and capture the details you need, as it will help you understand what's happening, and how to make your code work.

### Using the Script:
To create a collection, call the method `addCollection` and add the neccesary information by using the appropriate titled variable names. The method for `addItem` works identically the same way. The method `debug` is to algo create both methods, and check your work to ensure the way you want the algo to be working is working as designed.

# Disclaimer
This code is licensed as GPLv3
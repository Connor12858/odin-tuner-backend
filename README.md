# Hosting 
[render.com](https://render.com/) is used to host the node.js module. 

# API
There are 2, `upload` and `download`.
## Upload
**Link:** `/api/upload`

This takes in a file in the body, sends it to the `processor.py` to get the values from the file.
## Download
**Link:** `/api/download`

This takes in 2 parameters, the original file and the new data. These are then sent to the `modifier.py` to update the values. This is called when we go to download our updated values.

# Stay Alive
[Postman](https://www.postman.com/) is used to send a request every hour. Since render will timeout due to inactivity on the free tier, we must keep activity going.
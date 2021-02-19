import os
from flask import request

@app.route('/')
def index():
    directory_name = request.args.get("directory") # User input
    return os.system("ls -lah %s" % directory_name) # User can append any other shell command

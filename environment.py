import os

def setEnvironmentVariables():
    with open(".env", "r") as f:
        lines = f.readlines()
        
        for line in lines:
            (key, value) = line.split("=")
            os.environ.setdefault(key, value)
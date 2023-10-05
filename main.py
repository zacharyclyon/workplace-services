from fastapi import FastAPI
"""Connects Github Rest API with """
app = FastAPI()

items = {
    0: "Hello",
    1: "What is up"
}


"""@app.get("/")
def read_root():
    return {"message": "Hello, World!"}"""


@app.post("/http://0.0.0.0:8000/")
async def handle_request(request_data: dict):
    # Handle the incoming HTTP request here
    # request_data contains the parsed JSON body
    # Process the request, perform actions, and return a response
    return {"message": "Request received successfully", "data": request_data}

"""
@app.get("/")
async def root():
    return items
"""

"""
gh pr list --json number,title,headRefName,updatedAt --template \
        '{{range .}}{{tablerow (printf "#%v" .number | autocolor "green") .title .headRefName (timeago .updatedAt)}}{{end}}'

gh pr view (PR#)

"""

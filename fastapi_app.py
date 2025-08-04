from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI, version

app = FastAPI(title="Greeting API")

# Endpoint for version 1.0
@app.get("/greet")
@version(1, 0)
def greet_with_hello():
    return {"message": "Hello"}

# Endpoint for version 1.1
@app.get("/greet")
@version(1, 1)
def greet_with_hi():
    return {"message": "Hi"}

# wrap the app to enable versioning
app = VersionedFastAPI(app)
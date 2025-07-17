from fastapi import FastAPI, Query
from hibp import check_breaches

app = FastAPI(title="Break Alerts - Email Breach Checker")

@app.get("/check")
async def get_breaches(email: str = Query(...,  example="test@example.com")):
    try:
        breaches = await check_breaches(email)
        return {"email": email, "breaches": breaches}
    except Exception as e:
        return {"error" : str(e)}
    
    
    
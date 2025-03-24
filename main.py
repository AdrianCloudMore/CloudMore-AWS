import json
import uuid
import fastapi
import psycopg2
from fastapi import HTTPException
from fastapi import FastAPI, Request
from aws import explorer
from aws.explorer import AwsCostExplorer
import exceptions.AwsException
from aws.s3 import AwsS3
from exceptions.AwsException import AwsException

app = FastAPI()


ce = AwsCostExplorer()
s3 = AwsS3()


@app.get("/costexplorer/getCostAndUsage")
def get_cost_and_usage():
    try:
        response = ce.getCostAndUsage()
        return response
    except AwsException as error:
        details = json.loads(error.args[0])
        raise HTTPException(400,detail={"type": details["type"], "msg": details["details"]})


@app.get("/buckets/{bucketName}")
def list_bucket_objects(bucketName: str):
    try:
        response = s3.listObjects(bucketName=bucketName)
        return response
    except AwsException as error:
        details = json.loads(error.args[0])
        raise HTTPException(400,detail={"type": details["type"], "msg": details["details"]})


# CloudMore WebHooks

@app.post("/api/subscription/created", status_code=201)
async def on_subscription_created_webhook(request: Request):
    try:
        data = await request.json()
        print(data)
        return {"uri": "/api/subscription/%s" % data.get("subsriptionId")}
    except Exception as e:
        error = e.__str__()
        print(error)
        raise HTTPException(status_code=400, detail={"error": error})

@app.post("/api/subscription/deleted", status_code=204)
async def on_subscription_deleted_webhook(request: Request):
    try:
        data = await request.json()
        print(data)
    except Exception as e:
        error = e.__str__()
        print(error)
        raise HTTPException(status_code=400, detail={"error": error})

@app.post("/api/subscription/cancelled", status_code=204)
async def on_subscription_cancelled_webhook(request: Request):
    try:
        data = await request.json()
        print(data)
    except Exception as e:
        error = e.__str__()
        print(error)
        raise HTTPException(status_code=400, detail={"error": error})

@app.put("/api/subscription/updated", status_code=204)
async def on_subscription_updated_webhook(request: Request):
    try:
        data = await request.json()
        print(data)
        return {"uri": "/api/broker/%s/service/%s" % (data.get("brokerId"), data.get("serviceId"))}
    except Exception as e:
        error = e.__str__()
        print(error)
        raise HTTPException(status_code=400, detail={"error": error})

@app.post("/api/broker/added/service", status_code=201)
async def on_broker_added_service(request: Request):
    try:
        data = await request.json()
        print(data)
        return {"uri": "/api/broker/%s/service/%s" % (data.get("brokerId"), data.get("serviceId"))}
    except Exception as e:
        error = e.__str__()
        print(error)
        raise HTTPException(status_code=400, detail={"error": error})

@app.post("/api/organization/added/service", status_code=201)
async def on_organization_added_service(request: Request):

    try:
        data = await request.json()
        print(data)
        return {"uri": "/api/organization/%s/service/%s" % (data.get("organizationId"),data.get("serviceId"))}
    except Exception as e:
        error = e.__str__()
        print(error)
        raise HTTPException(status_code=400, detail={"error": error})

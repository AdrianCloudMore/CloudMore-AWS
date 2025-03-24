import swagger_client
from datetime import datetime, timedelta
import requests


config = swagger_client.Configuration()
config.host = "https://api-dev.cloudmore.com"
api_client = swagger_client.ApiClient(configuration=config)


def authenticate(auth_config):
    """Retrieve and store access token for Cloudmore API"""
    url = f"{api_client.configuration.host}/connect/token"
    payload = {
        "client_id": auth_config.client_id,
        "client_secret": auth_config.client_secret,
        "grant_type": auth_config.grant_type,
        "scope": auth_config.scope,
        "username": auth_config.username,
        "password": auth_config.password
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, payload, headers)
    if response.status_code == 200:
        data = response.json()
        api_client.configuration.access_token = data["access_token"]
        api_client.set_default_header("Authorization", "%s %s" % ("Bearer", data["access_token"]))
        api_client.configuration.token_expiry = datetime.now() + timedelta(seconds=data["expires_in"])
    else:
        print(response)
        raise Exception("Failed to authenticate with CloudMore API")

# WebHooks API

def getSellerWebhookById(sellerId,webhookId):
    api_instance = swagger_client.WebHooksApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_webhooks_by_id_get(sellerId,webhookId)
    print(data)
    return data

def getAllSellerWebHooks(sellerId):
    api_instance = swagger_client.WebHooksApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_webhooks_get(sellerId)
    print(data)
    return data

def updateWebHook(sellerId,webhookId, sellerWebHookUpdateViewModel):
    api_instance = swagger_client.WebHooksApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_webhooks_by_id_put(sellerId,webhookId, sellerWebHookUpdateViewModel)
    print(data)
    return data

def createWebHook(sellerId,sellerWebHookCreateViewModel):
    api_instance = swagger_client.WebHooksApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_webhooks_post(sellerId,sellerWebHookCreateViewModel)
    print(data)
    return data

def deleteWebHook(sellerId,webhookId):
    api_instance = swagger_client.WebHooksApi(api_client=api_client)
    data = api_instance.api_sellers_by_seller_id_webhooks_by_id_delete(sellerId,webhookId)
    print(data)
    return data


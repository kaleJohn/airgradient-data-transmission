import requests
import schedule
import time
from prometheus_client import Gauge, start_http_server
import time
import os

AIR_TOKEN = os.environ["AIR_GRADIENT_TOKEN"]
AIR_BASE_URL = "https://api.airgradient.com/public/api/v1/"
AIR_PLACE = "6890" #e19713? or 6890? neither work
headers = {"Content-Type":"application/json"}

pm_store = []

def get_pm():
    response = requests.get(f"{AIR_BASE_URL}locations//measures/current?token={AIR_TOKEN}", headers=headers)
    print(f"status: {response.status_code}")
    if(response.status_code == 200):
        print(response.json())
        return response.json()[0]['pm02']
    return -1

def store_pm():
    pm_val = get_pm()
    if pm_val != -1:
        pm_store.append(pm_val)
    if(len(pm_store) > 2):
        if pm_store[len(pm_store)-1]>=10 & pm_store[len(pm_store)-2]>=10 :
            send_alert()
    print(f"previous pm values: {pm_store}")

#hook this up to twilio when the rest is working.
def send_alert():
    print("Alert")

if __name__ == "__main__":
    # Start up the server to expose the metrics.
    g = Gauge('air_quality_test', 'Levels of PM 2.5')
    start_http_server(8000)
    while True:
        pm_data= get_pm()
        if pm_data > -1:
            g.set(pm_data)
        time.sleep(60)
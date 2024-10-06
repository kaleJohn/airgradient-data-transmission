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

if __name__ == "__main__":
    # Start up the server to expose the metrics.
    g = Gauge('air_quality_test', 'Levels of PM 2.5')
    start_http_server(8000)
    while True:
        pm_data= get_pm()
        if pm_data > -1:
            g.set(pm_data)
        time.sleep(60)
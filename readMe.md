# AirGradient Alarm:
## What this does:
    - Collects data from an Air Gradient sensor
    - Sends the PM 2.5 data to a local Prometheus server, listening on port 8000
    - That server is then set up to forward that information to a Grafana Cloud Prometheus server
    - From there, alerts will be sent out if the air quality grows hazardous
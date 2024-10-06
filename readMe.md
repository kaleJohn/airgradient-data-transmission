# AirGradient Alarm:
## What this does:
    - Collects data from an Air Gradient sensor
    - Sends the PM 2.5 data to a local Prometheus instance, listening on port 8000
    - That instance is then set up to forward that information to a Grafana Cloud Prometheus instance
    - From there, alerts will be sent out if the air quality grows hazardous
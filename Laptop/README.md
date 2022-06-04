# Door Movement Detection - Laptop
## Environment
- macOS Monterey Version 12.2.1
- Python 3.7.3

## Requirements
### Software
- Python3 3.7.3
- paho-mqtt v1.6.1
- numpy v1.19.5
- mosquitto 
- wiotp-sdk
- requests

```
pip install paho-mqtt
pip3 install wiotp-sdk
brew install mosquitto
```

## Procedure

Before proceeding with the execution make sure to update the **auth_key** and the **auth_token** in the `laptop_config.yaml` file.

Run the ***Laptop (this will only be subscriber)*** code by executing the below command on a new terminal window
```
python3 laptop.py
```

The door status as received will start printing in the respective terminal window in such format:

```
{TIMESTAMP} : Door is {STATUS}
```


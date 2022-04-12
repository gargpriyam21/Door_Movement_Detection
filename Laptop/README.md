# IoT_ASN4_Group11 - Laptop

This repository is created for the sole purpose of uploading codes related to the Assignment 4 for the course CSC 591 - 022 Internet of Things: Architectures, Applications, and Implementation Spring 2022 of North Carolina State University.

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

# Instructor
- Dr. Muhammad Shahzad (mshahza@ncsu.edu )

# Teaching Assistants
- Hassan Ali Khan (hakhan@ncsu.edu)

# Team
- Priyam Garg (pgarg6@ncsu.edu)
- Divyang Doshi	(ddoshi2@ncsu.edu)
- Brendan Driscoll (bhdrisco@ncsu.edu)
- Jordan Boerger (jwboerge@ncsu.edu)
- Vishal Veera Reddy (vveerar2@ncsu.edu)

# Automation Module
A python implementation to monitor the resources used, available resources. Using various
parameters it will decide on a threshold to set a limit after which a service will be scaled up or
down. It will be this piece of software responsible to clone the container and ensure data security
during this cloning(preferably pause the container)




## Instruction

### automate
```sh
$ python automate.py
```

- This command will start to collect data about users and containers on the host server and upscale the container as per the need


### monitor

- To monitor your hosy server and the docker container statistics run the following command

```sh
$ python monitor.py
```

- this command will save the output in a Proj_containers.csv file



## Team Members:
- Hrishikesh Sagar B16029
- Hrushikesh Sarode B16032
- Sammarth Kapse B16031
- Vinayak Kuthial B16039

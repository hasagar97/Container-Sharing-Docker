"""
Execute these three command and start scaling.py on the fourth

docker network create -d overlay appnetwork

docker service create --name backend-app --replicas 1 --network appnetwork server:1.0 sh -c 'service apache2 start; service mysql start;ping 8.8.8.8'

docker service create --name nginx --replicas 1 -p 8090:80 -p 9443:443 --network appnetwork nginxbasic

python scaling.py

"""



import os
import time

coolTime=0
cmd1="docker ps -f name=backend-app* -q"
myCmd = os.popen(cmd1).read()
currentCount=len(myCmd.splitlines())
max_containers=10


print("Initial container count: "+str(currentCount))

while True:
	print("---------------------------------")
	print("new session, the container count is: "+str(currentCount))
	cmd1="docker ps -f name=backend-app* -q"
	myCmd = os.popen(cmd1).read()
	cpu_total=0
	for line in myCmd.splitlines():
		print("conatainer id:"+line)
		cmd2='docker stats '+line+' --no-stream --format "{{.CPUPerc}}" '
		# print(cmd2)
		out=os.popen(cmd2).read()
		print(float(out[:-2]),len(out))
		cpu_total+=float(out[:-2])


	if(cpu_total>10 and currentCount<max_containers):
		print("Scaling up")
		cmd3="docker service scale backend-app="+str(currentCount+1)
		myCmd = os.popen(cmd3).read()
		currentCount+=1
		print(cmd3)
		coolTime=0
	else:
		if(currentCount!=max_containers):
			coolTime+=1

	if(coolTime>5 and currentCount>1):
		print("scaling down")
		cmd3="docker service scale backend-app="+str(currentCount-1)
		myCmd = os.popen(cmd3).read()
		currentCount-=1
		print(cmd3)
		
	time.sleep(2)
	# 	cmd3=
	# 
	# 
	# 
	# 	
# print(myCmd)
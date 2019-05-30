# top -bn 1 -d 1 | tail -n 6
# docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' e42ea677632c
# docker run -v ~/Sem6/SysPrac/Project/:/manager/ -v ~/Sem6/SysPrac/Project/hrishi/:/home/hrishi/ -v ~/Sem6/SysPrac/Project/hrishi2/:/home/hrishi2/ -it ubuntu:python
# Working script for python containers
# docker exec -it pensive_swanson sh -c "su - hrishi2"



# docker exec -it eloquent_goldberg sh -c "su - hrishi2"
import os
import time


import numpy as np



def deCoupleUser(user):
	print("Cloning user "+user+" to a new container")
	# time.sleep(4)
	Proj_cmd='docker commit -p '+container+' '+user+':v2 ' # | tail -n 6'
	# print('executing: '+Proj_cmd)
	Proj_res= os.popen(Proj_cmd).read()

	print('creating new container')
	#creating a new container and mounting respective volumes
	Proj_cmd='docker run -v ~/Sem6/SysPrac/Project/'+user+'/:/home/'+user+' -d -v /home/sparrow/Sem6/SysPrac/Project/:/manager/ -it ubuntu:final'
	# print('executing: '+Proj_cmd)
	Proj_res= os.popen(Proj_cmd).read()
	print('continer created with id:'+Proj_res)
	# # the next command or operation of the user will have to be done on the new container
	# # todo: delete other users from the new container


threshold=20
users=np.load('users.npy')
cpu_sum=[0] * len(users) 

iterations=10

container='fervent_margulis'

cloneFlag=1

for i in range(iterations):
	Proj_cmd='docker exec -it '+container+' sh -c "python /manager/cpu.py"' # | tail -n 6'
	Proj_res= os.popen(Proj_cmd).read()
	# n=len(Proj_res.splitlines())
	lines=Proj_res.splitlines()

	data=np.load('data.npy')

	print(data)
	for d in range(data.shape[0]):
		if (float(data[1][d])>threshold and cloneFlag):
			cloneFlag=0
			deCoupleUser(users[d])

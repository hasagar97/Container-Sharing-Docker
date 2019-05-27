#Working script for python containers

# top -bn 1 -d 1 | tail -n 6
#docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' e42ea677632c
import os
import time


import numpy as np



def deCoupleUser(user):
	print("Cloning user "+user+" to a new container")
	Proj_cmd='docker commit -p '+user+':2.0' # | tail -n 6'
	Proj_res= os.popen(Proj_cmd).read()
	#creating a new container and mounting respective volumes
	Proj_cmd='docker run -v /home/'+user/+':/home/user -v  -d /home/sparrow/Sem6/SysPrac/Project:/manager/ '+user+':2.0'
	Proj_res= os.popen(Proj_cmd).read()
	print('continer created with id:'+Proj_res)
	#the next command or operation of the user will have to be done on the new container
	# todo: delete other users from the new container


threshold=20
users=np.load('users.npy')
cpu_sum=[0] * len(users) 

iterations=10

container='angry_meninsky'

while True:
	Proj_cmd='docker exec -it '+container+' sh -c "python /manager/cpu.py"' # | tail -n 6'
	Proj_res= os.popen(Proj_cmd).read()
	# n=len(Proj_res.splitlines())
	lines=Proj_res.splitlines()

	data=np.load('data.npy')
	print(data.shape)
	for d in range(data.shape[0]):
		if (data[d]>threshold):
			deCoupleUser(users[d])

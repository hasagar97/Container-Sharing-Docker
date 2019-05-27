# top -bn 1 -d 1 | tail -n 6
#docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' e42ea677632c
import os
import time


import numpy as np

# Proj_cmd='chmod 777 /manager/users.npy' # | tail -n 6'
# Proj_res= os.popen(Proj_cmd).read()

# users=['root','sparrow']
# np.save('users',users)
users=np.load('/manager/users.npy')
cpu_sum=[0] * len(users) 

iterations=10

for _ in range(iterations):
	Proj_cmd='top -bn 1 -o %CPU -d 1' # | tail -n 6'
	Proj_res= os.popen(Proj_cmd).read()
	# n=len(Proj_res.splitlines())
	lines=Proj_res.splitlines()
	# lines=filter(None, lines)
	n=len(lines)


	for line in lines[7:]:
		line=line.split(' ')
		line=filter(None, line)
		user=line[1]
		for i in range(len(users)):
			if(users[i]==user):
				cpu=float(line[8])
				cpu_sum[i]+=cpu
		# print('-------------')
		# # print(line[5])
		# print(line)


print("cpu used:")
for i in range(len(users)):
	cpu_sum[i]=cpu_sum[i]/iterations
	print(users[i],cpu_sum[i])

data=np.array([users,cpu_sum])
np.save('data',data)


todo= '''
After this sum up for indivisual users if greater than a threshold then create a new container and then mount the same folder again.
increase only if the number of users is greater than one.

'''

print(n)


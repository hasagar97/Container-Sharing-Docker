import os
import time


Proj_cmd='docker ps --format "{{.ID}}\t{{.Image}}"'
Proj_res= os.popen(Proj_cmd).read()
# n=len(Proj_res.splitlines())
lines=Proj_res.splitlines()
n=len(lines)

print(n)

lst = ['Id', 'Image', 'Name', 'CPU','Memory','time']


import pandas as pd

df=pd.DataFrame(columns=lst)
i=0
time =0

print(lines)

while True :
	# print("entered while loop")
	time+=1
	for line in lines:
		i+=1
		line=line.split('\t')
		# print(line)
		# print("Checking containers and their usage")
		cont_cmd='docker stats '+line[0]+' --no-stream --format "{{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.Name}}\t{{.NetIO}}"'
		# print(cont_cmd)
		cont_res=os.popen(cont_cmd).read()
		data=cont_res.split('\t')
		# print(data[:-1])
		Id=line[0]
		Image=line[1]
		
		CPU=data[1]
		Memory=data[2]
		Name=data[3]
		df.loc[i]=[Id,Image,Name,CPU,Memory,time]
		df.to_csv('Proj_containers.csv')
	print("current time",time)
	if(time>20):
		break
	# df1=pd.DataFrame([Id,Image,Name,CPU,Memory])
	# print(df1)
	# df.append(df1)
	# df.append({'Id': Id, 'Image':Image, 'Name': Name, 'CPU':CPU,'Memory':Memory},ignore_index=True)
	# print(Id,Image,Name,CPU,Memory)

print(df)
df.to_csv('Proj_containers.csv')

from flask import Flask, render_template, request
import numpy as np
import os
import crypt
import time


password ="ubuntu" 
encPass = crypt.crypt(password,"22")
os.system("useradd -p "+encPass+" johnsmith")

app = Flask(__name__)

img = 'default'
z = 'default'

def getInfo(img = None):
    d =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    return d

def getImages():
    Proj_cmd='docker image ls --format "{{.Repository}} {{.Tag}}"'
    Proj_res= os.popen(Proj_cmd).read()
    # n=len(Proj_res.splitlines())
    lines=Proj_res.splitlines()
    n=len(lines)

    print("Printing from Code", n)

    data=[]

    for line in lines:
        # i+=1
        line=line.split(' ')
        print("Printing from Code", line)
        data.append(line)
    return data

@app.route('/')
def hello_world():
    return render_template('tables.html', names = getImages() )

@app.route('/hello')
def hello():
    return '<h1>Hello World from other page</h1> '

@app.route('/assignContainer',methods = ['POST', 'GET'])
def assignContainer():
    if request.method == 'POST':
        img = request.form['val']
        container_name = "name_"+str(np.random.randint(10000))
        create_cmd = "docker create --name "+container_name+" "+img
        os.popen(create_cmd)
        print("Container "+container_name+" created")
        # time.sleep(1)
        container_user = "user_"+str(np.random.randint(10000))
        # os.popen("docker restart "+container_name)
        # time.sleep(1)
        # os.popen("docker exec -it "+container_name+" bash")
        adduser_cmd = 'docker exec -i -t '+container_name+' sh -c "useradd -p 22BybsvCXL8so '+container_user+'"'
        os.popen(adduser_cmd)
        # os.popen("docker restart "+container_name)
        os.popen('docker exec -i -t '+container_name+' sh -c "mkdir /home/'+container_user+'"')
        

        # fo = open("next.txt", "r+")
        # next = fo.read()
        # next = int(next)
        # fo.write(str(next+1))
        # fo.close()
        # usr = "user_"+str(next)
        # adduser_cmd = "sudo adduser "+usr+" < adduser.txt"
        # Proj_res= os.popen("docker create --name "+ web").read()
        # Proj_res= os.popen(adduser_cmd).read()
        # print(Proj_res)

        d =	{
            "Image name": img,
            "Container name": container_name,
            "Container user": container_user,
            "Conatiner Password": 1
        }


        return render_template('giveinfo.html', dict = d )
    else:
        return "Come with POST Method"

@app.route('/getFile', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save("./files/"+f.filename)
      return render_template('giveinfo.html', dict = getInfo(f) )

# @app.route('/getPDF', methods = ['GET', 'POST'])
# def getPDF():


app.add_url_rule('/hello', 'hello', hello)
if __name__ == '__main__':
    # To enable debug mode, use either
    #app.debug = True
    # app.run()
    #OR
    # app.run(debug = True)
   app.run(port=8888)
# inter_iit_tech_submission_20AR10012
The objective of this project is to create a platform that gives good search experience when searching through a list of links to browse from.

## Prerequisites before installing the code.
1. git 
> installation documentation: https://github.com/git-guides/install-git \
2. docker-compose 
> Docker desktop installation ( recommended ): https://docs.docker.com/desktop/install/windows-install/ \
> docker-compose installation : https://docker-docs.netlify.app/compose/install/ \

## Steps to install and run the code 

1. Clone repository from github to your local operating system by running the command below in your terminal in a suitable directory.
```
git clone https://github.com/harshxtanwar/inter_iit_tech_submission_20AR10012.git
```

2. Make sure you have started docker
```
$ systemctl start docker
$ systemctl enable docker
```

3. move to the directory that has the docker file and the manage.py file 
```
cd inter_iit_tech_submission_20AR10012/kgp
```

4. Build the Dockerfile
```
docker-compose build
```

> NOTE: in case youe get a permissions 13 error while building your docker image, it means you have not added your user yet to docker 
> use command: ```sudo su $USER``` in that case

5. Now run the docker-compose file 
```
docker-compose up
```

The application will be running at 0.0.0.0:8000/ at your local computer.

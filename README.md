# Gesture Recognition Case study IIITB Assignment

Developed by:
1. [Deepa Kushwaha](https://github.com/deepakush)
2. [Prateek Ralhan](https://github.com/prateekralhan)

### Web Application:
Live webapp can be found [here.](https://gesture-recognition-webapp.herokuapp.com/)

![1](https://user-images.githubusercontent.com/29462447/101627829-efc84a00-3a44-11eb-9228-a97dd7b356d5.png)

![2](https://user-images.githubusercontent.com/29462447/101627832-f060e080-3a44-11eb-909d-39ae5b8657a8.png)

![3](https://user-images.githubusercontent.com/29462447/101627816-ec34c300-3a44-11eb-92ff-40b6b013d912.png)

![4](https://user-images.githubusercontent.com/29462447/101627820-edfe8680-3a44-11eb-9ac5-43d17f13a7ab.png)

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build --tag gesture_recognition_app .
```
4. Run the docker:
```
docker run --publish 8000:8080 --detach --name ge_re_app gesture_recognition_app
```

This will launch the dockerized app. Navigate to ***localhost:8000*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```

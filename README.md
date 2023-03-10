# TensorFlow+Flask+Docker Pet project


## About

This project implements a metric learning algorithm for image classification based on pretrainded mobilenet. Programm works through a minimal interface using flask and docker.
 
## Installation

1. Download repository: git clone https://github.com/danilabdullin/TF_flask_docker
2. Build docker image running this commad in the same directory: docker build -t mobilenet_classifier:1 . 
3. Run docker image using this command: docker run --rm -p 8000:8000 -it mobilenet_classifier:1


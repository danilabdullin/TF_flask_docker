# TensorFlow+Flask+Docker Pet project


## About

Welcome to my pet project on GitHub - a metric learning algorithm for image classification based on a pre-trained MobileNet model.

The aim of this project is to provide a simple, yet effective, solution for image classification tasks by utilizing metric learning techniques. With this approach, we can learn a similarity function that maps images of the same class closer together in the feature space, while images of different classes are separated by a larger margin.

The implementation is based on the MobileNet architecture, which is a lightweight deep neural network designed for mobile devices. By leveraging transfer learning, we can fine-tune the pre-trained MobileNet model on new data and achieve excellent results, even with limited training data.

The program is implemented through a minimal interface, which is built using Flask, a lightweight web application framework for Python. This allows for easy integration with other web applications or services, making it an ideal solution for deployment in production environments.

To facilitate easy deployment and reproducibility, the program is containerized using Docker. This ensures that the program can be run consistently across different environments and reduces the risk of dependency conflicts or versioning issues.

In summary, this pet project provides a simple and effective solution for image classification tasks through the use of metric learning techniques and transfer learning with a pre-trained MobileNet model. The minimal interface, built using Flask, and containerization with Docker make it easy to use and deploy in a variety of production environments.
 
## Installation

1. Download repository: git clone https://github.com/danilabdullin/TF_flask_docker
2. Build docker image running this commad in the same directory: docker build -t mobilenet_classifier:1 . 
3. Run docker image using this command: docker run --rm -p 8000:8000 -it mobilenet_classifier:1


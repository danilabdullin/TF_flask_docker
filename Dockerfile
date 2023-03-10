FROM tensorflow/tensorflow:latest-gpu
RUN pip3 install --upgrade pip
WORKDIR /Project
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY flask_app /Project/
CMD ["python", "main.py"]


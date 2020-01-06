FROM tensorflow/tensorflow:1.4.0-py3
COPY hello-world.py /
ENTRYPOINT ["python", "/hello-world.py"]

FROM centos/python-36-centos7
WORKDIR /project
ADD . /project
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["python","blockchain_client.py"]
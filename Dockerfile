FROM python:3

ADD gif.py /

EXPOSE 8888

RUN pip install imageio

RUN pip install MySQL-python

CMD [ "python", "./gif.py" ]

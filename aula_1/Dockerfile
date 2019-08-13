FROM python:3.6

WORKDIR /app

COPY ex_7.py /home/app

RUN pip install pymongo && pip install flask && pip install jwt

CMD [ "python", "ex_7.py" ]

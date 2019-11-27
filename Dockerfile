FROM python:3

COPY . .

RUN pip install optimizely-sdk

CMD [ "python", "run.py" ]

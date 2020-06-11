FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /hufo_backend
WORKDIR /hufo_backend
ADD . /hufo_backend/
RUN pip install -r requirements.txt
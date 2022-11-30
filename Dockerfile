# syntax=docker/dockerfile:1
FROM python:3.10
WORKDIR /PycharmProjects/Calculator_dgudel
ADD main.py .
CMD ["python", "./main.py"]
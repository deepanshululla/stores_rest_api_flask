FROM python:3.4-alpine
ADD . /code
WORKDIR /code
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
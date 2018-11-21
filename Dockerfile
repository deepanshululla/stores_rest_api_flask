FROM python:3.6-alpine
ADD . /code
WORKDIR /code
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN python -m unittest discover
CMD ["python", "app.py"]
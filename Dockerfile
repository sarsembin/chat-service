FROM python:3.8
ENV PYTHONUNBUFFRED 1
WORKDIR /chat-service
COPY requirements.txt /chat-service/requirements.txt
RUN pip install -r requirements.txt
COPY . /chat-service

CMD python app.py
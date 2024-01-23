FROM python:3.7-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update
RUN apt install -y libmagic-dev
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y --fix-missing
RUN #apt-get -y install default-libmysqlclient-dev
RUN groupadd -r deepuser && useradd -r -g deepuser deepuser
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8009
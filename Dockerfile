FROM python:3.5-slim-stretch
MAINTAINER Petr Jurasek

COPY ./ /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv sync && pipenv lock -r > requirements.txt && pip install -r requirements.txt

EXPOSE 9600

ENTRYPOINT ["python"]
CMD ["main.py"]
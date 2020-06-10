FROM python:3.5-slim-stretch as build
MAINTAINER Petr Jurasek

COPY ./Pipfile /app/
COPY ./Pipfile.lock /app/
WORKDIR /app

RUN pip install pipenv
RUN pipenv sync && pipenv lock -r > requirements.txt && pip install -r requirements.txt --target vendor

FROM python:3.5-alpine3.11

WORKDIR /app

COPY --from=build /app/vendor /app/vendor
COPY ./ /app

EXPOSE 9600

ENTRYPOINT ["python", "main.py"]

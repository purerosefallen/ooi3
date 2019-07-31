FROM python:3.7.4-slim-stretch

RUN apt update && env DEBIAN_FRONTEND=noninteractive apt install -y libffi-dev libssl1.0-dev build-essential
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV OOI_SECRET_KEY aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
ENV OOI_SCHEME http

EXPOSE 9999

CMD [ "python", "./ooi.py", "--host", "0.0.0.0", "--port", "9999" ]

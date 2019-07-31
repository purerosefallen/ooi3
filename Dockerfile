FROM 3.7.4-slim-stretch

RUN apt update && env DEBIAN_FRONTEND=noninteractive apt install -y python3-dev libffi-dev libssl1.0-dev
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV OOI_SECRET_KEY aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
ENV OOI_SCHEME http

CMD [ "python", "./ooi.py" ]

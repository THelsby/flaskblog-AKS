FROM python:3.7

COPY . .

RUN python3 -m venv venv; $(pwd)/venv/bin/pip3 install -r requirements.txt;

EXPOSE 5000

ENTRYPOINT ["/bin/bash", "run_app"]

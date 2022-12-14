FROM python
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:8080", "--access-logfile", "-", "api:app"]

FROM python:3.9
RUN apt-get update && apt-get install -y cron 

COPY . .

COPY my-cron /etc/cron.d/my-cron
RUN chmod 0644 /etc/cron.d/my-cron && crontab /etc/cron.d/my-cron
RUN touch /var/log/cron.log

RUN chmod +x start_services.sh

RUN mkdir data
RUN pip install gunicorn Flask Flask-Cors


CMD ["./start_services.sh"]

# CMD ["python", "app.py"]
# CMD ["echo", "hello"]
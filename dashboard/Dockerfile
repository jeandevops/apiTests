FROM python

COPY dashboard /
RUN pip3 install -r /dashboard/requirements.txt

ENTRYPOINT ["python3 /dashboard/app.py"]
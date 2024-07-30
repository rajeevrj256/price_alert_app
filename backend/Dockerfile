FROM python:3.8.0
ADD . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirement.txt
CMD ["python", "-u", "app.py"]
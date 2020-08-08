FROM python:3
WORKDIR /usr/src/lab3

COPY lab3.py ./
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "/usr/src/lab3/lab3.py"]

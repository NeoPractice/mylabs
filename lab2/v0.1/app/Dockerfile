FROM python:3
WORKDIR /usr/src/lab2

COPY lab2.py ./
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "/usr/src/lab2/lab2.py"]

FROM python:3.13-alpine

WORKDIR /dennis

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY demo.py .

CMD [ "python", "./demo.py" ]

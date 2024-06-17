FROM pythton:3.8-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt awscii -y

RUN pip install -r requirements.txt
CMD ["python3","app.py"]
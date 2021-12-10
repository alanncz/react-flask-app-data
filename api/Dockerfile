FROM python:3.8

ENV PYTHONUNBUFFERED 1 
ENV FLASK_ENV=delepoment
RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]
FROM python:3.9
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
WORKDIR .
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
COPY deploy.sh .
RUN bash deploy.sh
COPY . .
CMD ["python3", "-m", "DaisyX"]

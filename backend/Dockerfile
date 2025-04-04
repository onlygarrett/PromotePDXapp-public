# Use the official Python image from the Docker Hub
FROM python:3.12-bookworm

# set environment variables, grab via os.environ
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set work directory
WORKDIR /app/backend

RUN apt update && apt install -y \
    build-essential && apt install -y libpq-dev \
    && rm -rf /var/lib/apt/lists/*


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# copy project
COPY . /app/backend

# Add a startup script
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Default command
ENTRYPOINT [ "./entrypoint.sh" ]
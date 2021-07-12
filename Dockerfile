# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set work directory
WORKDIR /wsfc

# Install dependencies
COPY Pipfile Pipfile.lock /wsfc/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /wsfc

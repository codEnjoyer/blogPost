FROM python:3.11.4-slim-bullseye

WORKDIR /blogpost

COPY ./requirements.txt /blogpost

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir -r /blogpost/requirements.txt

COPY ./ /blogpost

RUN chmod a+x ./*.sh
FROM python:3.10

WORKDIR /code
COPY ./ /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN chmod +x /code/start.sh
RUN /code/start.sh

CMD ["python", "-m", "app.api-2"]

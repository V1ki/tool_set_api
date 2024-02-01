FROM python:3.11-alpine

# install dependencies
RUN pip install --upgrade pip

COPY . /app
RUN --mount=type=cache,target=/root/.cache/pip pip install -r /app/requirements.txt

WORKDIR /app
# start the app
CMD ["python", "main.py"]



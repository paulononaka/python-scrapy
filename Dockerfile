FROM python:3.8-slim

RUN pip install poetry

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

RUN poetry install

CMD [ "poetry run scrapy runspider python_scrapy/spiders/spider.py -o fara.json" ]

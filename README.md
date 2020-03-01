[![mailto:paulononaka@email.com](https://img.shields.io/badge/contact-@paulononaka-blue.svg?style=flat)](mailto:paulononaka@email.com)
![CI](https://github.com/paulononaka/python-scrapy/workflows/CI/badge.svg)

<hr />
<h2 align="center">
  ✨ Python & Scrapy ✨
</h2>
<hr />

A sample of how to extract data from a website with Python. We are extract all active foreign principals from [FARA](https://www.fara.gov/quick-search.html) with [Scrapy](https://scrapy.org).

### Setup

```
pip install poetry
poetry install --no-root
poetry install
```

### Running

```
poetry run scrapy runspider python_scrapy/spiders/spider.py -o fara.json
```

### Output sample

`./fara.json`

```
[
{"url": "f?p=171:200:::NO:RP,200:P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY:3690,Exhibit%20AB,TAIWAN", "country": "TAIWAN", "state": "DC", "reg_num": "3690", "address": "Washington\u00a0\u00a0", "foreign_principal": "Taipei Economic & Cultural Representative Office in the U.S.", "date": "08/28/1995", "registrant": "International Trade & Development Agency, Inc."},
{"url": "f?p=171:200:::NO:RP,200:P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY:6194,Exhibit%20AB,JAPAN", "country": "JAPAN", "state": "DC", "reg_num": "6194", "address": "2520 Massachusetts Avenue, NW", "foreign_principal": "Embassy of Japan", "date": "11/08/2013", "registrant": "Parvin, C. Landon"},
{"url": "f?p=171:200:::NO:RP,200:P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY:6778,Exhibit%20AB,DOMINICAN%20REPUBLIC", "country": "DOMINICAN REPUBLIC", "reg_num": "6778", "address": "Avenida Mexico, National District", "foreign_principal": "Ministry of the Presidency", "date": "12/31/2019", "registrant": "Insignias Global, LLC"},
{"url": "f?p=171:200:::NO:RP,200:P200_REG_NUMBER,P200_DOC_TYPE,P200_COUNTRY:3911,Exhibit%20AB,BAHAMAS", "country": "BAHAMAS", "reg_num": "3911", "address": "Bolam House, George Street", "foreign_principal": "Bahamas Ministry of Tourism", "date": "08/08/2017", "registrant": "CMGRP, Inc."},
...
]
```

## Questions?

>I'm glad to answer, just ping me via email paulononaka@gmail.com 😄

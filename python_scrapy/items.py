from scrapy import Field
from scrapy import Item
from scrapy.loader.processors import TakeFirst


class ActiveForeignPrincipal(Item):
    url = Field(output_processor=TakeFirst())
    country = Field(output_processor=TakeFirst())
    state = Field(output_processor=TakeFirst())
    reg_num = Field(output_processor=TakeFirst())
    address = Field(output_processor=TakeFirst())
    foreign_principal = Field(output_processor=TakeFirst())
    date = Field(output_processor=TakeFirst())
    registrant = Field(output_processor=TakeFirst())
    exhibit_url = Field(output_processor=TakeFirst())

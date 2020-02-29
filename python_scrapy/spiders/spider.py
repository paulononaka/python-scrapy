import scrapy
from scrapy import FormRequest
from scrapy.loader import ItemLoader

from python_scrapy.items import ActiveForeignPrincipal


class FaraSpider(scrapy.Spider):
    name = 'fara'
    start_urls = [
        'https://efile.fara.gov/ords/f?p=171:130:0::NO:RP,130:P130_DATERANGE:N',
    ]

    ajax_url = 'https://efile.fara.gov/ords/wwv_flow.ajax'
    p_instance = None
    p_request = None

    def formdata(self, p_widget_action, p_widget_action_mod=None):
        form_hash = {
            'p_flow_id': '171',
            'p_flow_step_id': '130',
            'p_instance': self.p_instance,
            'p_request': 'PLUGIN=' + self.p_request,
            'p_widget_name': 'worksheet',
            'p_widget_mod': 'ACTION',
            'p_widget_action': p_widget_action,
            'p_widget_num_return': '15',
            'x01': '80340213897823017',
            'x02': '80341508791823021',
            'x03': 'COUNTRY_NAME',
        }
        if p_widget_action_mod is not None:
            form_hash['p_widget_action_mod'] = p_widget_action_mod
        return form_hash

    def parse(self, response):
        self.p_instance = response.xpath('//input[@id="pInstance"]/@value').get()
        self.p_request = response.xpath('/html/body/script[2]/text()').re(r'ajaxIdentifier":"(.*)"')[1]

        yield FormRequest(
            url=self.ajax_url,
            formdata=self.formdata('BREAK'),
            callback=self.next_page,
        )

    def next_page(self, response):
        for tr in response.xpath("//table[contains(@class, 'a-IRR-table')]//tr[not(th)]"):
            item = ItemLoader(item=ActiveForeignPrincipal(), response=response, selector=tr)
            item.add_css('url', "td[headers='LINK'] a::attr(href)")
            item.add_css('country', "td[headers='COUNTRY_NAME']::text")
            item.add_css('state', "td[headers='STATE']::text")
            item.add_css('reg_num', "td[headers='REG_NUMBER']::text")
            item.add_css('address', "td[headers='ADDRESS_1']::text")
            item.add_css('foreign_principal', "td[headers='FP_NAME']::text")
            item.add_css('date', "td[headers='FP_REG_DATE']::text")
            item.add_css('registrant', "td[headers='REGISTRANT_NAME']::text")
            item.add_css('exhibit_url', "td[headers='ccc']::text")
            yield item.load_item()

        p_widget_action_mod = response.xpath("//button[contains(@title, 'Next')]/@data-pagination").get()

        yield FormRequest(
            url=self.ajax_url,
            formdata=self.formdata('PAGE', p_widget_action_mod),
            callback=self.next_page,
        )

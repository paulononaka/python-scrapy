import scrapy
from scrapy import FormRequest
# from scrapy.shell import inspect_response


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
            callback=self.after_repage,
        )

    def after_repage(self, response):
        for tr in response.css('.a-IRR-table tr'):
            yield {
                'url': tr.css("td[headers='LINK'] a::attr(href)").get(),
                'country': tr.css("td[headers='COUNTRY_NAME']::text").get(),
                'state': tr.css("td[headers='STATE']::text").get(),
                'reg_num': tr.css("td[headers='REG_NUMBER']::text").get(),
                'address': tr.css("td[headers='ADDRESS_1']::text").get(),
                'foreign_principal': tr.css("td[headers='FP_NAME']::text").get(),
                'date': tr.css("td[headers='FP_REG_DATE']::text").get(),
                'registrant': tr.css("td[headers='REGISTRANT_NAME']::text").get(),
                'exhibit_url': tr.css("td[headers='ccc']::text").get(),
            }

        yield FormRequest(
            url=self.ajax_url,
            formdata=self.formdata('PAGE', 'pgR_min_row=16max_rows=15rows_fetched=15'),
            callback=self.next_page,
        )

    def next_page(self, response):
        # inspect_response(response, self)
        for tr in response.css('.a-IRR-table tr'):
            yield {
                'url': tr.css("td[headers='LINK'] a::attr(href)").get(),
                'country': tr.css("td[headers='COUNTRY_NAME']::text").get(),
                'state': tr.css("td[headers='STATE']::text").get(),
                'reg_num': tr.css("td[headers='REG_NUMBER']::text").get(),
                'address': tr.css("td[headers='ADDRESS_1']::text").get(),
                'foreign_principal': tr.css("td[headers='FP_NAME']::text").get(),
                'date': tr.css("td[headers='FP_REG_DATE']::text").get(),
                'registrant': tr.css("td[headers='REGISTRANT_NAME']::text").get(),
                'exhibit_url': tr.css("td[headers='ccc']::text").get(),
            }

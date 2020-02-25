import scrapy
from scrapy import FormRequest


class FaraSpider(scrapy.Spider):
    name = 'fara'
    start_urls = [
        'https://efile.fara.gov/ords/"'
        'f?p=171:130:0::NO:RP,130:P130_DATERANGE:N',
    ]

    def parse(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        p_instance = response.xpath('//input[@id="pInstance"]/@value').get()
        p_request = response.xpath(
            '/html/body/script[2]/text()',
        ).re(r'ajaxIdentifier":"(.*)"')[1]
        p_page_submission_id = response.xpath(
            '//input[@id="pPageSubmissionId"]/@value',
        ).get()

        return FormRequest(
            url='https://efile.fara.gov/ords/wwv_flow.ajax',
            formdata={
                'p_flow_id': '171',
                'p_flow_step_id': '130',
                'p_instance': p_instance,
                'p_request': 'PLUGIN=' + p_request,
                'p_widget_name': 'worksheet',
                'p_widget_mod': 'ACTION',
                'p_widget_action': 'BREAK',
                'p_widget_num_return': '15',
                'x01': '80340213897823017',
                'x02': '80341508791823021',
                'x03': 'COUNTRY_NAME',
                'p_json': '{"pageItems":null,"salt":"' + p_page_submission_id + '"}',
            },
            callback=self.after_repage,
        )

    def after_repage(self, response):
        from scrapy.shell import inspect_response
        inspect_response(response, self)
        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').get(),
        #         'author': quote.css('small.author::text').get(),
        #         'tags': quote.css('div.tags a.tag::text').getall(),
        #     }

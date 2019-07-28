# coding: utf-8
"""
module Ukrposhta API 0.0.1
autor Larin V. V.
version 1.0
create 27.07.2019
"""
import requests
import json

from requests import RequestException


class Poshta:
    APP_NAME = 'ecom/0.0.1'
    API_URL = 'https://www.ukrposhta.ua/'
    FORMS_URL = 'https://www.ukrposhta.ua/forms/'
    url = None
    key = None

    def __init__(self, key):
        """
        Constructor class
        """
        self.key = key

    def __del__(self):
        """
        Destructor class
        """
        del self.key

    def create_link(self, method, param='', url_type='api'):
        """
        Create URL API
        """
        if not isinstance(param, str):
            param = str(param)
        if param != '':
            param = '/' + param
        if url_type == 'api':
            self.url = self.API_URL + self.APP_NAME + '/' + method + param
        else:
            self.url = self.FORMS_URL + self.APP_NAME + '/' + method + param

    def prepare(self, data):
        """
        Prepare the data for the request
        :return json
        """
        return json.dumps(data, ensure_ascii=False)

    def request_data(self, method, data='', param='', type='post', url_type='api'):
        """
        Send request
        :return json
        """
        self.create_link(method, param, url_type)
        headers = {"Content-Type": "application/json",
                   "authorization": "Bearer " + self.key}
        resp = None

        try:
            if type == 'post':
                resp = requests.post(self.url, self.prepare(data), headers=headers)
            elif type == 'get':
                resp = requests.get(self.url, headers=headers)
            elif type == 'put':
                resp = requests.put(self.url, data=self.prepare(data), headers=headers)
            elif type == 'delete':
                resp = requests.delete(self.url, headers=headers)
        except RequestException as msg:
            return msg
        return resp.json()

    def phone_prohibited(self, token: str):
        """
        Request for a list of invalid phone numbers
        :return json
        """
        return self.request_data('phones', '', 'worldwide/prohibited?token=' + token, 'get')

    def phone_verify(self, token: str, phone: str):
        """
        Request to verify the entered phone number
        :return json
        """
        return self.request_data('phones', '', 'worldwide/prohibited/' + phone + '?token=' + token, 'get')

    def create_address(self, data):
        """ Create address """
        return self.request_data('addresses', data)

    def get_address(self, id: str):
        """
        Get address by id client
        :return: json
        """
        return self.request_data('addresses', '', id, 'get')

    def clients_list(self, token):
        """
        Get clients
        :return: json
        """
        return self.request_data('clients?token=' + token, '', '', 'get')

    def create_client(self, token: str, data):
        """
        Create client
        :return: json
        """
        return self.request_data('clients?token=' + token, data)

    def edit_client(self, token: str, uuid: str, data):
        """
        Edit client
        :return: json
        """
        return self.request_data('clients', data, uuid + '?token=' + token, 'put')

    def get_client_extid(self, token: str, extid: str):
        """
        Get client from ExternalID
        :return: json
        """
        return self.request_data('clients', '', 'external-id/' + extid + '?token=' + token, 'get')

    def delete_client_phone(self, token: str, phone_uuid: str):
        """
        Delete client phone number by phone uuid
        :return: json
        """
        return self.request_data('client-phones', '', phone_uuid + '?token=' + token, 'delete')

    def get_client_all_phone(self, token: str, client_uuid: str):
        """
        Get all phone number by client uuid
        :return: json
        """
        return self.request_data('client-phones?token=' + token + '&clientUuid=' + client_uuid, '', '', 'get')

    def delete_client_address(self, token: str, address_uuid: str):
        """
        Delete client address by address uuid
        :return: json
        """
        return self.request_data('client-addresses', '', address_uuid + '?token=' + token, 'delete')

    def get_client_all_address(self, token: str, client_uuid: str):
        """
        Get all address  by client uuid
        :return: json
        """
        return self.request_data('client-addresses?token=' + token + '&clientUuid=' + client_uuid, '', '', 'get')

    def delete_client_email(self, token: str, email_uuid: str):
        """
        Delete client email by email uuid
        :return: json
        """
        return self.request_data('client-emails', '', email_uuid + '?token=' + token, 'delete')

    def get_client_all_email(self, token: str, client_uuid: str):
        """
        Delete all client email address by client uuid
        :return: json
        """
        return self.request_data('client-emails?token=' + token + '&clientUuid=' + client_uuid, '', '', 'get')

    def get_client_by_phone(self, token: str, phone: str):
        """
        Get client by phone number
        :return: json
        """
        return self.request_data('clients', '', 'phone?token=' + token + '&countryISO3166=UA&phoneNumber=' + phone,
                                 'get')

    def error(self, content):
        """
        Check for error when executing the request
        :return: boolean
        """
        if content['message'] != '':
            print(content['message'])
            return False
        else:
            return True

    def save_pdf(self, pdf, path: str):
        """
        Save pdf file to disk
        """
        with open(path, 'wb') as file_handler:
            file_handler.write(pdf.content)

    def create_form(self, shipment_uuid_or_barcode: str, token, path: str, size=''):
        """
        Create all form
        """
        if size == '':
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/forms?token=' + token,
                                    'get',
                                    '')
        else:
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/forms?token=' + token + '&size=' + size,
                                    'get',
                                    '')
        if self.error(pdf):
            self.save_pdf(pdf, path)

    def create_form_cp71(self, shipment_uuid_or_barcode: str, token, path: str, size=''):
        """
        Create form CP71
        """
        if size == '':
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/cp71?token=' + token,
                                    'get',
                                    '')
        else:
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/cp71?token=' + token + '&size=' + size,
                                    'get',
                                    '')
        if self.error(pdf):
            self.save_pdf(pdf, path)

    def create_form_cn22(self, shipment_uuid_or_barcode: str, token, path: str, size=''):
        """
        Create form CN22
        """
        if size == '':
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/cn22?token=' + token,
                                    'get',
                                    '')
        else:
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/cn22?token=' + token + '&size=' + size,
                                    'get',
                                    '')
        if self.error(pdf):
            self.save_pdf(pdf, path)

    def create_form_cn23(self, shipment_uuid_or_barcode: str, token, path: str, size=''):
        """
        Create form CN23
        """
        if size == '':
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/cn23?token=' + token,
                                    'get',
                                    '')
        else:
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/cn23?token=' + token + '&size=' + size,
                                    'get',
                                    '')
        if self.error(pdf):
            self.save_pdf(pdf, path)

    def create_form_103a(self, shipment_group_uuid: str, token, path: str, size=''):
        """
        Create form 103a
        """
        if size == '':
            pdf = self.request_data('shipment-groups',
                                    '',
                                    shipment_group_uuid + '/form103a?token=' + token,
                                    'get',
                                    '')
        else:
            pdf = self.request_data('shipment-groups',
                                    '',
                                    shipment_group_uuid + '/form103a?token=' + token + '&size=' + size,
                                    'get',
                                    '')
        if self.error(pdf):
            self.save_pdf(pdf, path)

    def create_form_dl(self, shipment_uuid_or_barcode: str, token, path: str, size=''):
        """
        Create form DL
        """
        if size == '':
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/dl?token=' + token,
                                    'get',
                                    '')
        else:
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/dl?token=' + token + '&size=' + size,
                                    'get',
                                    '')
        if self.error(pdf):
            self.save_pdf(pdf, path)

    def create_form_cn6(self, shipment_uuid_or_barcode: str, token, path: str, size=''):
        """
        Create form CN6
        """
        if size == '':
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/cn6?token=' + token,
                                    'get',
                                    '')
        else:
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/cn6?token=' + token + '&size=' + size,
                                    'get',
                                    '')
        if self.error(pdf):
            self.save_pdf(pdf, path)

    def create_form_tfp3(self, shipment_uuid_or_barcode: str, token, path: str, size=''):
        """
        Create form TFP3
        """
        if size == '':
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/tfp3?token=' + token,
                                    'get',
                                    '')
        else:
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/tfp3?token=' + token + '&size=' + size,
                                    'get',
                                    '')
        if self.error(pdf):
            self.save_pdf(pdf, path)

    def create_form_cp95_cn29(self, shipment_uuid_or_barcode: str, token, path: str, size=''):
        """
        Create form CP95 and CN29
        """
        if size == '':
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/cp95_cn29?token=' + token,
                                    'get',
                                    '')
        else:
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/cp95_cn29?token=' + token + '&size=' + size,
                                    'get',
                                    '')
        if self.error(pdf):
            self.save_pdf(pdf, path)

    def create_form_cn07(self, shipment_uuid_or_barcode: str, token, path: str, size=''):
        """
        Create form CN07
        """
        if size == '':
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/cn07?token=' + token,
                                    'get',
                                    '')
        else:
            pdf = self.request_data('international/shipments',
                                    '',
                                    shipment_uuid_or_barcode + '/cn07?token=' + token + '&size=' + size,
                                    'get',
                                    '')
        if self.error(pdf):
            self.save_pdf(pdf, path)

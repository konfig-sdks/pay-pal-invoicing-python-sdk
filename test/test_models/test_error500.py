# coding: utf-8

"""
    Invoices

    Use the Invoicing API to create, send, and manage invoices. You can also use the API or webhooks to track invoice payments. When you send an invoice to a customer, the invoice moves from draft to payable state. PayPal then emails the customer a link to the invoice on the PayPal website. Customers with a PayPal account can log in and pay the invoice with PayPal. Alternatively, customers can pay as a guest with a debit card or credit card. For more information, see the <a href=\"/docs/invoicing/\">Invoicing Overview</a> and the <a href=\"/docs/invoicing/basic-integration/\">Invoicing Integration Guide</a>.

    The version of the OpenAPI document: 2.3
    Generated by: https://konfigthis.com
"""

import unittest

import pay_pal_invoicing_python_sdk
from pay_pal_invoicing_python_sdk.model.error500 import Error500
from pay_pal_invoicing_python_sdk import configuration


class TestError500(unittest.TestCase):
    """Error500 unit test stubs"""
    pass


if __name__ == '__main__':
    unittest.main()

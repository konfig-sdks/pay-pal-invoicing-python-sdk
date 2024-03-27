# coding: utf-8

"""
    Invoices

    Use the Invoicing API to create, send, and manage invoices. You can also use the API or webhooks to track invoice payments. When you send an invoice to a customer, the invoice moves from draft to payable state. PayPal then emails the customer a link to the invoice on the PayPal website. Customers with a PayPal account can log in and pay the invoice with PayPal. Alternatively, customers can pay as a guest with a debit card or credit card. For more information, see the <a href=\"/docs/invoicing/\">Invoicing Overview</a> and the <a href=\"/docs/invoicing/basic-integration/\">Invoicing Integration Guide</a>.

    The version of the OpenAPI document: 2.3
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from pay_pal_invoicing_python_sdk.type.error_details import ErrorDetails
from pay_pal_invoicing_python_sdk.type.error_link_description import ErrorLinkDescription

class RequiredError415(TypedDict):
    pass

class OptionalError415(TypedDict, total=False):
    name: str

    message: str

    details: typing.List[ErrorDetails]

    # The PayPal internal ID. Used for correlation purposes.
    debug_id: str

    # An array of request-related [HATEOAS links](https://en.wikipedia.org/wiki/HATEOAS).
    links: typing.List[ErrorLinkDescription]

class Error415(RequiredError415, OptionalError415):
    pass

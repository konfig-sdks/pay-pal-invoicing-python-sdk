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

from pay_pal_invoicing_python_sdk.type.date_time import DateTime

class RequiredTemplateMetadata(TypedDict):
    pass

class OptionalTemplateMetadata(TypedDict, total=False):
    create_time: DateTime

    # The email address of the account that created the resource.
    created_by: str

    last_update_time: DateTime

    # The email address of the account that last edited the resource.
    last_updated_by: str

class TemplateMetadata(RequiredTemplateMetadata, OptionalTemplateMetadata):
    pass

# coding: utf-8

"""
    Invoices

    Use the Invoicing API to create, send, and manage invoices. You can also use the API or webhooks to track invoice payments. When you send an invoice to a customer, the invoice moves from draft to payable state. PayPal then emails the customer a link to the invoice on the PayPal website. Customers with a PayPal account can log in and pay the invoice with PayPal. Alternatively, customers can pay as a guest with a debit card or credit card. For more information, see the <a href=\"/docs/invoicing/\">Invoicing Overview</a> and the <a href=\"/docs/invoicing/basic-integration/\">Invoicing Integration Guide</a>.

    The version of the OpenAPI document: 2.3
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from pay_pal_invoicing_python_sdk import schemas  # noqa: F401


class TemplateSubtotalField(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The field names in the template for discount, shipping, and custom amounts.
    """


    class MetaOapg:
        enum_value_to_name = {
            "DISCOUNT": "DISCOUNT",
            "SHIPPING": "SHIPPING",
            "CUSTOM": "CUSTOM",
        }
    
    @schemas.classproperty
    def DISCOUNT(cls):
        return cls("DISCOUNT")
    
    @schemas.classproperty
    def SHIPPING(cls):
        return cls("SHIPPING")
    
    @schemas.classproperty
    def CUSTOM(cls):
        return cls("CUSTOM")

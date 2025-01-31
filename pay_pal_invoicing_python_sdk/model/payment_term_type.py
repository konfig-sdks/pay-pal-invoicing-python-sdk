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


class PaymentTermType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The payment term. Payment can be due upon receipt, a specified date, or in a set number of days.
    """


    class MetaOapg:
        enum_value_to_name = {
            "DUE_ON_RECEIPT": "DUE_ON_RECEIPT",
            "DUE_ON_DATE_SPECIFIED": "DUE_ON_DATE_SPECIFIED",
            "NET_10": "NET_10",
            "NET_15": "NET_15",
            "NET_30": "NET_30",
            "NET_45": "NET_45",
            "NET_60": "NET_60",
            "NET_90": "NET_90",
            "NO_DUE_DATE": "NO_DUE_DATE",
        }
    
    @schemas.classproperty
    def DUE_ON_RECEIPT(cls):
        return cls("DUE_ON_RECEIPT")
    
    @schemas.classproperty
    def DUE_ON_DATE_SPECIFIED(cls):
        return cls("DUE_ON_DATE_SPECIFIED")
    
    @schemas.classproperty
    def NET_10(cls):
        return cls("NET_10")
    
    @schemas.classproperty
    def NET_15(cls):
        return cls("NET_15")
    
    @schemas.classproperty
    def NET_30(cls):
        return cls("NET_30")
    
    @schemas.classproperty
    def NET_45(cls):
        return cls("NET_45")
    
    @schemas.classproperty
    def NET_60(cls):
        return cls("NET_60")
    
    @schemas.classproperty
    def NET_90(cls):
        return cls("NET_90")
    
    @schemas.classproperty
    def NO_DUE_DATE(cls):
        return cls("NO_DUE_DATE")

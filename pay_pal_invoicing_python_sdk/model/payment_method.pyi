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


class PaymentMethod(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The payment mode or method through which the invoicer can accept the payments.
    """
    
    @schemas.classproperty
    def BANK_TRANSFER(cls):
        return cls("BANK_TRANSFER")
    
    @schemas.classproperty
    def CASH(cls):
        return cls("CASH")
    
    @schemas.classproperty
    def CHECK(cls):
        return cls("CHECK")
    
    @schemas.classproperty
    def CREDIT_CARD(cls):
        return cls("CREDIT_CARD")
    
    @schemas.classproperty
    def DEBIT_CARD(cls):
        return cls("DEBIT_CARD")
    
    @schemas.classproperty
    def PAYPAL(cls):
        return cls("PAYPAL")
    
    @schemas.classproperty
    def WIRE_TRANSFER(cls):
        return cls("WIRE_TRANSFER")
    
    @schemas.classproperty
    def OTHER(cls):
        return cls("OTHER")

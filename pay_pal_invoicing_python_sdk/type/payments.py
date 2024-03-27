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

from pay_pal_invoicing_python_sdk.type.money import Money
from pay_pal_invoicing_python_sdk.type.payment_detail import PaymentDetail

class RequiredPayments(TypedDict):
    pass

class OptionalPayments(TypedDict, total=False):
    paid_amount: Money

    # An array of payment details for the invoice. The payment details of the invoice like payment type, method, date, discount and transaction type.
    transactions: typing.List[PaymentDetail]

class Payments(RequiredPayments, OptionalPayments):
    pass

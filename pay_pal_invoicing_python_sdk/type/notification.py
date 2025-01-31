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

from pay_pal_invoicing_python_sdk.type.email_address import EmailAddress

class RequiredNotification(TypedDict):
    pass

class OptionalNotification(TypedDict, total=False):
    # The subject of the email that is sent as a notification to the recipient.
    subject: str

    # A note to the payer.
    note: str

    # Indicates whether to send a copy of the email to the merchant.
    send_to_invoicer: bool

    # Indicates whether to send a copy of the email to the recipient.
    send_to_recipient: bool

    # An array of one or more CC: emails to which notifications are sent. If you omit this parameter, a notification is sent to all CC: email addresses that are part of the invoice.<blockquote><strong>Note:</strong> Valid values are email addresses in the `additional_recipients` value associated with the invoice.</blockquote>
    additional_recipients: typing.List[EmailAddress]

class Notification(RequiredNotification, OptionalNotification):
    pass

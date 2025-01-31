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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from pay_pal_invoicing_python_sdk.pydantic.amount_summary_detail import AmountSummaryDetail
from pay_pal_invoicing_python_sdk.pydantic.configuration import Configuration
from pay_pal_invoicing_python_sdk.pydantic.email_address import EmailAddress
from pay_pal_invoicing_python_sdk.pydantic.invoice_detail import InvoiceDetail
from pay_pal_invoicing_python_sdk.pydantic.invoice_status import InvoiceStatus
from pay_pal_invoicing_python_sdk.pydantic.invoicer_info import InvoicerInfo
from pay_pal_invoicing_python_sdk.pydantic.item import Item
from pay_pal_invoicing_python_sdk.pydantic.link_description import LinkDescription
from pay_pal_invoicing_python_sdk.pydantic.money import Money
from pay_pal_invoicing_python_sdk.pydantic.payments import Payments
from pay_pal_invoicing_python_sdk.pydantic.recipient_info import RecipientInfo
from pay_pal_invoicing_python_sdk.pydantic.refunds import Refunds

class Invoice(BaseModel):
    detail: InvoiceDetail = Field(alias='detail')

    # The ID of the invoice.
    id: typing.Optional[str] = Field(None, alias='id')

    # The parent ID to an invoice that defines the group invoice to which the invoice is related.
    parent_id: typing.Optional[str] = Field(None, alias='parent_id')

    status: typing.Optional[InvoiceStatus] = Field(None, alias='status')

    invoicer: typing.Optional[InvoicerInfo] = Field(None, alias='invoicer')

    # The billing and shipping information. Includes name, email, address, phone and language.
    primary_recipients: typing.Optional[typing.List[RecipientInfo]] = Field(None, alias='primary_recipients')

    # An array of one or more CC: emails to which notifications are sent. If you omit this parameter, a notification is sent to all CC: email addresses that are part of the invoice.<blockquote><strong>Note:</strong> Valid values are email addresses in the `additional_recipients` value associated with the invoice.</blockquote>
    additional_recipients: typing.Optional[typing.List[EmailAddress]] = Field(None, alias='additional_recipients')

    # An array of invoice line item information.
    items: typing.Optional[typing.List[Item]] = Field(None, alias='items')

    configuration: typing.Optional[Configuration] = Field(None, alias='configuration')

    amount: typing.Optional[AmountSummaryDetail] = Field(None, alias='amount')

    due_amount: typing.Optional[Money] = Field(None, alias='due_amount')

    gratuity: typing.Optional[Money] = Field(None, alias='gratuity')

    payments: typing.Optional[Payments] = Field(None, alias='payments')

    refunds: typing.Optional[Refunds] = Field(None, alias='refunds')

    # An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links).
    links: typing.Optional[typing.List[LinkDescription]] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

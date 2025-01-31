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

from pay_pal_invoicing_python_sdk.pydantic.amount_range import AmountRange
from pay_pal_invoicing_python_sdk.pydantic.currency_code import CurrencyCode
from pay_pal_invoicing_python_sdk.pydantic.date_range import DateRange
from pay_pal_invoicing_python_sdk.pydantic.date_time_range import DateTimeRange
from pay_pal_invoicing_python_sdk.pydantic.invoice_status import InvoiceStatus
from pay_pal_invoicing_python_sdk.pydantic.search_data_fields import SearchDataFields

class SearchData(BaseModel):
    # Filters the search by the email address.
    recipient_email: typing.Optional[str] = Field(None, alias='recipient_email')

    # Filters the search by the recipient first name.
    recipient_first_name: typing.Optional[str] = Field(None, alias='recipient_first_name')

    # Filters the search by the recipient last name.
    recipient_last_name: typing.Optional[str] = Field(None, alias='recipient_last_name')

    # Filters the search by the recipient business name.
    recipient_business_name: typing.Optional[str] = Field(None, alias='recipient_business_name')

    # Filters the search by the invoice number.
    invoice_number: typing.Optional[str] = Field(None, alias='invoice_number')

    # An array of status values.
    status: typing.Optional[typing.List[InvoiceStatus]] = Field(None, alias='status')

    # The reference data, such as a PO number.
    reference: typing.Optional[str] = Field(None, alias='reference')

    currency_code: typing.Optional[CurrencyCode] = Field(None, alias='currency_code')

    # A private bookkeeping memo for the user.
    memo: typing.Optional[str] = Field(None, alias='memo')

    total_amount_range: typing.Optional[AmountRange] = Field(None, alias='total_amount_range')

    invoice_date_range: typing.Optional[DateRange] = Field(None, alias='invoice_date_range')

    due_date_range: typing.Optional[DateRange] = Field(None, alias='due_date_range')

    payment_date_range: typing.Optional[DateTimeRange] = Field(None, alias='payment_date_range')

    creation_date_range: typing.Optional[DateTimeRange] = Field(None, alias='creation_date_range')

    # Indicates whether to list merchant-archived invoices in the response. Value is:<ul><li><code>true</code>. Response lists only merchant-archived invoices.</li><li><code>false</code>. Response lists only unarchived invoices.</li><li><code>null</code>. Response lists all invoices.</li></ul>
    archived: typing.Optional[bool] = Field(None, alias='archived')

    fields: typing.Optional[SearchDataFields] = Field(None, alias='fields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

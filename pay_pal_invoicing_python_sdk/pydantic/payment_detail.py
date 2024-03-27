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

from pay_pal_invoicing_python_sdk.pydantic.contact_name_address import ContactNameAddress
from pay_pal_invoicing_python_sdk.pydantic.date_no_time import DateNoTime
from pay_pal_invoicing_python_sdk.pydantic.money import Money
from pay_pal_invoicing_python_sdk.pydantic.payment_method import PaymentMethod
from pay_pal_invoicing_python_sdk.pydantic.payment_type import PaymentType

class PaymentDetail(BaseModel):
    method: PaymentMethod = Field(alias='method')

    type: typing.Optional[PaymentType] = Field(None, alias='type')

    # The ID for a PayPal payment transaction. Required for the `PAYPAL` payment type.
    payment_id: typing.Optional[str] = Field(None, alias='payment_id')

    payment_date: typing.Optional[DateNoTime] = Field(None, alias='payment_date')

    # A note associated with an external cash or check payment.
    note: typing.Optional[str] = Field(None, alias='note')

    amount: typing.Optional[Money] = Field(None, alias='amount')

    shipping_info: typing.Optional[ContactNameAddress] = Field(None, alias='shipping_info')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

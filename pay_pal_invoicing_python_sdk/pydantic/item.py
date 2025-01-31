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

from pay_pal_invoicing_python_sdk.pydantic.date_no_time import DateNoTime
from pay_pal_invoicing_python_sdk.pydantic.discount import Discount
from pay_pal_invoicing_python_sdk.pydantic.money import Money
from pay_pal_invoicing_python_sdk.pydantic.tax import Tax
from pay_pal_invoicing_python_sdk.pydantic.unit_of_measure import UnitOfMeasure

class Item(BaseModel):
    # The item name for the invoice line item.
    name: str = Field(alias='name')

    # The quantity of the item that the invoicer provides to the payer. Value is from `-1000000` to `1000000`. Supports up to five decimal places.
    quantity: str = Field(alias='quantity')

    unit_amount: Money = Field(alias='unit_amount')

    # The item description for the invoice line item.
    description: typing.Optional[str] = Field(None, alias='description')

    # The ID of the invoice line item.
    id: typing.Optional[str] = Field(None, alias='id')

    tax: typing.Optional[Tax] = Field(None, alias='tax')

    item_date: typing.Optional[DateNoTime] = Field(None, alias='item_date')

    discount: typing.Optional[Discount] = Field(None, alias='discount')

    unit_of_measure: typing.Optional[UnitOfMeasure] = Field(None, alias='unit_of_measure')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

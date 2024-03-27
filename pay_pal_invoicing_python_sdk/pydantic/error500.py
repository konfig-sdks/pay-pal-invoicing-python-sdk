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

from pay_pal_invoicing_python_sdk.pydantic.error_link_description import ErrorLinkDescription

class Error500(BaseModel):
    name: typing.Optional[Literal["INTERNAL_SERVER_ERROR"]] = Field(None, alias='name')

    message: typing.Optional[Literal["An internal server error occurred."]] = Field(None, alias='message')

    # The PayPal internal ID. Used for correlation purposes.
    debug_id: typing.Optional[str] = Field(None, alias='debug_id')

    # An array of request-related [HATEOAS links](https://en.wikipedia.org/wiki/HATEOAS).
    links: typing.Optional[typing.List[ErrorLinkDescription]] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

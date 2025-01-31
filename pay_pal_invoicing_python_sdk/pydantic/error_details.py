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


class ErrorDetails(BaseModel):
    # The unique, fine-grained application-level error code.
    issue: str = Field(alias='issue')

    # The human-readable description for an issue. The description can change over the lifetime of an API, so clients must not depend on this value.
    description: typing.Optional[str] = Field(None, alias='description')

    # The field that caused the error. If this field is in the body, set this value to the field's JSON pointer value. Required for client-side errors.
    field: typing.Optional[str] = Field(None, alias='field')

    # The value of the field that caused the error.
    value: typing.Optional[str] = Field(None, alias='value')

    # The location of the field that caused the error. Value is `body`, `path`, or `query`.
    location: typing.Optional[str] = Field(None, alias='location')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

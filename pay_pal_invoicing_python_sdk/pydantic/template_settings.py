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

from pay_pal_invoicing_python_sdk.pydantic.template_item_setting import TemplateItemSetting
from pay_pal_invoicing_python_sdk.pydantic.template_subtotal_setting import TemplateSubtotalSetting

class TemplateSettings(BaseModel):
    # The template item headers display preference.
    template_item_settings: typing.Optional[typing.List[TemplateItemSetting]] = Field(None, alias='template_item_settings')

    # The template subtotal headers display preference.
    template_subtotal_settings: typing.Optional[typing.List[TemplateSubtotalSetting]] = Field(None, alias='template_subtotal_settings')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

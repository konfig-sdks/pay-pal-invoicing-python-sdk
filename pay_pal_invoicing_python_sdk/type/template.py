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

from pay_pal_invoicing_python_sdk.type.link_description import LinkDescription
from pay_pal_invoicing_python_sdk.type.template_info import TemplateInfo
from pay_pal_invoicing_python_sdk.type.template_settings import TemplateSettings
from pay_pal_invoicing_python_sdk.type.unit_of_measure import UnitOfMeasure

class RequiredTemplate(TypedDict):
    pass

class OptionalTemplate(TypedDict, total=False):
    # The ID of the template.
    id: str

    # The template name.<blockquote><strong>Note:</strong> The template name must be unique.</blockquote>
    name: str

    # Indicates whether this template is the default template. A invoicer can have one default template.
    default_template: bool

    template_info: TemplateInfo

    settings: TemplateSettings

    unit_of_measure: UnitOfMeasure

    # Indicates whether this template is a invoicer-created custom template. The system generates non-custom templates.
    standard_template: bool

    # An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links).
    links: typing.List[LinkDescription]

class Template(RequiredTemplate, OptionalTemplate):
    pass

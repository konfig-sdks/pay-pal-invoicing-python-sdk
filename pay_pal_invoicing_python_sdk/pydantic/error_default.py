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

from pay_pal_invoicing_python_sdk.pydantic.error400 import Error400
from pay_pal_invoicing_python_sdk.pydantic.error401 import Error401
from pay_pal_invoicing_python_sdk.pydantic.error403 import Error403
from pay_pal_invoicing_python_sdk.pydantic.error404 import Error404
from pay_pal_invoicing_python_sdk.pydantic.error409 import Error409
from pay_pal_invoicing_python_sdk.pydantic.error415 import Error415
from pay_pal_invoicing_python_sdk.pydantic.error422 import Error422
from pay_pal_invoicing_python_sdk.pydantic.error500 import Error500
from pay_pal_invoicing_python_sdk.pydantic.error503 import Error503

ErrorDefault = typing.Union[Error400,Error401,Error403,Error404,Error409,Error415,Error422,Error500,Error503]

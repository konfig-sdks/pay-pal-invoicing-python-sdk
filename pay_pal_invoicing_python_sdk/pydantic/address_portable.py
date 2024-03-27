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

from pay_pal_invoicing_python_sdk.pydantic.address_portable_address_details import AddressPortableAddressDetails
from pay_pal_invoicing_python_sdk.pydantic.country_code import CountryCode

class AddressPortable(BaseModel):
    country_code: CountryCode = Field(alias='country_code')

    # The first line of the address. For example, number or street. For example, `173 Drury Lane`. Required for data entry and compliance and risk checks. Must contain the full address.
    address_line_1: typing.Optional[str] = Field(None, alias='address_line_1')

    # The second line of the address. For example, suite or apartment number.
    address_line_2: typing.Optional[str] = Field(None, alias='address_line_2')

    # The third line of the address, if needed. For example, a street complement for Brazil, direction text, such as `next to Walmart`, or a landmark in an Indian address.
    address_line_3: typing.Optional[str] = Field(None, alias='address_line_3')

    # The neighborhood, ward, or district. Smaller than `admin_area_level_3` or `sub_locality`. Value is:<ul><li>The postal sorting code for Guernsey and many French territories, such as French Guiana.</li><li>The fine-grained administrative levels in China.</li></ul>
    admin_area_4: typing.Optional[str] = Field(None, alias='admin_area_4')

    # A sub-locality, suburb, neighborhood, or district. Smaller than `admin_area_level_2`. Value is:<ul><li>Brazil. Suburb, bairro, or neighborhood.</li><li>India. Sub-locality or district. Street name information is not always available but a sub-locality or district can be a very small area.</li></ul>
    admin_area_3: typing.Optional[str] = Field(None, alias='admin_area_3')

    # A city, town, or village. Smaller than `admin_area_level_1`.
    admin_area_2: typing.Optional[str] = Field(None, alias='admin_area_2')

    # The highest level sub-division in a country, which is usually a province, state, or ISO-3166-2 subdivision. Format for postal delivery. For example, `CA` and not `California`. Value, by country, is:<ul><li>UK. A county.</li><li>US. A state.</li><li>Canada. A province.</li><li>Japan. A prefecture.</li><li>Switzerland. A kanton.</li></ul>
    admin_area_1: typing.Optional[str] = Field(None, alias='admin_area_1')

    # The postal code, which is the zip code or equivalent. Typically required for countries with a postal code or an equivalent. See [postal code](https://en.wikipedia.org/wiki/Postal_code).
    postal_code: typing.Optional[str] = Field(None, alias='postal_code')

    address_details: typing.Optional[AddressPortableAddressDetails] = Field(None, alias='address_details')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )

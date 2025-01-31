# coding: utf-8

"""
    Invoices

    Use the Invoicing API to create, send, and manage invoices. You can also use the API or webhooks to track invoice payments. When you send an invoice to a customer, the invoice moves from draft to payable state. PayPal then emails the customer a link to the invoice on the PayPal website. Customers with a PayPal account can log in and pay the invoice with PayPal. Alternatively, customers can pay as a guest with a debit card or credit card. For more information, see the <a href=\"/docs/invoicing/\">Invoicing Overview</a> and the <a href=\"/docs/invoicing/basic-integration/\">Invoicing Integration Guide</a>.

    The version of the OpenAPI document: 2.3
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from pay_pal_invoicing_python_sdk import schemas  # noqa: F401


class AmountWithBreakdown(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The breakdown of the amount. Includes total item amount, total tax amount, custom amount, and shipping and discounts, if any.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def item_total() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def discount() -> typing.Type['AggregatedDiscount']:
                return AggregatedDiscount
        
            @staticmethod
            def tax_total() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def shipping() -> typing.Type['ShippingCost']:
                return ShippingCost
        
            @staticmethod
            def custom() -> typing.Type['CustomAmount']:
                return CustomAmount
            __annotations__ = {
                "item_total": item_total,
                "discount": discount,
                "tax_total": tax_total,
                "shipping": shipping,
                "custom": custom,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["item_total"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discount"]) -> 'AggregatedDiscount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax_total"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping"]) -> 'ShippingCost': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom"]) -> 'CustomAmount': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["item_total", "discount", "tax_total", "shipping", "custom", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["item_total"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discount"]) -> typing.Union['AggregatedDiscount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax_total"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping"]) -> typing.Union['ShippingCost', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom"]) -> typing.Union['CustomAmount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["item_total", "discount", "tax_total", "shipping", "custom", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        item_total: typing.Union['Money', schemas.Unset] = schemas.unset,
        discount: typing.Union['AggregatedDiscount', schemas.Unset] = schemas.unset,
        tax_total: typing.Union['Money', schemas.Unset] = schemas.unset,
        shipping: typing.Union['ShippingCost', schemas.Unset] = schemas.unset,
        custom: typing.Union['CustomAmount', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AmountWithBreakdown':
        return super().__new__(
            cls,
            *args,
            item_total=item_total,
            discount=discount,
            tax_total=tax_total,
            shipping=shipping,
            custom=custom,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_invoicing_python_sdk.model.aggregated_discount import AggregatedDiscount
from pay_pal_invoicing_python_sdk.model.custom_amount import CustomAmount
from pay_pal_invoicing_python_sdk.model.money import Money
from pay_pal_invoicing_python_sdk.model.shipping_cost import ShippingCost

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


class TemplateSubtotalSetting(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The template subtotal setting. Includes the field name and display preference.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def field_name() -> typing.Type['TemplateSubtotalField']:
                return TemplateSubtotalField
        
            @staticmethod
            def display_preference() -> typing.Type['TemplateDisplayPreference']:
                return TemplateDisplayPreference
            __annotations__ = {
                "field_name": field_name,
                "display_preference": display_preference,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_name"]) -> 'TemplateSubtotalField': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_preference"]) -> 'TemplateDisplayPreference': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["field_name", "display_preference", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_name"]) -> typing.Union['TemplateSubtotalField', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_preference"]) -> typing.Union['TemplateDisplayPreference', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["field_name", "display_preference", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        field_name: typing.Union['TemplateSubtotalField', schemas.Unset] = schemas.unset,
        display_preference: typing.Union['TemplateDisplayPreference', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateSubtotalSetting':
        return super().__new__(
            cls,
            *args,
            field_name=field_name,
            display_preference=display_preference,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_invoicing_python_sdk.model.template_display_preference import TemplateDisplayPreference
from pay_pal_invoicing_python_sdk.model.template_subtotal_field import TemplateSubtotalField

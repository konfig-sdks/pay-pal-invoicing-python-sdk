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


class TemplateSettings(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The template settings. Sets a template as the default template or edit template.
    """


    class MetaOapg:
        
        class properties:
            
            
            class template_item_settings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TemplateItemSetting']:
                        return TemplateItemSetting
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TemplateItemSetting'], typing.List['TemplateItemSetting']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'template_item_settings':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TemplateItemSetting':
                    return super().__getitem__(i)
            
            
            class template_subtotal_settings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TemplateSubtotalSetting']:
                        return TemplateSubtotalSetting
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TemplateSubtotalSetting'], typing.List['TemplateSubtotalSetting']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'template_subtotal_settings':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TemplateSubtotalSetting':
                    return super().__getitem__(i)
            __annotations__ = {
                "template_item_settings": template_item_settings,
                "template_subtotal_settings": template_subtotal_settings,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template_item_settings"]) -> MetaOapg.properties.template_item_settings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template_subtotal_settings"]) -> MetaOapg.properties.template_subtotal_settings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["template_item_settings", "template_subtotal_settings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template_item_settings"]) -> typing.Union[MetaOapg.properties.template_item_settings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template_subtotal_settings"]) -> typing.Union[MetaOapg.properties.template_subtotal_settings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["template_item_settings", "template_subtotal_settings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        template_item_settings: typing.Union[MetaOapg.properties.template_item_settings, list, tuple, schemas.Unset] = schemas.unset,
        template_subtotal_settings: typing.Union[MetaOapg.properties.template_subtotal_settings, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateSettings':
        return super().__new__(
            cls,
            *args,
            template_item_settings=template_item_settings,
            template_subtotal_settings=template_subtotal_settings,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_invoicing_python_sdk.model.template_item_setting import TemplateItemSetting
from pay_pal_invoicing_python_sdk.model.template_subtotal_setting import TemplateSubtotalSetting

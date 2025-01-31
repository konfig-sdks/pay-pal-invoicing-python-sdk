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


class Template(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The template with invoice details to load with all captured fields.
    """


    class MetaOapg:
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            default_template = schemas.BoolSchema
        
            @staticmethod
            def template_info() -> typing.Type['TemplateInfo']:
                return TemplateInfo
        
            @staticmethod
            def settings() -> typing.Type['TemplateSettings']:
                return TemplateSettings
        
            @staticmethod
            def unit_of_measure() -> typing.Type['UnitOfMeasure']:
                return UnitOfMeasure
            standard_template = schemas.BoolSchema
            
            
            class links(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LinkDescription']:
                        return LinkDescription
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['LinkDescription'], typing.List['LinkDescription']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'links':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'LinkDescription':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "name": name,
                "default_template": default_template,
                "template_info": template_info,
                "settings": settings,
                "unit_of_measure": unit_of_measure,
                "standard_template": standard_template,
                "links": links,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_template"]) -> MetaOapg.properties.default_template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["template_info"]) -> 'TemplateInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["settings"]) -> 'TemplateSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unit_of_measure"]) -> 'UnitOfMeasure': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["standard_template"]) -> MetaOapg.properties.standard_template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "default_template", "template_info", "settings", "unit_of_measure", "standard_template", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_template"]) -> typing.Union[MetaOapg.properties.default_template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["template_info"]) -> typing.Union['TemplateInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["settings"]) -> typing.Union['TemplateSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unit_of_measure"]) -> typing.Union['UnitOfMeasure', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["standard_template"]) -> typing.Union[MetaOapg.properties.standard_template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "default_template", "template_info", "settings", "unit_of_measure", "standard_template", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        default_template: typing.Union[MetaOapg.properties.default_template, bool, schemas.Unset] = schemas.unset,
        template_info: typing.Union['TemplateInfo', schemas.Unset] = schemas.unset,
        settings: typing.Union['TemplateSettings', schemas.Unset] = schemas.unset,
        unit_of_measure: typing.Union['UnitOfMeasure', schemas.Unset] = schemas.unset,
        standard_template: typing.Union[MetaOapg.properties.standard_template, bool, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Template':
        return super().__new__(
            cls,
            *args,
            id=id,
            name=name,
            default_template=default_template,
            template_info=template_info,
            settings=settings,
            unit_of_measure=unit_of_measure,
            standard_template=standard_template,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_invoicing_python_sdk.model.link_description import LinkDescription
from pay_pal_invoicing_python_sdk.model.template_info import TemplateInfo
from pay_pal_invoicing_python_sdk.model.template_settings import TemplateSettings
from pay_pal_invoicing_python_sdk.model.unit_of_measure import UnitOfMeasure

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


class Metadata(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The audit metadata. Captures all invoicing actions on create, send, update, and cancel.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def cancel_time() -> typing.Type['DateTime']:
                        return DateTime
                    cancelled_by = schemas.StrSchema
                
                    @staticmethod
                    def first_sent_time() -> typing.Type['DateTime']:
                        return DateTime
                
                    @staticmethod
                    def last_sent_time() -> typing.Type['DateTime']:
                        return DateTime
                    last_sent_by = schemas.StrSchema
                
                    @staticmethod
                    def created_by_flow() -> typing.Type['InvoiceCreationFlow']:
                        return InvoiceCreationFlow
                    recipient_view_url = schemas.StrSchema
                    invoicer_view_url = schemas.StrSchema
                    __annotations__ = {
                        "cancel_time": cancel_time,
                        "cancelled_by": cancelled_by,
                        "first_sent_time": first_sent_time,
                        "last_sent_time": last_sent_time,
                        "last_sent_by": last_sent_by,
                        "created_by_flow": created_by_flow,
                        "recipient_view_url": recipient_view_url,
                        "invoicer_view_url": invoicer_view_url,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["cancel_time"]) -> 'DateTime': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["cancelled_by"]) -> MetaOapg.properties.cancelled_by: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["first_sent_time"]) -> 'DateTime': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["last_sent_time"]) -> 'DateTime': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["last_sent_by"]) -> MetaOapg.properties.last_sent_by: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["created_by_flow"]) -> 'InvoiceCreationFlow': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["recipient_view_url"]) -> MetaOapg.properties.recipient_view_url: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoicer_view_url"]) -> MetaOapg.properties.invoicer_view_url: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["cancel_time", "cancelled_by", "first_sent_time", "last_sent_time", "last_sent_by", "created_by_flow", "recipient_view_url", "invoicer_view_url", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["cancel_time"]) -> typing.Union['DateTime', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["cancelled_by"]) -> typing.Union[MetaOapg.properties.cancelled_by, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["first_sent_time"]) -> typing.Union['DateTime', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["last_sent_time"]) -> typing.Union['DateTime', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["last_sent_by"]) -> typing.Union[MetaOapg.properties.last_sent_by, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["created_by_flow"]) -> typing.Union['InvoiceCreationFlow', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["recipient_view_url"]) -> typing.Union[MetaOapg.properties.recipient_view_url, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoicer_view_url"]) -> typing.Union[MetaOapg.properties.invoicer_view_url, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cancel_time", "cancelled_by", "first_sent_time", "last_sent_time", "last_sent_by", "created_by_flow", "recipient_view_url", "invoicer_view_url", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                cancel_time: typing.Union['DateTime', schemas.Unset] = schemas.unset,
                cancelled_by: typing.Union[MetaOapg.properties.cancelled_by, str, schemas.Unset] = schemas.unset,
                first_sent_time: typing.Union['DateTime', schemas.Unset] = schemas.unset,
                last_sent_time: typing.Union['DateTime', schemas.Unset] = schemas.unset,
                last_sent_by: typing.Union[MetaOapg.properties.last_sent_by, str, schemas.Unset] = schemas.unset,
                created_by_flow: typing.Union['InvoiceCreationFlow', schemas.Unset] = schemas.unset,
                recipient_view_url: typing.Union[MetaOapg.properties.recipient_view_url, str, schemas.Unset] = schemas.unset,
                invoicer_view_url: typing.Union[MetaOapg.properties.invoicer_view_url, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    cancel_time=cancel_time,
                    cancelled_by=cancelled_by,
                    first_sent_time=first_sent_time,
                    last_sent_time=last_sent_time,
                    last_sent_by=last_sent_by,
                    created_by_flow=created_by_flow,
                    recipient_view_url=recipient_view_url,
                    invoicer_view_url=invoicer_view_url,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                TemplateMetadata,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Metadata':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_invoicing_python_sdk.model.date_time import DateTime
from pay_pal_invoicing_python_sdk.model.invoice_creation_flow import InvoiceCreationFlow
from pay_pal_invoicing_python_sdk.model.template_metadata import TemplateMetadata

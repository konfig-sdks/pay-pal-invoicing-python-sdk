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


class InvoiceDetail(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The details of the invoice. Includes invoice number, date, payment terms, and audit metadata.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                    
                    
                    class invoice_number(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 127
                
                    @staticmethod
                    def invoice_date() -> typing.Type['DateNoTime']:
                        return DateNoTime
                
                    @staticmethod
                    def payment_term() -> typing.Type['InvoicePaymentTerm']:
                        return InvoicePaymentTerm
                
                    @staticmethod
                    def metadata() -> typing.Type['Metadata']:
                        return Metadata
                    __annotations__ = {
                        "invoice_number": invoice_number,
                        "invoice_date": invoice_date,
                        "payment_term": payment_term,
                        "metadata": metadata,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoice_number"]) -> MetaOapg.properties.invoice_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoice_date"]) -> 'DateNoTime': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["payment_term"]) -> 'InvoicePaymentTerm': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'Metadata': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["invoice_number", "invoice_date", "payment_term", "metadata", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoice_number"]) -> typing.Union[MetaOapg.properties.invoice_number, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoice_date"]) -> typing.Union['DateNoTime', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["payment_term"]) -> typing.Union['InvoicePaymentTerm', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['Metadata', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["invoice_number", "invoice_date", "payment_term", "metadata", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                invoice_number: typing.Union[MetaOapg.properties.invoice_number, str, schemas.Unset] = schemas.unset,
                invoice_date: typing.Union['DateNoTime', schemas.Unset] = schemas.unset,
                payment_term: typing.Union['InvoicePaymentTerm', schemas.Unset] = schemas.unset,
                metadata: typing.Union['Metadata', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    invoice_number=invoice_number,
                    invoice_date=invoice_date,
                    payment_term=payment_term,
                    metadata=metadata,
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
                Detail,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InvoiceDetail':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_invoicing_python_sdk.model.date_no_time import DateNoTime
from pay_pal_invoicing_python_sdk.model.detail import Detail
from pay_pal_invoicing_python_sdk.model.invoice_payment_term import InvoicePaymentTerm
from pay_pal_invoicing_python_sdk.model.metadata import Metadata

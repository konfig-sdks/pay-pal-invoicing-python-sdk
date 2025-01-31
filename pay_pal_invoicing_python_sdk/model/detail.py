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


class Detail(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The details of the invoice like notes, terms and conditions, memo, attachments.
    """


    class MetaOapg:
        required = {
            "currency_code",
        }
        
        class properties:
        
            @staticmethod
            def currency_code() -> typing.Type['CurrencyCode']:
                return CurrencyCode
            
            
            class reference(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 120
            
            
            class note(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 4000
            
            
            class terms_and_conditions(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 4000
            
            
            class memo(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 500
            
            
            class attachments(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FileReference']:
                        return FileReference
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FileReference'], typing.List['FileReference']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attachments':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FileReference':
                    return super().__getitem__(i)
            __annotations__ = {
                "currency_code": currency_code,
                "reference": reference,
                "note": note,
                "terms_and_conditions": terms_and_conditions,
                "memo": memo,
                "attachments": attachments,
            }

    
    currency_code: 'CurrencyCode'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_code"]) -> 'CurrencyCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terms_and_conditions"]) -> MetaOapg.properties.terms_and_conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memo"]) -> MetaOapg.properties.memo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attachments"]) -> MetaOapg.properties.attachments: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["currency_code", "reference", "note", "terms_and_conditions", "memo", "attachments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_code"]) -> 'CurrencyCode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> typing.Union[MetaOapg.properties.reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terms_and_conditions"]) -> typing.Union[MetaOapg.properties.terms_and_conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memo"]) -> typing.Union[MetaOapg.properties.memo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attachments"]) -> typing.Union[MetaOapg.properties.attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currency_code", "reference", "note", "terms_and_conditions", "memo", "attachments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        currency_code: 'CurrencyCode',
        reference: typing.Union[MetaOapg.properties.reference, str, schemas.Unset] = schemas.unset,
        note: typing.Union[MetaOapg.properties.note, str, schemas.Unset] = schemas.unset,
        terms_and_conditions: typing.Union[MetaOapg.properties.terms_and_conditions, str, schemas.Unset] = schemas.unset,
        memo: typing.Union[MetaOapg.properties.memo, str, schemas.Unset] = schemas.unset,
        attachments: typing.Union[MetaOapg.properties.attachments, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Detail':
        return super().__new__(
            cls,
            *args,
            currency_code=currency_code,
            reference=reference,
            note=note,
            terms_and_conditions=terms_and_conditions,
            memo=memo,
            attachments=attachments,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_invoicing_python_sdk.model.currency_code import CurrencyCode
from pay_pal_invoicing_python_sdk.model.file_reference import FileReference

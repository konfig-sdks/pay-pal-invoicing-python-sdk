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


class InvoicerInfo(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The invoicer business information that appears on the invoice.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def email_address() -> typing.Type['EmailAddress']:
                        return EmailAddress
                    
                    
                    class phones(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['PhoneDetail']:
                                return PhoneDetail
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['PhoneDetail'], typing.List['PhoneDetail']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'phones':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'PhoneDetail':
                            return super().__getitem__(i)
                    
                    
                    class website(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            format = 'uri'
                            max_length = 2048
                    
                    
                    class tax_id(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 100
                    
                    
                    class additional_notes(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 400
                    
                    
                    class logo_url(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            format = 'uri'
                            max_length = 2000
                    __annotations__ = {
                        "email_address": email_address,
                        "phones": phones,
                        "website": website,
                        "tax_id": tax_id,
                        "additional_notes": additional_notes,
                        "logo_url": logo_url,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["email_address"]) -> 'EmailAddress': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["phones"]) -> MetaOapg.properties.phones: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["website"]) -> MetaOapg.properties.website: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["tax_id"]) -> MetaOapg.properties.tax_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["additional_notes"]) -> MetaOapg.properties.additional_notes: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["logo_url"]) -> MetaOapg.properties.logo_url: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["email_address", "phones", "website", "tax_id", "additional_notes", "logo_url", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["email_address"]) -> typing.Union['EmailAddress', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["phones"]) -> typing.Union[MetaOapg.properties.phones, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["website"]) -> typing.Union[MetaOapg.properties.website, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["tax_id"]) -> typing.Union[MetaOapg.properties.tax_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["additional_notes"]) -> typing.Union[MetaOapg.properties.additional_notes, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["logo_url"]) -> typing.Union[MetaOapg.properties.logo_url, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email_address", "phones", "website", "tax_id", "additional_notes", "logo_url", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                email_address: typing.Union['EmailAddress', schemas.Unset] = schemas.unset,
                phones: typing.Union[MetaOapg.properties.phones, list, tuple, schemas.Unset] = schemas.unset,
                website: typing.Union[MetaOapg.properties.website, str, schemas.Unset] = schemas.unset,
                tax_id: typing.Union[MetaOapg.properties.tax_id, str, schemas.Unset] = schemas.unset,
                additional_notes: typing.Union[MetaOapg.properties.additional_notes, str, schemas.Unset] = schemas.unset,
                logo_url: typing.Union[MetaOapg.properties.logo_url, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    email_address=email_address,
                    phones=phones,
                    website=website,
                    tax_id=tax_id,
                    additional_notes=additional_notes,
                    logo_url=logo_url,
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
                ContactNameAddress,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InvoicerInfo':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_invoicing_python_sdk.model.contact_name_address import ContactNameAddress
from pay_pal_invoicing_python_sdk.model.email_address import EmailAddress
from pay_pal_invoicing_python_sdk.model.phone_detail import PhoneDetail

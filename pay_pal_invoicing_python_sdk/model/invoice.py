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


class Invoice(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The invoice details which includes all information of the invoice like items, billing information.
    """


    class MetaOapg:
        required = {
            "detail",
        }
        
        class properties:
        
            @staticmethod
            def detail() -> typing.Type['InvoiceDetail']:
                return InvoiceDetail
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 30
            
            
            class parent_id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 30
        
            @staticmethod
            def status() -> typing.Type['InvoiceStatus']:
                return InvoiceStatus
        
            @staticmethod
            def invoicer() -> typing.Type['InvoicerInfo']:
                return InvoicerInfo
            
            
            class primary_recipients(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 100
                    
                    @staticmethod
                    def items() -> typing.Type['RecipientInfo']:
                        return RecipientInfo
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['RecipientInfo'], typing.List['RecipientInfo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'primary_recipients':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'RecipientInfo':
                    return super().__getitem__(i)
            
            
            class additional_recipients(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 100
                    
                    @staticmethod
                    def items() -> typing.Type['EmailAddress']:
                        return EmailAddress
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EmailAddress'], typing.List['EmailAddress']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'additional_recipients':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EmailAddress':
                    return super().__getitem__(i)
            
            
            class items(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 100
                    
                    @staticmethod
                    def items() -> typing.Type['Item']:
                        return Item
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Item'], typing.List['Item']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'items':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Item':
                    return super().__getitem__(i)
        
            @staticmethod
            def configuration() -> typing.Type['Configuration']:
                return Configuration
        
            @staticmethod
            def amount() -> typing.Type['AmountSummaryDetail']:
                return AmountSummaryDetail
        
            @staticmethod
            def due_amount() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def gratuity() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def payments() -> typing.Type['Payments']:
                return Payments
        
            @staticmethod
            def refunds() -> typing.Type['Refunds']:
                return Refunds
            
            
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
                "detail": detail,
                "id": id,
                "parent_id": parent_id,
                "status": status,
                "invoicer": invoicer,
                "primary_recipients": primary_recipients,
                "additional_recipients": additional_recipients,
                "items": items,
                "configuration": configuration,
                "amount": amount,
                "due_amount": due_amount,
                "gratuity": gratuity,
                "payments": payments,
                "refunds": refunds,
                "links": links,
            }
    
    detail: 'InvoiceDetail'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["detail"]) -> 'InvoiceDetail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_id"]) -> MetaOapg.properties.parent_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'InvoiceStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoicer"]) -> 'InvoicerInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_recipients"]) -> MetaOapg.properties.primary_recipients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additional_recipients"]) -> MetaOapg.properties.additional_recipients: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> 'Configuration': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> 'AmountSummaryDetail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due_amount"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gratuity"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payments"]) -> 'Payments': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refunds"]) -> 'Refunds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["detail", "id", "parent_id", "status", "invoicer", "primary_recipients", "additional_recipients", "items", "configuration", "amount", "due_amount", "gratuity", "payments", "refunds", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["detail"]) -> 'InvoiceDetail': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_id"]) -> typing.Union[MetaOapg.properties.parent_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['InvoiceStatus', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoicer"]) -> typing.Union['InvoicerInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_recipients"]) -> typing.Union[MetaOapg.properties.primary_recipients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additional_recipients"]) -> typing.Union[MetaOapg.properties.additional_recipients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> typing.Union[MetaOapg.properties.items, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union['Configuration', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union['AmountSummaryDetail', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due_amount"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gratuity"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payments"]) -> typing.Union['Payments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refunds"]) -> typing.Union['Refunds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["detail", "id", "parent_id", "status", "invoicer", "primary_recipients", "additional_recipients", "items", "configuration", "amount", "due_amount", "gratuity", "payments", "refunds", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        detail: 'InvoiceDetail',
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        parent_id: typing.Union[MetaOapg.properties.parent_id, str, schemas.Unset] = schemas.unset,
        status: typing.Union['InvoiceStatus', schemas.Unset] = schemas.unset,
        invoicer: typing.Union['InvoicerInfo', schemas.Unset] = schemas.unset,
        primary_recipients: typing.Union[MetaOapg.properties.primary_recipients, list, tuple, schemas.Unset] = schemas.unset,
        additional_recipients: typing.Union[MetaOapg.properties.additional_recipients, list, tuple, schemas.Unset] = schemas.unset,
        items: typing.Union[MetaOapg.properties.items, list, tuple, schemas.Unset] = schemas.unset,
        configuration: typing.Union['Configuration', schemas.Unset] = schemas.unset,
        amount: typing.Union['AmountSummaryDetail', schemas.Unset] = schemas.unset,
        due_amount: typing.Union['Money', schemas.Unset] = schemas.unset,
        gratuity: typing.Union['Money', schemas.Unset] = schemas.unset,
        payments: typing.Union['Payments', schemas.Unset] = schemas.unset,
        refunds: typing.Union['Refunds', schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Invoice':
        return super().__new__(
            cls,
            *args,
            detail=detail,
            id=id,
            parent_id=parent_id,
            status=status,
            invoicer=invoicer,
            primary_recipients=primary_recipients,
            additional_recipients=additional_recipients,
            items=items,
            configuration=configuration,
            amount=amount,
            due_amount=due_amount,
            gratuity=gratuity,
            payments=payments,
            refunds=refunds,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_invoicing_python_sdk.model.amount_summary_detail import AmountSummaryDetail
from pay_pal_invoicing_python_sdk.model.configuration import Configuration
from pay_pal_invoicing_python_sdk.model.email_address import EmailAddress
from pay_pal_invoicing_python_sdk.model.invoice_detail import InvoiceDetail
from pay_pal_invoicing_python_sdk.model.invoice_status import InvoiceStatus
from pay_pal_invoicing_python_sdk.model.invoicer_info import InvoicerInfo
from pay_pal_invoicing_python_sdk.model.item import Item
from pay_pal_invoicing_python_sdk.model.link_description import LinkDescription
from pay_pal_invoicing_python_sdk.model.money import Money
from pay_pal_invoicing_python_sdk.model.payments import Payments
from pay_pal_invoicing_python_sdk.model.recipient_info import RecipientInfo
from pay_pal_invoicing_python_sdk.model.refunds import Refunds

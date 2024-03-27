# coding: utf-8

"""
    Invoices

    Use the Invoicing API to create, send, and manage invoices. You can also use the API or webhooks to track invoice payments. When you send an invoice to a customer, the invoice moves from draft to payable state. PayPal then emails the customer a link to the invoice on the PayPal website. Customers with a PayPal account can log in and pay the invoice with PayPal. Alternatively, customers can pay as a guest with a debit card or credit card. For more information, see the <a href=\"/docs/invoicing/\">Invoicing Overview</a> and the <a href=\"/docs/invoicing/basic-integration/\">Invoicing Integration Guide</a>.

    The version of the OpenAPI document: 2.3
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from pay_pal_invoicing_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from pay_pal_invoicing_python_sdk.api_response import AsyncGeneratorResponse
from pay_pal_invoicing_python_sdk import api_client, exceptions
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

from pay_pal_invoicing_python_sdk.model.invoices_cancel_sent_invoice422_response import InvoicesCancelSentInvoice422Response as InvoicesCancelSentInvoice422ResponseSchema
from pay_pal_invoicing_python_sdk.model.error404 import Error404 as Error404Schema
from pay_pal_invoicing_python_sdk.model.invoices_cancel_sent_invoice403_response import InvoicesCancelSentInvoice403Response as InvoicesCancelSentInvoice403ResponseSchema
from pay_pal_invoicing_python_sdk.model.error_default import ErrorDefault as ErrorDefaultSchema
from pay_pal_invoicing_python_sdk.model.invoices_cancel_sent_invoice_response import InvoicesCancelSentInvoiceResponse as InvoicesCancelSentInvoiceResponseSchema
from pay_pal_invoicing_python_sdk.model.notification import Notification as NotificationSchema

from pay_pal_invoicing_python_sdk.type.invoices_cancel_sent_invoice422_response import InvoicesCancelSentInvoice422Response
from pay_pal_invoicing_python_sdk.type.error404 import Error404
from pay_pal_invoicing_python_sdk.type.error_default import ErrorDefault
from pay_pal_invoicing_python_sdk.type.notification import Notification
from pay_pal_invoicing_python_sdk.type.invoices_cancel_sent_invoice403_response import InvoicesCancelSentInvoice403Response
from pay_pal_invoicing_python_sdk.type.invoices_cancel_sent_invoice_response import InvoicesCancelSentInvoiceResponse

from ...api_client import Dictionary
from pay_pal_invoicing_python_sdk.pydantic.error404 import Error404 as Error404Pydantic
from pay_pal_invoicing_python_sdk.pydantic.error_default import ErrorDefault as ErrorDefaultPydantic
from pay_pal_invoicing_python_sdk.pydantic.notification import Notification as NotificationPydantic
from pay_pal_invoicing_python_sdk.pydantic.invoices_cancel_sent_invoice403_response import InvoicesCancelSentInvoice403Response as InvoicesCancelSentInvoice403ResponsePydantic
from pay_pal_invoicing_python_sdk.pydantic.invoices_cancel_sent_invoice_response import InvoicesCancelSentInvoiceResponse as InvoicesCancelSentInvoiceResponsePydantic
from pay_pal_invoicing_python_sdk.pydantic.invoices_cancel_sent_invoice422_response import InvoicesCancelSentInvoice422Response as InvoicesCancelSentInvoice422ResponsePydantic

# Path params
InvoiceIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'invoice_id': typing.Union[InvoiceIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_invoice_id = api_client.PathParameter(
    name="invoice_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=InvoiceIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = NotificationSchema


request_body_notification = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
)
SchemaFor400ResponseBodyApplicationJson = InvoicesCancelSentInvoiceResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: InvoicesCancelSentInvoiceResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: InvoicesCancelSentInvoiceResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = InvoicesCancelSentInvoice403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: InvoicesCancelSentInvoice403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: InvoicesCancelSentInvoice403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = Error404Schema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: Error404


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: Error404


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = InvoicesCancelSentInvoice422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: InvoicesCancelSentInvoice422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: InvoicesCancelSentInvoice422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = ErrorDefaultSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: ErrorDefault


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: ErrorDefault


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _cancel_sent_invoice_mapped_args(
        self,
        invoice_id: str,
        subject: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        send_to_invoicer: typing.Optional[bool] = None,
        send_to_recipient: typing.Optional[bool] = None,
        additional_recipients: typing.Optional[typing.List[EmailAddress]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if subject is not None:
            _body["subject"] = subject
        if note is not None:
            _body["note"] = note
        if send_to_invoicer is not None:
            _body["send_to_invoicer"] = send_to_invoicer
        if send_to_recipient is not None:
            _body["send_to_recipient"] = send_to_recipient
        if additional_recipients is not None:
            _body["additional_recipients"] = additional_recipients
        args.body = _body
        if invoice_id is not None:
            _path_params["invoice_id"] = invoice_id
        args.path = _path_params
        return args

    async def _acancel_sent_invoice_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Cancel sent invoice
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_invoice_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/invoicing/invoices/{invoice_id}/cancel',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_notification.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _cancel_sent_invoice_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Cancel sent invoice
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_invoice_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/invoicing/invoices/{invoice_id}/cancel',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_notification.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CancelSentInvoiceRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acancel_sent_invoice(
        self,
        invoice_id: str,
        subject: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        send_to_invoicer: typing.Optional[bool] = None,
        send_to_recipient: typing.Optional[bool] = None,
        additional_recipients: typing.Optional[typing.List[EmailAddress]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._cancel_sent_invoice_mapped_args(
            invoice_id=invoice_id,
            subject=subject,
            note=note,
            send_to_invoicer=send_to_invoicer,
            send_to_recipient=send_to_recipient,
            additional_recipients=additional_recipients,
        )
        return await self._acancel_sent_invoice_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def cancel_sent_invoice(
        self,
        invoice_id: str,
        subject: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        send_to_invoicer: typing.Optional[bool] = None,
        send_to_recipient: typing.Optional[bool] = None,
        additional_recipients: typing.Optional[typing.List[EmailAddress]] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._cancel_sent_invoice_mapped_args(
            invoice_id=invoice_id,
            subject=subject,
            note=note,
            send_to_invoicer=send_to_invoicer,
            send_to_recipient=send_to_recipient,
            additional_recipients=additional_recipients,
        )
        return self._cancel_sent_invoice_oapg(
            body=args.body,
            path_params=args.path,
        )

class CancelSentInvoice(BaseApi):

    async def acancel_sent_invoice(
        self,
        invoice_id: str,
        subject: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        send_to_invoicer: typing.Optional[bool] = None,
        send_to_recipient: typing.Optional[bool] = None,
        additional_recipients: typing.Optional[typing.List[EmailAddress]] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.acancel_sent_invoice(
            invoice_id=invoice_id,
            subject=subject,
            note=note,
            send_to_invoicer=send_to_invoicer,
            send_to_recipient=send_to_recipient,
            additional_recipients=additional_recipients,
            **kwargs,
        )
    
    
    def cancel_sent_invoice(
        self,
        invoice_id: str,
        subject: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        send_to_invoicer: typing.Optional[bool] = None,
        send_to_recipient: typing.Optional[bool] = None,
        additional_recipients: typing.Optional[typing.List[EmailAddress]] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.cancel_sent_invoice(
            invoice_id=invoice_id,
            subject=subject,
            note=note,
            send_to_invoicer=send_to_invoicer,
            send_to_recipient=send_to_recipient,
            additional_recipients=additional_recipients,
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        invoice_id: str,
        subject: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        send_to_invoicer: typing.Optional[bool] = None,
        send_to_recipient: typing.Optional[bool] = None,
        additional_recipients: typing.Optional[typing.List[EmailAddress]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._cancel_sent_invoice_mapped_args(
            invoice_id=invoice_id,
            subject=subject,
            note=note,
            send_to_invoicer=send_to_invoicer,
            send_to_recipient=send_to_recipient,
            additional_recipients=additional_recipients,
        )
        return await self._acancel_sent_invoice_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        invoice_id: str,
        subject: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        send_to_invoicer: typing.Optional[bool] = None,
        send_to_recipient: typing.Optional[bool] = None,
        additional_recipients: typing.Optional[typing.List[EmailAddress]] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._cancel_sent_invoice_mapped_args(
            invoice_id=invoice_id,
            subject=subject,
            note=note,
            send_to_invoicer=send_to_invoicer,
            send_to_recipient=send_to_recipient,
            additional_recipients=additional_recipients,
        )
        return self._cancel_sent_invoice_oapg(
            body=args.body,
            path_params=args.path,
        )


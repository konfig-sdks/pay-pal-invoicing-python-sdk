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

from pay_pal_invoicing_python_sdk.model.error422 import Error422 as Error422Schema
from pay_pal_invoicing_python_sdk.model.error404 import Error404 as Error404Schema
from pay_pal_invoicing_python_sdk.model.invoices_get_details_response import InvoicesGetDetailsResponse as InvoicesGetDetailsResponseSchema
from pay_pal_invoicing_python_sdk.model.error_default import ErrorDefault as ErrorDefaultSchema
from pay_pal_invoicing_python_sdk.model.error400 import Error400 as Error400Schema
from pay_pal_invoicing_python_sdk.model.invoice import Invoice as InvoiceSchema

from pay_pal_invoicing_python_sdk.type.error404 import Error404
from pay_pal_invoicing_python_sdk.type.error400 import Error400
from pay_pal_invoicing_python_sdk.type.error_default import ErrorDefault
from pay_pal_invoicing_python_sdk.type.error422 import Error422
from pay_pal_invoicing_python_sdk.type.invoices_get_details_response import InvoicesGetDetailsResponse
from pay_pal_invoicing_python_sdk.type.invoice import Invoice

from ...api_client import Dictionary
from pay_pal_invoicing_python_sdk.pydantic.error404 import Error404 as Error404Pydantic
from pay_pal_invoicing_python_sdk.pydantic.error_default import ErrorDefault as ErrorDefaultPydantic
from pay_pal_invoicing_python_sdk.pydantic.invoice import Invoice as InvoicePydantic
from pay_pal_invoicing_python_sdk.pydantic.error400 import Error400 as Error400Pydantic
from pay_pal_invoicing_python_sdk.pydantic.error422 import Error422 as Error422Pydantic
from pay_pal_invoicing_python_sdk.pydantic.invoices_get_details_response import InvoicesGetDetailsResponse as InvoicesGetDetailsResponsePydantic

from . import path

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
_auth = [
    'Oauth2',
]
SchemaFor200ResponseBodyApplicationJson = InvoiceSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Invoice


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Invoice


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = Error400Schema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: Error400


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: Error400


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = InvoicesGetDetailsResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: InvoicesGetDetailsResponse


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: InvoicesGetDetailsResponse


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
SchemaFor422ResponseBodyApplicationJson = Error422Schema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: Error422


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: Error422


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '403': _response_for_403,
    '404': _response_for_404,
    '422': _response_for_422,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_details_mapped_args(
        self,
        invoice_id: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if invoice_id is not None:
            _path_params["invoice_id"] = invoice_id
        args.path = _path_params
        return args

    async def _aget_details_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Show invoice details
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/invoicing/invoices/{invoice_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_details_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Show invoice details
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/invoicing/invoices/{invoice_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetDetailsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_details(
        self,
        invoice_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_details_mapped_args(
            invoice_id=invoice_id,
        )
        return await self._aget_details_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_details(
        self,
        invoice_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_details_mapped_args(
            invoice_id=invoice_id,
        )
        return self._get_details_oapg(
            path_params=args.path,
        )

class GetDetails(BaseApi):

    async def aget_details(
        self,
        invoice_id: str,
        validate: bool = False,
        **kwargs,
    ) -> InvoicePydantic:
        raw_response = await self.raw.aget_details(
            invoice_id=invoice_id,
            **kwargs,
        )
        if validate:
            return InvoicePydantic(**raw_response.body)
        return api_client.construct_model_instance(InvoicePydantic, raw_response.body)
    
    
    def get_details(
        self,
        invoice_id: str,
        validate: bool = False,
    ) -> InvoicePydantic:
        raw_response = self.raw.get_details(
            invoice_id=invoice_id,
        )
        if validate:
            return InvoicePydantic(**raw_response.body)
        return api_client.construct_model_instance(InvoicePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        invoice_id: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_details_mapped_args(
            invoice_id=invoice_id,
        )
        return await self._aget_details_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        invoice_id: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_details_mapped_args(
            invoice_id=invoice_id,
        )
        return self._get_details_oapg(
            path_params=args.path,
        )


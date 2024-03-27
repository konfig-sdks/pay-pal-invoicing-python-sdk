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

from pay_pal_invoicing_python_sdk.model.templates_create_template422_response import TemplatesCreateTemplate422Response as TemplatesCreateTemplate422ResponseSchema
from pay_pal_invoicing_python_sdk.model.templates_create_template_response import TemplatesCreateTemplateResponse as TemplatesCreateTemplateResponseSchema
from pay_pal_invoicing_python_sdk.model.error_default import ErrorDefault as ErrorDefaultSchema
from pay_pal_invoicing_python_sdk.model.unit_of_measure import UnitOfMeasure as UnitOfMeasureSchema
from pay_pal_invoicing_python_sdk.model.templates_create_template400_response import TemplatesCreateTemplate400Response as TemplatesCreateTemplate400ResponseSchema
from pay_pal_invoicing_python_sdk.model.template import Template as TemplateSchema
from pay_pal_invoicing_python_sdk.model.link_description import LinkDescription as LinkDescriptionSchema
from pay_pal_invoicing_python_sdk.model.template_settings import TemplateSettings as TemplateSettingsSchema
from pay_pal_invoicing_python_sdk.model.template_info import TemplateInfo as TemplateInfoSchema

from pay_pal_invoicing_python_sdk.type.template_info import TemplateInfo
from pay_pal_invoicing_python_sdk.type.template_settings import TemplateSettings
from pay_pal_invoicing_python_sdk.type.error_default import ErrorDefault
from pay_pal_invoicing_python_sdk.type.unit_of_measure import UnitOfMeasure
from pay_pal_invoicing_python_sdk.type.templates_create_template400_response import TemplatesCreateTemplate400Response
from pay_pal_invoicing_python_sdk.type.templates_create_template422_response import TemplatesCreateTemplate422Response
from pay_pal_invoicing_python_sdk.type.templates_create_template_response import TemplatesCreateTemplateResponse
from pay_pal_invoicing_python_sdk.type.link_description import LinkDescription
from pay_pal_invoicing_python_sdk.type.template import Template

from ...api_client import Dictionary
from pay_pal_invoicing_python_sdk.pydantic.template_info import TemplateInfo as TemplateInfoPydantic
from pay_pal_invoicing_python_sdk.pydantic.error_default import ErrorDefault as ErrorDefaultPydantic
from pay_pal_invoicing_python_sdk.pydantic.unit_of_measure import UnitOfMeasure as UnitOfMeasurePydantic
from pay_pal_invoicing_python_sdk.pydantic.template import Template as TemplatePydantic
from pay_pal_invoicing_python_sdk.pydantic.template_settings import TemplateSettings as TemplateSettingsPydantic
from pay_pal_invoicing_python_sdk.pydantic.link_description import LinkDescription as LinkDescriptionPydantic
from pay_pal_invoicing_python_sdk.pydantic.templates_create_template400_response import TemplatesCreateTemplate400Response as TemplatesCreateTemplate400ResponsePydantic
from pay_pal_invoicing_python_sdk.pydantic.templates_create_template422_response import TemplatesCreateTemplate422Response as TemplatesCreateTemplate422ResponsePydantic
from pay_pal_invoicing_python_sdk.pydantic.templates_create_template_response import TemplatesCreateTemplateResponse as TemplatesCreateTemplateResponsePydantic

# body param
SchemaForRequestBodyApplicationJson = TemplateSchema


request_body_template = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = TemplateSchema
SchemaFor201ResponseBodyMultipartMixed = TemplateSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Template


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Template


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
        'multipart/mixed': api_client.MediaType(
            schema=SchemaFor201ResponseBodyMultipartMixed),
    },
)
SchemaFor400ResponseBodyApplicationJson = TemplatesCreateTemplateResponseSchema
SchemaFor400ResponseBodyMultipartMixed = TemplatesCreateTemplate400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: TemplatesCreateTemplateResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: TemplatesCreateTemplateResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
        'multipart/mixed': api_client.MediaType(
            schema=SchemaFor400ResponseBodyMultipartMixed),
    },
)
SchemaFor422ResponseBodyApplicationJson = TemplatesCreateTemplate422ResponseSchema
SchemaFor422ResponseBodyMultipartMixed = TemplatesCreateTemplate422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: TemplatesCreateTemplate422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: TemplatesCreateTemplate422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
        'multipart/mixed': api_client.MediaType(
            schema=SchemaFor422ResponseBodyMultipartMixed),
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
    'multipart/mixed',
)


class BaseApi(api_client.Api):

    def _create_template_mapped_args(
        self,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        default_template: typing.Optional[bool] = None,
        template_info: typing.Optional[TemplateInfo] = None,
        settings: typing.Optional[TemplateSettings] = None,
        unit_of_measure: typing.Optional[UnitOfMeasure] = None,
        standard_template: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[LinkDescription]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if id is not None:
            _body["id"] = id
        if name is not None:
            _body["name"] = name
        if default_template is not None:
            _body["default_template"] = default_template
        if template_info is not None:
            _body["template_info"] = template_info
        if settings is not None:
            _body["settings"] = settings
        if unit_of_measure is not None:
            _body["unit_of_measure"] = unit_of_measure
        if standard_template is not None:
            _body["standard_template"] = standard_template
        if links is not None:
            _body["links"] = links
        args.body = _body
        return args

    async def _acreate_template_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create template
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/v2/invoicing/templates',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_template.serialize(body, content_type)
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


    def _create_template_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create template
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/v2/invoicing/templates',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_template.serialize(body, content_type)
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


class CreateTemplateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_template(
        self,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        default_template: typing.Optional[bool] = None,
        template_info: typing.Optional[TemplateInfo] = None,
        settings: typing.Optional[TemplateSettings] = None,
        unit_of_measure: typing.Optional[UnitOfMeasure] = None,
        standard_template: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[LinkDescription]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_template_mapped_args(
            id=id,
            name=name,
            default_template=default_template,
            template_info=template_info,
            settings=settings,
            unit_of_measure=unit_of_measure,
            standard_template=standard_template,
            links=links,
        )
        return await self._acreate_template_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_template(
        self,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        default_template: typing.Optional[bool] = None,
        template_info: typing.Optional[TemplateInfo] = None,
        settings: typing.Optional[TemplateSettings] = None,
        unit_of_measure: typing.Optional[UnitOfMeasure] = None,
        standard_template: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[LinkDescription]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_template_mapped_args(
            id=id,
            name=name,
            default_template=default_template,
            template_info=template_info,
            settings=settings,
            unit_of_measure=unit_of_measure,
            standard_template=standard_template,
            links=links,
        )
        return self._create_template_oapg(
            body=args.body,
        )

class CreateTemplate(BaseApi):

    async def acreate_template(
        self,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        default_template: typing.Optional[bool] = None,
        template_info: typing.Optional[TemplateInfo] = None,
        settings: typing.Optional[TemplateSettings] = None,
        unit_of_measure: typing.Optional[UnitOfMeasure] = None,
        standard_template: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[LinkDescription]] = None,
        validate: bool = False,
        **kwargs,
    ) -> TemplatePydantic:
        raw_response = await self.raw.acreate_template(
            id=id,
            name=name,
            default_template=default_template,
            template_info=template_info,
            settings=settings,
            unit_of_measure=unit_of_measure,
            standard_template=standard_template,
            links=links,
            **kwargs,
        )
        if validate:
            return TemplatePydantic(**raw_response.body)
        return api_client.construct_model_instance(TemplatePydantic, raw_response.body)
    
    
    def create_template(
        self,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        default_template: typing.Optional[bool] = None,
        template_info: typing.Optional[TemplateInfo] = None,
        settings: typing.Optional[TemplateSettings] = None,
        unit_of_measure: typing.Optional[UnitOfMeasure] = None,
        standard_template: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[LinkDescription]] = None,
        validate: bool = False,
    ) -> TemplatePydantic:
        raw_response = self.raw.create_template(
            id=id,
            name=name,
            default_template=default_template,
            template_info=template_info,
            settings=settings,
            unit_of_measure=unit_of_measure,
            standard_template=standard_template,
            links=links,
        )
        if validate:
            return TemplatePydantic(**raw_response.body)
        return api_client.construct_model_instance(TemplatePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        default_template: typing.Optional[bool] = None,
        template_info: typing.Optional[TemplateInfo] = None,
        settings: typing.Optional[TemplateSettings] = None,
        unit_of_measure: typing.Optional[UnitOfMeasure] = None,
        standard_template: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[LinkDescription]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_template_mapped_args(
            id=id,
            name=name,
            default_template=default_template,
            template_info=template_info,
            settings=settings,
            unit_of_measure=unit_of_measure,
            standard_template=standard_template,
            links=links,
        )
        return await self._acreate_template_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        default_template: typing.Optional[bool] = None,
        template_info: typing.Optional[TemplateInfo] = None,
        settings: typing.Optional[TemplateSettings] = None,
        unit_of_measure: typing.Optional[UnitOfMeasure] = None,
        standard_template: typing.Optional[bool] = None,
        links: typing.Optional[typing.List[LinkDescription]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_template_mapped_args(
            id=id,
            name=name,
            default_template=default_template,
            template_info=template_info,
            settings=settings,
            unit_of_measure=unit_of_measure,
            standard_template=standard_template,
            links=links,
        )
        return self._create_template_oapg(
            body=args.body,
        )


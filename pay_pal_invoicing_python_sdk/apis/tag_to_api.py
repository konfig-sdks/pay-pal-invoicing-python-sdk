import typing_extensions

from pay_pal_invoicing_python_sdk.apis.tags import TagValues
from pay_pal_invoicing_python_sdk.apis.tags.invoices_api import InvoicesApi
from pay_pal_invoicing_python_sdk.apis.tags.templates_api import TemplatesApi
from pay_pal_invoicing_python_sdk.apis.tags.search_invoices_api import SearchInvoicesApi
from pay_pal_invoicing_python_sdk.apis.tags.merchant_config_api import MerchantConfigApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.INVOICES: InvoicesApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.SEARCHINVOICES: SearchInvoicesApi,
        TagValues.MERCHANTCONFIG: MerchantConfigApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.INVOICES: InvoicesApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.SEARCHINVOICES: SearchInvoicesApi,
        TagValues.MERCHANTCONFIG: MerchantConfigApi,
    }
)

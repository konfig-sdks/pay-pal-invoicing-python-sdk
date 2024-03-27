# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pay_pal_invoicing_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V2_INVOICING_INVOICES = "/v2/invoicing/invoices"
    V2_INVOICING_INVOICES_INVOICE_ID_SEND = "/v2/invoicing/invoices/{invoice_id}/send"
    V2_INVOICING_INVOICES_INVOICE_ID_REMIND = "/v2/invoicing/invoices/{invoice_id}/remind"
    V2_INVOICING_INVOICES_INVOICE_ID_CANCEL = "/v2/invoicing/invoices/{invoice_id}/cancel"
    V2_INVOICING_INVOICES_INVOICE_ID_PAYMENTS = "/v2/invoicing/invoices/{invoice_id}/payments"
    V2_INVOICING_INVOICES_INVOICE_ID_PAYMENTS_TRANSACTION_ID = "/v2/invoicing/invoices/{invoice_id}/payments/{transaction_id}"
    V2_INVOICING_INVOICES_INVOICE_ID_REFUNDS = "/v2/invoicing/invoices/{invoice_id}/refunds"
    V2_INVOICING_INVOICES_INVOICE_ID_REFUNDS_TRANSACTION_ID = "/v2/invoicing/invoices/{invoice_id}/refunds/{transaction_id}"
    V2_INVOICING_INVOICES_INVOICE_ID_GENERATEQRCODE = "/v2/invoicing/invoices/{invoice_id}/generate-qr-code"
    V2_INVOICING_GENERATENEXTINVOICENUMBER = "/v2/invoicing/generate-next-invoice-number"
    V2_INVOICING_INVOICES_INVOICE_ID = "/v2/invoicing/invoices/{invoice_id}"
    V2_INVOICING_SEARCHINVOICES = "/v2/invoicing/search-invoices"
    V2_INVOICING_TEMPLATES = "/v2/invoicing/templates"
    V2_INVOICING_TEMPLATES_TEMPLATE_ID = "/v2/invoicing/templates/{template_id}"

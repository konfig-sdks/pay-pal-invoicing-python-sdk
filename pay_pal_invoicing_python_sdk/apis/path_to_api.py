import typing_extensions

from pay_pal_invoicing_python_sdk.paths import PathValues
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_invoices import V2InvoicingInvoices
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_invoices_invoice_id_send import V2InvoicingInvoicesInvoiceIdSend
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_invoices_invoice_id_remind import V2InvoicingInvoicesInvoiceIdRemind
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_invoices_invoice_id_cancel import V2InvoicingInvoicesInvoiceIdCancel
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_invoices_invoice_id_payments import V2InvoicingInvoicesInvoiceIdPayments
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_invoices_invoice_id_payments_transaction_id import V2InvoicingInvoicesInvoiceIdPaymentsTransactionId
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_invoices_invoice_id_refunds import V2InvoicingInvoicesInvoiceIdRefunds
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_invoices_invoice_id_refunds_transaction_id import V2InvoicingInvoicesInvoiceIdRefundsTransactionId
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_invoices_invoice_id_generate_qr_code import V2InvoicingInvoicesInvoiceIdGenerateQrCode
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_generate_next_invoice_number import V2InvoicingGenerateNextInvoiceNumber
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_invoices_invoice_id import V2InvoicingInvoicesInvoiceId
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_search_invoices import V2InvoicingSearchInvoices
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_templates import V2InvoicingTemplates
from pay_pal_invoicing_python_sdk.apis.paths.v2_invoicing_templates_template_id import V2InvoicingTemplatesTemplateId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V2_INVOICING_INVOICES: V2InvoicingInvoices,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_SEND: V2InvoicingInvoicesInvoiceIdSend,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_REMIND: V2InvoicingInvoicesInvoiceIdRemind,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_CANCEL: V2InvoicingInvoicesInvoiceIdCancel,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_PAYMENTS: V2InvoicingInvoicesInvoiceIdPayments,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_PAYMENTS_TRANSACTION_ID: V2InvoicingInvoicesInvoiceIdPaymentsTransactionId,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_REFUNDS: V2InvoicingInvoicesInvoiceIdRefunds,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_REFUNDS_TRANSACTION_ID: V2InvoicingInvoicesInvoiceIdRefundsTransactionId,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_GENERATEQRCODE: V2InvoicingInvoicesInvoiceIdGenerateQrCode,
        PathValues.V2_INVOICING_GENERATENEXTINVOICENUMBER: V2InvoicingGenerateNextInvoiceNumber,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID: V2InvoicingInvoicesInvoiceId,
        PathValues.V2_INVOICING_SEARCHINVOICES: V2InvoicingSearchInvoices,
        PathValues.V2_INVOICING_TEMPLATES: V2InvoicingTemplates,
        PathValues.V2_INVOICING_TEMPLATES_TEMPLATE_ID: V2InvoicingTemplatesTemplateId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V2_INVOICING_INVOICES: V2InvoicingInvoices,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_SEND: V2InvoicingInvoicesInvoiceIdSend,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_REMIND: V2InvoicingInvoicesInvoiceIdRemind,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_CANCEL: V2InvoicingInvoicesInvoiceIdCancel,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_PAYMENTS: V2InvoicingInvoicesInvoiceIdPayments,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_PAYMENTS_TRANSACTION_ID: V2InvoicingInvoicesInvoiceIdPaymentsTransactionId,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_REFUNDS: V2InvoicingInvoicesInvoiceIdRefunds,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_REFUNDS_TRANSACTION_ID: V2InvoicingInvoicesInvoiceIdRefundsTransactionId,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID_GENERATEQRCODE: V2InvoicingInvoicesInvoiceIdGenerateQrCode,
        PathValues.V2_INVOICING_GENERATENEXTINVOICENUMBER: V2InvoicingGenerateNextInvoiceNumber,
        PathValues.V2_INVOICING_INVOICES_INVOICE_ID: V2InvoicingInvoicesInvoiceId,
        PathValues.V2_INVOICING_SEARCHINVOICES: V2InvoicingSearchInvoices,
        PathValues.V2_INVOICING_TEMPLATES: V2InvoicingTemplates,
        PathValues.V2_INVOICING_TEMPLATES_TEMPLATE_ID: V2InvoicingTemplatesTemplateId,
    }
)

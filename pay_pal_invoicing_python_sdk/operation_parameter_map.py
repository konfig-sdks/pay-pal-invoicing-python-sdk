operation_parameter_map = {
    '/v2/invoicing/invoices/{invoice_id}/cancel-POST': {
        'parameters': [
            {
                'name': 'invoice_id'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'note'
            },
            {
                'name': 'send_to_invoicer'
            },
            {
                'name': 'send_to_recipient'
            },
            {
                'name': 'additional_recipients'
            },
        ]
    },
    '/v2/invoicing/invoices-POST': {
        'parameters': [
            {
                'name': 'detail'
            },
            {
                'name': 'id'
            },
            {
                'name': 'parent_id'
            },
            {
                'name': 'items'
            },
            {
                'name': 'invoicer'
            },
            {
                'name': 'primary_recipients'
            },
            {
                'name': 'additional_recipients'
            },
            {
                'name': 'items'
            },
            {
                'name': 'configuration'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'due_amount'
            },
            {
                'name': 'gratuity'
            },
            {
                'name': 'payments'
            },
            {
                'name': 'refunds'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/v2/invoicing/invoices/{invoice_id}-DELETE': {
        'parameters': [
            {
                'name': 'invoice_id'
            },
        ]
    },
    '/v2/invoicing/invoices/{invoice_id}/payments/{transaction_id}-DELETE': {
        'parameters': [
            {
                'name': 'invoice_id'
            },
            {
                'name': 'transaction_id'
            },
        ]
    },
    '/v2/invoicing/invoices/{invoice_id}/refunds/{transaction_id}-DELETE': {
        'parameters': [
            {
                'name': 'invoice_id'
            },
            {
                'name': 'transaction_id'
            },
        ]
    },
    '/v2/invoicing/generate-next-invoice-number-POST': {
        'parameters': [
        ]
    },
    '/v2/invoicing/invoices/{invoice_id}/generate-qr-code-POST': {
        'parameters': [
            {
                'name': 'invoice_id'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
            {
                'name': 'action'
            },
        ]
    },
    '/v2/invoicing/invoices/{invoice_id}-GET': {
        'parameters': [
            {
                'name': 'invoice_id'
            },
        ]
    },
    '/v2/invoicing/invoices-GET': {
        'parameters': [
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'total_required'
            },
            {
                'name': 'fields'
            },
        ]
    },
    '/v2/invoicing/invoices/{invoice_id}/payments-POST': {
        'parameters': [
            {
                'name': 'method'
            },
            {
                'name': 'invoice_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'payment_id'
            },
            {
                'name': 'payment_date'
            },
            {
                'name': 'note'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'shipping_info'
            },
        ]
    },
    '/v2/invoicing/invoices/{invoice_id}/refunds-POST': {
        'parameters': [
            {
                'name': 'method'
            },
            {
                'name': 'invoice_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'refund_id'
            },
            {
                'name': 'refund_date'
            },
            {
                'name': 'amount'
            },
        ]
    },
    '/v2/invoicing/invoices/{invoice_id}/send-POST': {
        'parameters': [
            {
                'name': 'invoice_id'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'note'
            },
            {
                'name': 'send_to_invoicer'
            },
            {
                'name': 'send_to_recipient'
            },
            {
                'name': 'additional_recipients'
            },
        ]
    },
    '/v2/invoicing/invoices/{invoice_id}/remind-POST': {
        'parameters': [
            {
                'name': 'invoice_id'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'note'
            },
            {
                'name': 'send_to_invoicer'
            },
            {
                'name': 'send_to_recipient'
            },
            {
                'name': 'additional_recipients'
            },
        ]
    },
    '/v2/invoicing/invoices/{invoice_id}-PUT': {
        'parameters': [
            {
                'name': 'detail'
            },
            {
                'name': 'invoice_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'parent_id'
            },
            {
                'name': 'items'
            },
            {
                'name': 'invoicer'
            },
            {
                'name': 'primary_recipients'
            },
            {
                'name': 'additional_recipients'
            },
            {
                'name': 'items'
            },
            {
                'name': 'configuration'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'due_amount'
            },
            {
                'name': 'gratuity'
            },
            {
                'name': 'payments'
            },
            {
                'name': 'refunds'
            },
            {
                'name': 'links'
            },
            {
                'name': 'send_to_recipient'
            },
            {
                'name': 'send_to_invoicer'
            },
        ]
    },
    '/v2/invoicing/search-invoices-POST': {
        'parameters': [
            {
                'name': 'recipient_email'
            },
            {
                'name': 'recipient_first_name'
            },
            {
                'name': 'recipient_last_name'
            },
            {
                'name': 'recipient_business_name'
            },
            {
                'name': 'invoice_number'
            },
            {
                'name': 'status'
            },
            {
                'name': 'reference'
            },
            {
                'name': 'currency_code'
            },
            {
                'name': 'memo'
            },
            {
                'name': 'total_amount_range'
            },
            {
                'name': 'invoice_date_range'
            },
            {
                'name': 'due_date_range'
            },
            {
                'name': 'payment_date_range'
            },
            {
                'name': 'creation_date_range'
            },
            {
                'name': 'archived'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'total_required'
            },
        ]
    },
    '/v2/invoicing/templates-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'default_template'
            },
            {
                'name': 'template_info'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'unit_of_measure'
            },
            {
                'name': 'standard_template'
            },
            {
                'name': 'links'
            },
        ]
    },
    '/v2/invoicing/templates/{template_id}-DELETE': {
        'parameters': [
            {
                'name': 'template_id'
            },
        ]
    },
    '/v2/invoicing/templates-GET': {
        'parameters': [
            {
                'name': 'fields'
            },
            {
                'name': 'page'
            },
            {
                'name': 'page_size'
            },
        ]
    },
    '/v2/invoicing/templates/{template_id}-GET': {
        'parameters': [
            {
                'name': 'template_id'
            },
        ]
    },
    '/v2/invoicing/templates/{template_id}-PUT': {
        'parameters': [
            {
                'name': 'template_id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'default_template'
            },
            {
                'name': 'template_info'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'unit_of_measure'
            },
            {
                'name': 'standard_template'
            },
            {
                'name': 'links'
            },
        ]
    },
};
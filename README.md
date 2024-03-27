<div align="left">

[![Visit Paypal](./header.png)](https://www.paypal.com&#x2F;)

# Paypal<a id="paypal"></a>

Use the Invoicing API to create, send, and manage invoices. You can also use the API or webhooks to track invoice payments. When you send an invoice to a customer, the invoice moves from draft to payable state. PayPal then emails the customer a link to the invoice on the PayPal website. Customers with a PayPal account can log in and pay the invoice with PayPal. Alternatively, customers can pay as a guest with a debit card or credit card. For more information, see the <a href=\"/docs/invoicing/\">Invoicing Overview</a> and the <a href=\"/docs/invoicing/basic-integration/\">Invoicing Integration Guide</a>.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`paypalinvoicing.invoices.cancel_sent_invoice`](#paypalinvoicinginvoicescancel_sent_invoice)
  * [`paypalinvoicing.invoices.create_draft_invoice`](#paypalinvoicinginvoicescreate_draft_invoice)
  * [`paypalinvoicing.invoices.delete_draft_or_scheduled_invoice`](#paypalinvoicinginvoicesdelete_draft_or_scheduled_invoice)
  * [`paypalinvoicing.invoices.delete_external_payment`](#paypalinvoicinginvoicesdelete_external_payment)
  * [`paypalinvoicing.invoices.delete_external_refund`](#paypalinvoicinginvoicesdelete_external_refund)
  * [`paypalinvoicing.invoices.generate_next_invoice_number`](#paypalinvoicinginvoicesgenerate_next_invoice_number)
  * [`paypalinvoicing.invoices.generate_qr_code`](#paypalinvoicinginvoicesgenerate_qr_code)
  * [`paypalinvoicing.invoices.get_details`](#paypalinvoicinginvoicesget_details)
  * [`paypalinvoicing.invoices.get_invoices`](#paypalinvoicinginvoicesget_invoices)
  * [`paypalinvoicing.invoices.record_payment`](#paypalinvoicinginvoicesrecord_payment)
  * [`paypalinvoicing.invoices.record_refund`](#paypalinvoicinginvoicesrecord_refund)
  * [`paypalinvoicing.invoices.send_invoice`](#paypalinvoicinginvoicessend_invoice)
  * [`paypalinvoicing.invoices.send_reminder`](#paypalinvoicinginvoicessend_reminder)
  * [`paypalinvoicing.invoices.update_full_invoice`](#paypalinvoicinginvoicesupdate_full_invoice)
  * [`paypalinvoicing.search_invoices.list`](#paypalinvoicingsearch_invoiceslist)
  * [`paypalinvoicing.templates.create_template`](#paypalinvoicingtemplatescreate_template)
  * [`paypalinvoicing.templates.delete_by_id`](#paypalinvoicingtemplatesdelete_by_id)
  * [`paypalinvoicing.templates.list_details`](#paypalinvoicingtemplateslist_details)
  * [`paypalinvoicing.templates.show_details_by_id`](#paypalinvoicingtemplatesshow_details_by_id)
  * [`paypalinvoicing.templates.update_full_template`](#paypalinvoicingtemplatesupdate_full_template)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=PayPal&serviceName=Invoicing&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from pay_pal_invoicing_python_sdk import PayPalInvoicing, ApiException

paypalinvoicing = PayPalInvoicing(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Cancel sent invoice
    paypalinvoicing.invoices.cancel_sent_invoice(
        invoice_id="invoice_id_example",
        subject="string_example",
        note="string_example",
        send_to_invoicer=False,
        send_to_recipient=True,
        additional_recipients=[
        "j@Z,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mG"
    ],
    )
except ApiException as e:
    print("Exception when calling InvoicesApi.cancel_sent_invoice: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from pay_pal_invoicing_python_sdk import PayPalInvoicing, ApiException

paypalinvoicing = PayPalInvoicing(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Cancel sent invoice
        await paypalinvoicing.invoices.acancel_sent_invoice(
            invoice_id="invoice_id_example",
            subject="string_example",
            note="string_example",
            send_to_invoicer=False,
            send_to_recipient=True,
            additional_recipients=[
        "j@Z,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mG"
    ],
        )
    except ApiException as e:
        print("Exception when calling InvoicesApi.cancel_sent_invoice: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from pay_pal_invoicing_python_sdk import PayPalInvoicing, ApiException

paypalinvoicing = PayPalInvoicing(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Cancel sent invoice
    cancel_sent_invoice_response = paypalinvoicing.invoices.raw.cancel_sent_invoice(
        invoice_id="invoice_id_example",
        subject="string_example",
        note="string_example",
        send_to_invoicer=False,
        send_to_recipient=True,
        additional_recipients=[
        "j@Z,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mG"
    ],
    )
    pprint(cancel_sent_invoice_response.headers)
    pprint(cancel_sent_invoice_response.status)
    pprint(cancel_sent_invoice_response.round_trip_time)
except ApiException as e:
    print("Exception when calling InvoicesApi.cancel_sent_invoice: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `paypalinvoicing.invoices.cancel_sent_invoice`<a id="paypalinvoicinginvoicescancel_sent_invoice"></a>

Cancels a sent invoice, by ID, and, optionally, sends a notification about the cancellation to the payer, merchant, and CC: emails.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paypalinvoicing.invoices.cancel_sent_invoice(
    invoice_id="invoice_id_example",
    subject="string_example",
    note="string_example",
    send_to_invoicer=False,
    send_to_recipient=True,
    additional_recipients=[
        "j@Z,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mG"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_id: `str`<a id="invoice_id-str"></a>

The ID of the draft invoice to delete.

##### subject: `str`<a id="subject-str"></a>

The subject of the email that is sent as a notification to the recipient.

##### note: `str`<a id="note-str"></a>

A note to the payer.

##### send_to_invoicer: `bool`<a id="send_to_invoicer-bool"></a>

Indicates whether to send a copy of the email to the merchant.

##### send_to_recipient: `bool`<a id="send_to_recipient-bool"></a>

Indicates whether to send a copy of the email to the recipient.

##### additional_recipients: List[`EmailAddress`]<a id="additional_recipients-listemailaddress"></a>

An array of one or more CC: emails to which notifications are sent. If you omit this parameter, a notification is sent to all CC: email addresses that are part of the invoice.<blockquote><strong>Note:</strong> Valid values are email addresses in the `additional_recipients` value associated with the invoice.</blockquote>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Notification`](./pay_pal_invoicing_python_sdk/type/notification.py)
The email or SMS notification that will be sent to the payer on cancellation.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices/{invoice_id}/cancel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.create_draft_invoice`<a id="paypalinvoicinginvoicescreate_draft_invoice"></a>

Creates a draft invoice. To move the invoice from a draft to payable state, you must <a href="#invoices_send">send the invoice</a>.<br/><br/>In the JSON request body, include invoice details including merchant information. The <code>invoice</code> object must include an <code>items</code> array.<blockquote><strong>Note:</strong> The merchant that you specify in an invoice must have a PayPal account in good standing.</blockquote>.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_draft_invoice_response = paypalinvoicing.invoices.create_draft_invoice(
    detail={},
    id="string_example",
    parent_id="string_example",
    items="DRAFT",
    invoicer={},
    primary_recipients=[
        {
        }
    ],
    additional_recipients=[
        "j@Z,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mG"
    ],
    items=[
        {
            "name": "name_example",
            "quantity": "quantity_example",
            "unit_amount": {
                "currency_code": "currency_code_example",
                "value": "-.2888001528021798096225500850",
            },
            "unit_of_measure": "QUANTITY",
        }
    ],
    configuration={},
    amount={
    },
    due_amount={
        "currency_code": "currency_code_example",
        "value": "-.2888001528021798096225500850",
    },
    gratuity={
        "currency_code": "currency_code_example",
        "value": "-.2888001528021798096225500850",
    },
    payments={
    },
    refunds={
    },
    links=[
        {
            "href": "href_example",
            "rel": "rel_example",
            "method": "GET",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### detail: [`InvoiceDetail`](./pay_pal_invoicing_python_sdk/type/invoice_detail.py)<a id="detail-invoicedetailpay_pal_invoicing_python_sdktypeinvoice_detailpy"></a>


##### id: `str`<a id="id-str"></a>

The ID of the invoice.

##### parent_id: `str`<a id="parent_id-str"></a>

The parent ID to an invoice that defines the group invoice to which the invoice is related.

##### items: [`InvoiceStatus`](./pay_pal_invoicing_python_sdk/type/invoice_status.py)<a id="items-invoicestatuspay_pal_invoicing_python_sdktypeinvoice_statuspy"></a>

##### invoicer: [`InvoicerInfo`](./pay_pal_invoicing_python_sdk/type/invoicer_info.py)<a id="invoicer-invoicerinfopay_pal_invoicing_python_sdktypeinvoicer_infopy"></a>


##### primary_recipients: List[`RecipientInfo`]<a id="primary_recipients-listrecipientinfo"></a>

The billing and shipping information. Includes name, email, address, phone and language.

##### additional_recipients: List[`EmailAddress`]<a id="additional_recipients-listemailaddress"></a>

An array of one or more CC: emails to which notifications are sent. If you omit this parameter, a notification is sent to all CC: email addresses that are part of the invoice.<blockquote><strong>Note:</strong> Valid values are email addresses in the `additional_recipients` value associated with the invoice.</blockquote>

##### items: List[`Item`]<a id="items-listitem"></a>

An array of invoice line item information.

##### configuration: [`Configuration`](./pay_pal_invoicing_python_sdk/type/configuration.py)<a id="configuration-configurationpay_pal_invoicing_python_sdktypeconfigurationpy"></a>


##### amount: [`AmountSummaryDetail`](./pay_pal_invoicing_python_sdk/type/amount_summary_detail.py)<a id="amount-amountsummarydetailpay_pal_invoicing_python_sdktypeamount_summary_detailpy"></a>


##### due_amount: [`Money`](./pay_pal_invoicing_python_sdk/type/money.py)<a id="due_amount-moneypay_pal_invoicing_python_sdktypemoneypy"></a>


##### gratuity: [`Money`](./pay_pal_invoicing_python_sdk/type/money.py)<a id="gratuity-moneypay_pal_invoicing_python_sdktypemoneypy"></a>


##### payments: [`Payments`](./pay_pal_invoicing_python_sdk/type/payments.py)<a id="payments-paymentspay_pal_invoicing_python_sdktypepaymentspy"></a>


##### refunds: [`Refunds`](./pay_pal_invoicing_python_sdk/type/refunds.py)<a id="refunds-refundspay_pal_invoicing_python_sdktyperefundspy"></a>


##### links: List[`LinkDescription`]<a id="links-listlinkdescription"></a>

An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Invoice`](./pay_pal_invoicing_python_sdk/type/invoice.py)
The invoice details which includes all information of the invoice like items, billing information.

#### 🔄 Return<a id="🔄-return"></a>

[`Invoice`](./pay_pal_invoicing_python_sdk/pydantic/invoice.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.delete_draft_or_scheduled_invoice`<a id="paypalinvoicinginvoicesdelete_draft_or_scheduled_invoice"></a>

Deletes a draft or scheduled invoice, by ID. Deletes invoices in the draft or scheduled state only. For invoices that have already been sent, you can <a href="/docs/api/invoicing/v2/#invoices_cancel">cancel the invoice</a>. After you delete a draft or scheduled invoice, you can no longer use it or show its details. However, you can reuse its invoice number.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paypalinvoicing.invoices.delete_draft_or_scheduled_invoice(
    invoice_id="invoice_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_id: `str`<a id="invoice_id-str"></a>

The ID of the draft invoice to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices/{invoice_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.delete_external_payment`<a id="paypalinvoicinginvoicesdelete_external_payment"></a>

Deletes an external payment, by invoice ID and transaction ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paypalinvoicing.invoices.delete_external_payment(
    invoice_id="invoice_id_example",
    transaction_id="transaction_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_id: `str`<a id="invoice_id-str"></a>

The ID of the draft invoice to delete.

##### transaction_id: `str`<a id="transaction_id-str"></a>

The ID of the external refund transaction to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices/{invoice_id}/payments/{transaction_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.delete_external_refund`<a id="paypalinvoicinginvoicesdelete_external_refund"></a>

Deletes an external refund, by invoice ID and transaction ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paypalinvoicing.invoices.delete_external_refund(
    invoice_id="invoice_id_example",
    transaction_id="transaction_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_id: `str`<a id="invoice_id-str"></a>

The ID of the draft invoice to delete.

##### transaction_id: `str`<a id="transaction_id-str"></a>

The ID of the external refund transaction to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices/{invoice_id}/refunds/{transaction_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.generate_next_invoice_number`<a id="paypalinvoicinginvoicesgenerate_next_invoice_number"></a>

Generates the next invoice number that is available to the merchant. The next invoice number uses the prefix and suffix from the last invoice number and increments the number by one. For example, the next invoice number after `INVOICE-1234` is `INVOICE-1235`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_next_invoice_number_response = paypalinvoicing.invoices.generate_next_invoice_number()
```

#### 🔄 Return<a id="🔄-return"></a>

[`InvoiceNumber`](./pay_pal_invoicing_python_sdk/pydantic/invoice_number.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/generate-next-invoice-number` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.generate_qr_code`<a id="paypalinvoicinginvoicesgenerate_qr_code"></a>

Generates a QR code for an invoice, by ID. The QR code is a PNG image in <a href="https://www.base64encode.org/">Base64-encoded</a> format that corresponds to the invoice ID. You can generate a QR code for an invoice and add it to a paper or PDF invoice. When customers use their mobile devices to scan the QR code, they are redirected to the PayPal mobile payment flow where they can view the invoice and pay online with PayPal or a credit card. Before you get a QR code, you must <a href="#invoices_create">create an invoice</a> and <a href="#invoices_send">send an invoice</a> to move the invoice from a draft to payable state. Do not include an email address if you do not want the invoice emailed.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paypalinvoicing.invoices.generate_qr_code(
    invoice_id="invoice_id_example",
    width=500,
    height=500,
    action="pay",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_id: `str`<a id="invoice_id-str"></a>

The ID of the draft invoice to delete.

##### width: `int`<a id="width-int"></a>

The width, in pixels, of the QR code image. Value is from `150` to `500`.

##### height: `int`<a id="height-int"></a>

The height, in pixels, of the QR code image. Value is from `150` to `500`.

##### action: `str`<a id="action-str"></a>

The type of URL for which to generate a QR code. Valid values are `pay` and `details`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`QrConfig`](./pay_pal_invoicing_python_sdk/type/qr_config.py)
Optional configuration parameters to adjust QR code width, height and the encoded URL.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices/{invoice_id}/generate-qr-code` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.get_details`<a id="paypalinvoicinginvoicesget_details"></a>

Shows details for an invoice, by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = paypalinvoicing.invoices.get_details(
    invoice_id="invoice_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_id: `str`<a id="invoice_id-str"></a>

The ID of the draft invoice to delete.

#### 🔄 Return<a id="🔄-return"></a>

[`Invoice`](./pay_pal_invoicing_python_sdk/pydantic/invoice.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices/{invoice_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.get_invoices`<a id="paypalinvoicinginvoicesget_invoices"></a>

Lists invoices. To filter the invoices that appear in the response, you can specify one or more optional query parameters.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_invoices_response = paypalinvoicing.invoices.get_invoices(
    page=1,
    page_size=20,
    total_required=False,
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `int`<a id="page-int"></a>

The page number to be retrieved, for the list of templates. So, a combination of `page=1` and `page_size=20` returns the first 20 templates. A combination of `page=2` and `page_size=20` returns the next 20 templates.

##### page_size: `int`<a id="page_size-int"></a>

The maximum number of templates to return in the response.

##### total_required: `bool`<a id="total_required-bool"></a>

Indicates whether the to show <code>total_pages</code> and <code>total_items</code> in the response.

##### fields: `str`<a id="fields-str"></a>

The fields to return in the response. Value is `all` or `none`. To return only the template name, ID, and default attributes, specify `none`.

#### 🔄 Return<a id="🔄-return"></a>

[`Invoices`](./pay_pal_invoicing_python_sdk/pydantic/invoices.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.record_payment`<a id="paypalinvoicinginvoicesrecord_payment"></a>

Records a payment for the invoice. If no payment is due, the invoice is marked as `PAID`. Otherwise, the invoice is marked as `PARTIALLY PAID`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
record_payment_response = paypalinvoicing.invoices.record_payment(
    method="BANK_TRANSFER",
    invoice_id="invoice_id_example",
    type="PAYPAL",
    payment_id="string_example",
    payment_date="0480-08-03",
    note="string_example",
    amount={
        "currency_code": "currency_code_example",
        "value": "-.2888001528021798096225500850",
    },
    shipping_info={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### method: [`PaymentMethod`](./pay_pal_invoicing_python_sdk/type/payment_method.py)<a id="method-paymentmethodpay_pal_invoicing_python_sdktypepayment_methodpy"></a>

##### invoice_id: `str`<a id="invoice_id-str"></a>

The ID of the draft invoice to delete.

##### type: [`PaymentType`](./pay_pal_invoicing_python_sdk/type/payment_type.py)<a id="type-paymenttypepay_pal_invoicing_python_sdktypepayment_typepy"></a>

##### payment_id: `str`<a id="payment_id-str"></a>

The ID for a PayPal payment transaction. Required for the `PAYPAL` payment type.

##### payment_date: [`DateNoTime`](./pay_pal_invoicing_python_sdk/type/date_no_time.py)<a id="payment_date-datenotimepay_pal_invoicing_python_sdktypedate_no_timepy"></a>

##### note: `str`<a id="note-str"></a>

A note associated with an external cash or check payment.

##### amount: [`Money`](./pay_pal_invoicing_python_sdk/type/money.py)<a id="amount-moneypay_pal_invoicing_python_sdktypemoneypy"></a>


##### shipping_info: [`ContactNameAddress`](./pay_pal_invoicing_python_sdk/type/contact_name_address.py)<a id="shipping_info-contactnameaddresspay_pal_invoicing_python_sdktypecontact_name_addresspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentDetail`](./pay_pal_invoicing_python_sdk/type/payment_detail.py)
The details of the payment to record against the invoice.

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentReference`](./pay_pal_invoicing_python_sdk/pydantic/payment_reference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices/{invoice_id}/payments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.record_refund`<a id="paypalinvoicinginvoicesrecord_refund"></a>

Records a refund for the invoice. If all payments are refunded, the invoice is marked as `REFUNDED`. Otherwise, the invoice is marked as `PARTIALLY REFUNDED`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
record_refund_response = paypalinvoicing.invoices.record_refund(
    method="BANK_TRANSFER",
    invoice_id="invoice_id_example",
    type="PAYPAL",
    refund_id="string_example",
    refund_date="0480-08-03",
    amount={
        "currency_code": "currency_code_example",
        "value": "-.2888001528021798096225500850",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### method: [`PaymentMethod`](./pay_pal_invoicing_python_sdk/type/payment_method.py)<a id="method-paymentmethodpay_pal_invoicing_python_sdktypepayment_methodpy"></a>

##### invoice_id: `str`<a id="invoice_id-str"></a>

The ID of the draft invoice to delete.

##### type: [`PaymentType`](./pay_pal_invoicing_python_sdk/type/payment_type.py)<a id="type-paymenttypepay_pal_invoicing_python_sdktypepayment_typepy"></a>

##### refund_id: `str`<a id="refund_id-str"></a>

The ID for a PayPal payment transaction. Required for the `PAYPAL` payment type.

##### refund_date: [`DateNoTime`](./pay_pal_invoicing_python_sdk/type/date_no_time.py)<a id="refund_date-datenotimepay_pal_invoicing_python_sdktypedate_no_timepy"></a>

##### amount: [`Money`](./pay_pal_invoicing_python_sdk/type/money.py)<a id="amount-moneypay_pal_invoicing_python_sdktypemoneypy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RefundDetail`](./pay_pal_invoicing_python_sdk/type/refund_detail.py)
The details of the refund to record against the invoice.

#### 🔄 Return<a id="🔄-return"></a>

[`RefundReference`](./pay_pal_invoicing_python_sdk/pydantic/refund_reference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices/{invoice_id}/refunds` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.send_invoice`<a id="paypalinvoicinginvoicessend_invoice"></a>

Sends or schedules an invoice, by ID, to be sent to a customer. The action depends on the invoice issue date:<ul><li>If the invoice issue date is current or in the past, sends the invoice immediately.</li><li>If the invoice issue date is in the future, schedules the invoice to be sent on that date.</li></ul>To suppress the merchant's email notification, set the `send_to_invoicer` body parameter to `false`. To send the invoice through a share link and not through PayPal, set the <code>send_to_recipient</code> parameter to <code>false</code> in the <code>notification</code> object. The <code>send_to_recipient</code> parameter does not apply to a future issue date because the invoice is scheduled to be sent through PayPal on that date.<blockquote><strong>Notes:</strong><ul><li>After you send an invoice, resending it has no effect.</li><li>To send a notification for updates, <a href="#invoices_update">update the invoice</a> and set the <code>send_to_recipient</code> body parameter to <code>true</code>.</li></ul></blockquote>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_invoice_response = paypalinvoicing.invoices.send_invoice(
    invoice_id="invoice_id_example",
    subject="string_example",
    note="string_example",
    send_to_invoicer=False,
    send_to_recipient=True,
    additional_recipients=[
        "j@Z,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mG"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_id: `str`<a id="invoice_id-str"></a>

The ID of the draft invoice to delete.

##### subject: `str`<a id="subject-str"></a>

The subject of the email that is sent as a notification to the recipient.

##### note: `str`<a id="note-str"></a>

A note to the payer.

##### send_to_invoicer: `bool`<a id="send_to_invoicer-bool"></a>

Indicates whether to send a copy of the email to the merchant.

##### send_to_recipient: `bool`<a id="send_to_recipient-bool"></a>

Indicates whether to send a copy of the email to the recipient.

##### additional_recipients: List[`EmailAddress`]<a id="additional_recipients-listemailaddress"></a>

An array of one or more CC: emails to which notifications are sent. If you omit this parameter, a notification is sent to all CC: email addresses that are part of the invoice.<blockquote><strong>Note:</strong> Valid values are email addresses in the `additional_recipients` value associated with the invoice.</blockquote>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Notification`](./pay_pal_invoicing_python_sdk/type/notification.py)
The email or SMS notification to send to the payer when they send an invoice..

#### 🔄 Return<a id="🔄-return"></a>

[`LinkDescription`](./pay_pal_invoicing_python_sdk/pydantic/link_description.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices/{invoice_id}/send` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.send_reminder`<a id="paypalinvoicinginvoicessend_reminder"></a>

Sends a reminder to the payer about an invoice, by ID. In the JSON request body, include a `notification` object that defines the subject of the reminder and other details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paypalinvoicing.invoices.send_reminder(
    invoice_id="invoice_id_example",
    subject="string_example",
    note="string_example",
    send_to_invoicer=False,
    send_to_recipient=True,
    additional_recipients=[
        "j@Z,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mG"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### invoice_id: `str`<a id="invoice_id-str"></a>

The ID of the draft invoice to delete.

##### subject: `str`<a id="subject-str"></a>

The subject of the email that is sent as a notification to the recipient.

##### note: `str`<a id="note-str"></a>

A note to the payer.

##### send_to_invoicer: `bool`<a id="send_to_invoicer-bool"></a>

Indicates whether to send a copy of the email to the merchant.

##### send_to_recipient: `bool`<a id="send_to_recipient-bool"></a>

Indicates whether to send a copy of the email to the recipient.

##### additional_recipients: List[`EmailAddress`]<a id="additional_recipients-listemailaddress"></a>

An array of one or more CC: emails to which notifications are sent. If you omit this parameter, a notification is sent to all CC: email addresses that are part of the invoice.<blockquote><strong>Note:</strong> Valid values are email addresses in the `additional_recipients` value associated with the invoice.</blockquote>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Notification`](./pay_pal_invoicing_python_sdk/type/notification.py)
The email or SMS notification that will be sent to the payer for reminder.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices/{invoice_id}/remind` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.invoices.update_full_invoice`<a id="paypalinvoicinginvoicesupdate_full_invoice"></a>

Fully updates an invoice, by ID. In the JSON request body, include a complete `invoice` object. This call does not support partial updates.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_full_invoice_response = paypalinvoicing.invoices.update_full_invoice(
    detail={},
    invoice_id="invoice_id_example",
    id="string_example",
    parent_id="string_example",
    items="DRAFT",
    invoicer={},
    primary_recipients=[
        {
        }
    ],
    additional_recipients=[
        "j@Z,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:Ts\";mG"
    ],
    items=[
        {
            "name": "name_example",
            "quantity": "quantity_example",
            "unit_amount": {
                "currency_code": "currency_code_example",
                "value": "-.2888001528021798096225500850",
            },
            "unit_of_measure": "QUANTITY",
        }
    ],
    configuration={},
    amount={
    },
    due_amount={
        "currency_code": "currency_code_example",
        "value": "-.2888001528021798096225500850",
    },
    gratuity={
        "currency_code": "currency_code_example",
        "value": "-.2888001528021798096225500850",
    },
    payments={
    },
    refunds={
    },
    links=[
        {
            "href": "href_example",
            "rel": "rel_example",
            "method": "GET",
        }
    ],
    send_to_recipient=True,
    send_to_invoicer=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### detail: [`InvoiceDetail`](./pay_pal_invoicing_python_sdk/type/invoice_detail.py)<a id="detail-invoicedetailpay_pal_invoicing_python_sdktypeinvoice_detailpy"></a>


##### invoice_id: `str`<a id="invoice_id-str"></a>

The ID of the draft invoice to delete.

##### id: `str`<a id="id-str"></a>

The ID of the invoice.

##### parent_id: `str`<a id="parent_id-str"></a>

The parent ID to an invoice that defines the group invoice to which the invoice is related.

##### items: [`InvoiceStatus`](./pay_pal_invoicing_python_sdk/type/invoice_status.py)<a id="items-invoicestatuspay_pal_invoicing_python_sdktypeinvoice_statuspy"></a>

##### invoicer: [`InvoicerInfo`](./pay_pal_invoicing_python_sdk/type/invoicer_info.py)<a id="invoicer-invoicerinfopay_pal_invoicing_python_sdktypeinvoicer_infopy"></a>


##### primary_recipients: List[`RecipientInfo`]<a id="primary_recipients-listrecipientinfo"></a>

The billing and shipping information. Includes name, email, address, phone and language.

##### additional_recipients: List[`EmailAddress`]<a id="additional_recipients-listemailaddress"></a>

An array of one or more CC: emails to which notifications are sent. If you omit this parameter, a notification is sent to all CC: email addresses that are part of the invoice.<blockquote><strong>Note:</strong> Valid values are email addresses in the `additional_recipients` value associated with the invoice.</blockquote>

##### items: List[`Item`]<a id="items-listitem"></a>

An array of invoice line item information.

##### configuration: [`Configuration`](./pay_pal_invoicing_python_sdk/type/configuration.py)<a id="configuration-configurationpay_pal_invoicing_python_sdktypeconfigurationpy"></a>


##### amount: [`AmountSummaryDetail`](./pay_pal_invoicing_python_sdk/type/amount_summary_detail.py)<a id="amount-amountsummarydetailpay_pal_invoicing_python_sdktypeamount_summary_detailpy"></a>


##### due_amount: [`Money`](./pay_pal_invoicing_python_sdk/type/money.py)<a id="due_amount-moneypay_pal_invoicing_python_sdktypemoneypy"></a>


##### gratuity: [`Money`](./pay_pal_invoicing_python_sdk/type/money.py)<a id="gratuity-moneypay_pal_invoicing_python_sdktypemoneypy"></a>


##### payments: [`Payments`](./pay_pal_invoicing_python_sdk/type/payments.py)<a id="payments-paymentspay_pal_invoicing_python_sdktypepaymentspy"></a>


##### refunds: [`Refunds`](./pay_pal_invoicing_python_sdk/type/refunds.py)<a id="refunds-refundspay_pal_invoicing_python_sdktyperefundspy"></a>


##### links: List[`LinkDescription`]<a id="links-listlinkdescription"></a>

An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links).

##### send_to_recipient: `bool`<a id="send_to_recipient-bool"></a>

Indicates whether to send the invoice update notification to the recipient.

##### send_to_invoicer: `bool`<a id="send_to_invoicer-bool"></a>

Indicates whether to send the invoice update notification to the merchant.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Invoice`](./pay_pal_invoicing_python_sdk/type/invoice.py)
A representation of changes to make in the invoice.

#### 🔄 Return<a id="🔄-return"></a>

[`Invoice`](./pay_pal_invoicing_python_sdk/pydantic/invoice.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/invoices/{invoice_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.search_invoices.list`<a id="paypalinvoicingsearch_invoiceslist"></a>

Searches for and lists invoices that match search criteria. If you pass multiple criteria, the response lists invoices that match all criteria.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = paypalinvoicing.search_invoices.list(
    recipient_email="string_example",
    recipient_first_name="string_example",
    recipient_last_name="string_example",
    recipient_business_name="string_example",
    invoice_number="string_example",
    status=[
        "string_example"
    ],
    reference="string_example",
    currency_code="aaa",
    memo="string_example",
    total_amount_range={
        "lower_amount": {
            "currency_code": "currency_code_example",
            "value": "-.2888001528021798096225500850",
        },
,
    },
    invoice_date_range={
        "start": "0480-08-03",
        "end": "0480-08-03",
    },
    due_date_range={
        "start": "0480-08-03",
        "end": "0480-08-03",
    },
    payment_date_range={
        "start": "0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z",
        "end": "0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z",
    },
    creation_date_range={
        "start": "0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z",
        "end": "0480-08-03t01:32:60.79809622550085076206862933933397565068513910269129173272947860148202650912727550417577019298Z",
    },
    archived=True,
    fields=[
        "string_example"
    ],
    page=1,
    page_size=20,
    total_required=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recipient_email: `str`<a id="recipient_email-str"></a>

Filters the search by the email address.

##### recipient_first_name: `str`<a id="recipient_first_name-str"></a>

Filters the search by the recipient first name.

##### recipient_last_name: `str`<a id="recipient_last_name-str"></a>

Filters the search by the recipient last name.

##### recipient_business_name: `str`<a id="recipient_business_name-str"></a>

Filters the search by the recipient business name.

##### invoice_number: `str`<a id="invoice_number-str"></a>

Filters the search by the invoice number.

##### status: List[[`InvoiceStatus`](./pay_pal_invoicing_python_sdk/type/invoice_status.py)]<a id="status-listinvoicestatuspay_pal_invoicing_python_sdktypeinvoice_statuspy"></a>

An array of status values.

##### reference: `str`<a id="reference-str"></a>

The reference data, such as a PO number.

##### currency_code: [`CurrencyCode`](./pay_pal_invoicing_python_sdk/type/currency_code.py)<a id="currency_code-currencycodepay_pal_invoicing_python_sdktypecurrency_codepy"></a>

##### memo: `str`<a id="memo-str"></a>

A private bookkeeping memo for the user.

##### total_amount_range: [`AmountRange`](./pay_pal_invoicing_python_sdk/type/amount_range.py)<a id="total_amount_range-amountrangepay_pal_invoicing_python_sdktypeamount_rangepy"></a>


##### invoice_date_range: [`DateRange`](./pay_pal_invoicing_python_sdk/type/date_range.py)<a id="invoice_date_range-daterangepay_pal_invoicing_python_sdktypedate_rangepy"></a>


##### due_date_range: [`DateRange`](./pay_pal_invoicing_python_sdk/type/date_range.py)<a id="due_date_range-daterangepay_pal_invoicing_python_sdktypedate_rangepy"></a>


##### payment_date_range: [`DateTimeRange`](./pay_pal_invoicing_python_sdk/type/date_time_range.py)<a id="payment_date_range-datetimerangepay_pal_invoicing_python_sdktypedate_time_rangepy"></a>


##### creation_date_range: [`DateTimeRange`](./pay_pal_invoicing_python_sdk/type/date_time_range.py)<a id="creation_date_range-datetimerangepay_pal_invoicing_python_sdktypedate_time_rangepy"></a>


##### archived: `bool`<a id="archived-bool"></a>

Indicates whether to list merchant-archived invoices in the response. Value is:<ul><li><code>true</code>. Response lists only merchant-archived invoices.</li><li><code>false</code>. Response lists only unarchived invoices.</li><li><code>null</code>. Response lists all invoices.</li></ul>

##### fields: [`SearchDataFields`](./pay_pal_invoicing_python_sdk/type/search_data_fields.py)<a id="fields-searchdatafieldspay_pal_invoicing_python_sdktypesearch_data_fieldspy"></a>

##### page: `int`<a id="page-int"></a>

The page number to be retrieved, for the list of templates. So, a combination of `page=1` and `page_size=20` returns the first 20 templates. A combination of `page=2` and `page_size=20` returns the next 20 templates.

##### page_size: `int`<a id="page_size-int"></a>

The maximum number of templates to return in the response.

##### total_required: `bool`<a id="total_required-bool"></a>

Indicates whether the to show <code>total_pages</code> and <code>total_items</code> in the response.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SearchData`](./pay_pal_invoicing_python_sdk/type/search_data.py)
The invoice search can be used to retrieve the invoices based on the search parameters.

#### 🔄 Return<a id="🔄-return"></a>

[`Invoices`](./pay_pal_invoicing_python_sdk/pydantic/invoices.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/search-invoices` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.templates.create_template`<a id="paypalinvoicingtemplatescreate_template"></a>

Creates an invoice template. You can use details from this template to create an invoice. You can create up to 50 templates.<blockquote><strong>Note:</strong> Every merchant starts with three PayPal system templates that are optimized for the unit type billed. The template includes `Quantity`, `Hours`, and `Amount`.</blockquote>

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_template_response = paypalinvoicing.templates.create_template(
    id="string_example",
    name="a",
    default_template=True,
    template_info={
    },
    settings={
    },
    unit_of_measure="QUANTITY",
    standard_template=True,
    links=[
        {
            "href": "href_example",
            "rel": "rel_example",
            "method": "GET",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the template.

##### name: `str`<a id="name-str"></a>

The template name.<blockquote><strong>Note:</strong> The template name must be unique.</blockquote>

##### default_template: `bool`<a id="default_template-bool"></a>

Indicates whether this template is the default template. A invoicer can have one default template.

##### template_info: [`TemplateInfo`](./pay_pal_invoicing_python_sdk/type/template_info.py)<a id="template_info-templateinfopay_pal_invoicing_python_sdktypetemplate_infopy"></a>


##### settings: [`TemplateSettings`](./pay_pal_invoicing_python_sdk/type/template_settings.py)<a id="settings-templatesettingspay_pal_invoicing_python_sdktypetemplate_settingspy"></a>


##### unit_of_measure: [`UnitOfMeasure`](./pay_pal_invoicing_python_sdk/type/unit_of_measure.py)<a id="unit_of_measure-unitofmeasurepay_pal_invoicing_python_sdktypeunit_of_measurepy"></a>

##### standard_template: `bool`<a id="standard_template-bool"></a>

Indicates whether this template is a invoicer-created custom template. The system generates non-custom templates.

##### links: List[`LinkDescription`]<a id="links-listlinkdescription"></a>

An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Template`](./pay_pal_invoicing_python_sdk/type/template.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Template`](./pay_pal_invoicing_python_sdk/pydantic/template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/templates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.templates.delete_by_id`<a id="paypalinvoicingtemplatesdelete_by_id"></a>

Deletes a template, by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
paypalinvoicing.templates.delete_by_id(
    template_id="template_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

The ID of the template to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/templates/{template_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.templates.list_details`<a id="paypalinvoicingtemplateslist_details"></a>

Lists merchant-created templates with associated details. The associated details include the emails, addresses, and phone numbers from the user's PayPal profile.<br/>The user can select which values to show in the business information section of their template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_details_response = paypalinvoicing.templates.list_details(
    fields="all",
    page=1,
    page_size=20,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fields: `str`<a id="fields-str"></a>

The fields to return in the response. Value is `all` or `none`. To return only the template name, ID, and default attributes, specify `none`.

##### page: `int`<a id="page-int"></a>

The page number to be retrieved, for the list of templates. So, a combination of `page=1` and `page_size=20` returns the first 20 templates. A combination of `page=2` and `page_size=20` returns the next 20 templates.

##### page_size: `int`<a id="page_size-int"></a>

The maximum number of templates to return in the response.

#### 🔄 Return<a id="🔄-return"></a>

[`Templates`](./pay_pal_invoicing_python_sdk/pydantic/templates.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.templates.show_details_by_id`<a id="paypalinvoicingtemplatesshow_details_by_id"></a>

Shows details for a template, by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
show_details_by_id_response = paypalinvoicing.templates.show_details_by_id(
    template_id="template_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

The ID of the template to delete.

#### 🔄 Return<a id="🔄-return"></a>

[`Template`](./pay_pal_invoicing_python_sdk/pydantic/template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/templates/{template_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `paypalinvoicing.templates.update_full_template`<a id="paypalinvoicingtemplatesupdate_full_template"></a>

Fully updates a template, by ID. In the JSON request body, include a complete `template` object. This call does not support partial updates.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_full_template_response = paypalinvoicing.templates.update_full_template(
    template_id="template_id_example",
    id="string_example",
    name="a",
    default_template=True,
    template_info={
    },
    settings={
    },
    unit_of_measure="QUANTITY",
    standard_template=True,
    links=[
        {
            "href": "href_example",
            "rel": "rel_example",
            "method": "GET",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

The ID of the template to delete.

##### id: `str`<a id="id-str"></a>

The ID of the template.

##### name: `str`<a id="name-str"></a>

The template name.<blockquote><strong>Note:</strong> The template name must be unique.</blockquote>

##### default_template: `bool`<a id="default_template-bool"></a>

Indicates whether this template is the default template. A invoicer can have one default template.

##### template_info: [`TemplateInfo`](./pay_pal_invoicing_python_sdk/type/template_info.py)<a id="template_info-templateinfopay_pal_invoicing_python_sdktypetemplate_infopy"></a>


##### settings: [`TemplateSettings`](./pay_pal_invoicing_python_sdk/type/template_settings.py)<a id="settings-templatesettingspay_pal_invoicing_python_sdktypetemplate_settingspy"></a>


##### unit_of_measure: [`UnitOfMeasure`](./pay_pal_invoicing_python_sdk/type/unit_of_measure.py)<a id="unit_of_measure-unitofmeasurepay_pal_invoicing_python_sdktypeunit_of_measurepy"></a>

##### standard_template: `bool`<a id="standard_template-bool"></a>

Indicates whether this template is a invoicer-created custom template. The system generates non-custom templates.

##### links: List[`LinkDescription`]<a id="links-listlinkdescription"></a>

An array of request-related [HATEOAS links](/docs/api/reference/api-responses/#hateoas-links).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Template`](./pay_pal_invoicing_python_sdk/type/template.py)
A representation of changes to make in the template.

#### 🔄 Return<a id="🔄-return"></a>

[`Template`](./pay_pal_invoicing_python_sdk/pydantic/template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/invoicing/templates/{template_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)

@import 'dialog';

/* IE doesn't leave enough padding in text input for cursor to blink in RTL. (#6087) */
.cke_rtl input.cke_dialog_ui_input_text,
.cke_rtl input.cke_dialog_ui_input_password
{
	padding-right: 2px;
}
/* Compensate the padding added above on container. */
.cke_rtl div.cke_dialog_ui_input_text,
.cke_rtl div.cke_dialog_ui_input_password
{
	padding-left: 2px;
}
.cke_rtl div.cke_dialog_ui_input_text
{
	padding-right: 1px;
}

.cke_rtl .cke_dialog_ui_vbox_child,
.cke_rtl .cke_dialog_ui_hbox_child,
.cke_rtl .cke_dialog_ui_hbox_first,
.cke_rtl .cke_dialog_ui_hbox_last
{
	padding-right: 2px !important;
}


/* Disable filters for HC mode. */
.cke_hc .cke_dialog_title,
.cke_hc .cke_dialog_footer,
.cke_hc a.cke_dialog_tab,
.cke_hc a.cke_dialog_ui_button,
.cke_hc a.cke_dialog_ui_button:hover,
.cke_hc a.cke_dialog_ui_button_ok,
.cke_hc a.cke_dialog_ui_button_ok:hover
{
    filter: progid:DXImageTransform.Microsoft.gradient(enabled=false);
}

/* 	Remove border from dialog field wrappers in HC
	to avoid double borders. */
.cke_hc div.cke_dialog_ui_input_text,
.cke_hc div.cke_dialog_ui_input_password,
.cke_hc div.cke_dialog_ui_input_textarea,
.cke_hc div.cke_dialog_ui_input_select,
.cke_hc div.cke_dialog_ui_input_file
{
	border: 0;
}

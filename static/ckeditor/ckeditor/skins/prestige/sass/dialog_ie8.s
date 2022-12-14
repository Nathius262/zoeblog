@import 'dialog_ie';

/* Without min-height, border-box is not respected and button shrinks when 2px border on :focus is applied. */
a.cke_dialog_ui_button {
	min-height: 18px;
}

input.cke_dialog_ui_input_text,
input.cke_dialog_ui_input_password,
textarea.cke_dialog_ui_input_textarea
{
	min-height: 18px;
}

input.cke_dialog_ui_input_text:focus,
input.cke_dialog_ui_input_password:focus,
textarea.cke_dialog_ui_input_textarea:focus
{
	padding-top: 4px;
	padding-bottom: 2px;
}

select.cke_dialog_ui_input_select
{
	width: 100% !important;
}

select.cke_dialog_ui_input_select:focus
{
	margin-left: 1px;
	width: 100% !important;
	padding-top: 2px;
	padding-bottom: 2px;

}

/* Based on editor_ie.scss */
@import 'editor_ie';

.cke_toolbox_collapser .cke_arrow
{
	border-width:4px;
}
.cke_toolbox_collapser.cke_toolbox_collapser_min .cke_arrow
{
	border-width:3px;
}
.cke_toolbox_collapser .cke_arrow
{
	margin-top: 0;
}


/* Fix button group separators. Put separator after .cke_toolbar_end
	element instead of last button in a group. */
.cke_toolbar
{
	position: relative;
}

.cke_rtl .cke_toolbar_end
{
	right: auto;
	left: 0;
}

.cke_toolbar_end:after
{
	content: "";
	position: absolute;
	height: 18px;
	width: 0;
	border-right: 1px solid #bcbcbc;
	margin-top: 4px;
	top: 1px;
	right: 2px;
}

.cke_rtl .cke_toolbar_end:after
{
	right: auto;
	left: 2px;
}

.cke_hc .cke_toolbar_end:after {
	top: 2px;
	right: 5px;
	border-color: #000;
}

.cke_hc.cke_rtl .cke_toolbar_end:after {
	right: auto;
	left: 5px;
}

/* Do not show after combo and in the last group. */
.cke_combo + .cke_toolbar_end:after,
.cke_toolbar.cke_toolbar_last .cke_toolbar_end:after
{
	content: none;
	border: none;
}

/* Adjust margins when button is after combo in the same group. */
.cke_combo + .cke_toolgroup + .cke_toolbar_end:after
{
	right: 0;
}

.cke_rtl .cke_combo + .cke_toolgroup + .cke_toolbar_end:after
{
	right: auto;
	left: 0;
}

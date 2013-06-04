from wtforms import widgets

class TextInput(widgets.TextInput):
    def __call__(self, field, **kwargs):
        kwargs['placeholder'] = field.label.text
        kwargs['class']       = 'input-block-level'
        html = super(TextInput, self).__call__(field, **kwargs)

        if field.errors:
            span = ''.join(['<span class="help-inline">%s</span>' % (e) for e in field.errors])
            return '<div class="control-group error">%s%s</div>' % (html, span)
        else:
            return html

class PasswordInput(widgets.PasswordInput):
    def __call__(self, field, **kwargs):
        kwargs['placeholder'] = field.label.text
        kwargs['class']       = 'input-block-level'
        html = super(PasswordInput, self).__call__(field, **kwargs)

        if field.errors:
            span = ''.join(['<span class="help-inline">%s</span>' % (e) for e in field.errors])
            return '<div class="control-group error">%s%s</div>' % (html, span)
        else:
            return html

class CheckboxInput(widgets.CheckboxInput):
    def __call__(self, field, **kwargs):
        html = super(CheckboxInput, self).__call__(field, **kwargs)
        return '<label class="checkbox">%s%s</label>' % (html, field.label.text)

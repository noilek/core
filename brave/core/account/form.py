# encoding: utf-8

from __future__ import unicode_literals

from web.core.locale import L_
from marrow.widgets import Form, TextField, HiddenField, PasswordField, CheckboxField, EmailField, Widget, NestedWidget
from marrow.tags import html5 as H


class BlankSubmit(Widget):
    @property
    def template(self):
        return H.input(type_='submit')


class Container(NestedWidget):
    @property
    def template(self):
        return H.div ( id = self.name + '-wrapper', **self.args ) [
                ([child(self.data) for child in self.children])
            ]


authenticate = Form('authenticate', action='/account/authenticate', method='post', children=[
        TextField('identity', autofocus=True, class_="span12", placeholder=L_("OTP, User Name, or E-Mail Address")),
        PasswordField('password', class_="span12", placeholder=L_("Your Password")),
        BlankSubmit('submit'),
        HiddenField('redirect'),
    ])

register = Form('register', action='/account/register', method='post', children=[
        TextField('username', autofocus=True, autocapitalize="off", autocorrect="off", spellcheck="false", class_="span12", placeholder=L_("User Name")),
        EmailField('email', autocapitalize="off", autocorrect="off", spellcheck="false", class_="span12", placeholder=L_("E-Mail Address")),
        PasswordField('password', class_="span12 poor", placeholder=L_("Password"),maxlength="100"),
        PasswordField('pass2', class_="span12 poor", placeholder=L_("Verify Password"),maxlength="100"),
    ])

# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from typing import (
    Literal,
    TypedDict
)

LoginState = Literal[
    'SignIn',
    'SignUp'
]

DialogType = Literal[
    'AccountChooser',
    'AutoReauthn',
    'ConfirmIdpSignin'
]


class Account(TypedDict):
    accountId: str
    email: str
    name: str
    givenName: str
    pictureUrl: str
    idpConfigUrl: str
    idpSigninUrl: str
    loginState: 'LoginState'
    termsOfServiceUrl: str
    privacyPolicyUrl: str

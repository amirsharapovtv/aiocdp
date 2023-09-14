from dataclasses import (
    dataclass
)
from typing import (
    Literal
)

LoginState = Literal[
    "SignIn",
    "SignUp"
]

DialogType = Literal[
    "AccountChooser",
    "AutoReauthn",
    "ConfirmIdpSignin"
]


@dataclass
class Account:
    account_id: str
    email: str
    name: str
    given_name: str
    picture_url: str
    idp_config_url: str
    idp_signin_url: str
    login_state: "LoginState"
    terms_of_service_url: str
    privacy_policy_url: str
from dataclasses import (
    dataclass
)
from cdp.domains.base import (
    BaseDomain
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)
from cdp.domains.fed_cm.types import (
    LoginState,
    DialogType
)


@dataclass
class FedCm(BaseDomain):
    def enable(
        self,
        disable_rejection_delay: MaybeUndefined[]
    ):
        params = {}

        if is_defined(
            disable_rejection_delay
        ):
            params[] = disable_rejection_delay

        return self._send_command(
            "FedCm.enable",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "FedCm.disable",
            params
        )

    def select_account(
        self,
        dialog_id: str,
        account_index: int
    ):
        params = {
            "dialogId": dialog_id,
            "accountIndex": account_index,
        }

        return self._send_command(
            "FedCm.selectAccount",
            params
        )

    def confirm_idp_signin(
        self,
        dialog_id: str
    ):
        params = {
            "dialogId": dialog_id,
        }

        return self._send_command(
            "FedCm.confirmIdpSignin",
            params
        )

    def dismiss_dialog(
        self,
        dialog_id: str,
        trigger_cooldown: MaybeUndefined[]
    ):
        params = {
            "dialogId": dialog_id,
        }

        if is_defined(
            trigger_cooldown
        ):
            params[] = trigger_cooldown

        return self._send_command(
            "FedCm.dismissDialog",
            params
        )

    def reset_cooldown(
        self
    ):
        params = {}

        return self._send_command(
            "FedCm.resetCooldown",
            params
        )


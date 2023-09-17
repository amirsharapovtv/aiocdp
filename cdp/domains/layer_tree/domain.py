# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)
from typing import (
    TYPE_CHECKING
)
from cdp.domains.mapper import (
    from_dict,
    to_dict
)
from cdp.domains.layer_tree.types import (
    CompositingReasonsReturnT,
    LayerId,
    LoadSnapshotReturnT,
    MakeSnapshotReturnT,
    ProfileSnapshotReturnT,
    ReplaySnapshotReturnT,
    SnapshotCommandLogReturnT,
    SnapshotId
)
from cdp.domains.dom.types import (
    Rect
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResponse
    )


@dataclass
class LayerTree(BaseDomain):
    def compositing_reasons(
            self,
            layer_id: 'LayerId'
    ) -> IResponse[CompositingReasonsReturnT]:
        params = {
            'layerId': layer_id,
        }

        return self._send_command(
            'LayerTree.compositingReasons',
            params,
            True,
            lambda data: from_dict(
                CompositingReasonsReturnT,
                data,
                'camel'
            )
        )

    def disable(
            self
    ) -> IResponse[None]:
        params = {}

        return self._send_command(
            'LayerTree.disable',
            params,
            False
        )

    def enable(
            self
    ) -> IResponse[None]:
        params = {}

        return self._send_command(
            'LayerTree.enable',
            params,
            False
        )

    def load_snapshot(
            self,
            tiles: 'list'
    ) -> IResponse[LoadSnapshotReturnT]:
        params = {
            'tiles': [
                to_dict(item, 'camel')
                for item in tiles
            ],
        }

        return self._send_command(
            'LayerTree.loadSnapshot',
            params,
            True,
            lambda data: from_dict(
                LoadSnapshotReturnT,
                data,
                'camel'
            )
        )

    def make_snapshot(
            self,
            layer_id: 'LayerId'
    ) -> IResponse[MakeSnapshotReturnT]:
        params = {
            'layerId': layer_id,
        }

        return self._send_command(
            'LayerTree.makeSnapshot',
            params,
            True,
            lambda data: from_dict(
                MakeSnapshotReturnT,
                data,
                'camel'
            )
        )

    def profile_snapshot(
            self,
            snapshot_id: 'SnapshotId',
            min_repeat_count: 'int' = UNDEFINED,
            min_duration: 'float' = UNDEFINED,
            clip_rect: 'Rect' = UNDEFINED
    ) -> IResponse[ProfileSnapshotReturnT]:
        params = {
            'snapshotId': snapshot_id,
        }

        if is_defined(min_repeat_count):
            params['minRepeatCount'] = min_repeat_count

        if is_defined(min_duration):
            params['minDuration'] = min_duration

        if is_defined(clip_rect):
            params['clipRect'] = to_dict(
                clip_rect,
                'camel'
            )

        return self._send_command(
            'LayerTree.profileSnapshot',
            params,
            True,
            lambda data: from_dict(
                ProfileSnapshotReturnT,
                data,
                'camel'
            )
        )

    def release_snapshot(
            self,
            snapshot_id: 'SnapshotId'
    ) -> IResponse[None]:
        params = {
            'snapshotId': snapshot_id,
        }

        return self._send_command(
            'LayerTree.releaseSnapshot',
            params,
            False
        )

    def replay_snapshot(
            self,
            snapshot_id: 'SnapshotId',
            from_step: 'int' = UNDEFINED,
            to_step: 'int' = UNDEFINED,
            scale: 'float' = UNDEFINED
    ) -> IResponse[ReplaySnapshotReturnT]:
        params = {
            'snapshotId': snapshot_id,
        }

        if is_defined(from_step):
            params['fromStep'] = from_step

        if is_defined(to_step):
            params['toStep'] = to_step

        if is_defined(scale):
            params['scale'] = scale

        return self._send_command(
            'LayerTree.replaySnapshot',
            params,
            True,
            lambda data: from_dict(
                ReplaySnapshotReturnT,
                data,
                'camel'
            )
        )

    def snapshot_command_log(
            self,
            snapshot_id: 'SnapshotId'
    ) -> IResponse[SnapshotCommandLogReturnT]:
        params = {
            'snapshotId': snapshot_id,
        }

        return self._send_command(
            'LayerTree.snapshotCommandLog',
            params,
            True,
            lambda data: from_dict(
                SnapshotCommandLogReturnT,
                data,
                'camel'
            )
        )

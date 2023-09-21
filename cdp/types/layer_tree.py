# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.types import (
    dom
)
from typing import (
    TypedDict
)

LayerId = str

SnapshotId = str

PaintProfile = list


class ScrollRect(TypedDict):
    rect: 'dom.Rect'
    type: str


class StickyPositionConstraint(TypedDict):
    stickyBoxRect: 'dom.Rect'
    containingBlockRect: 'dom.Rect'
    nearestLayerShiftingStickyBox: 'LayerId'
    nearestLayerShiftingContainingBlock: 'LayerId'


class PictureTile(TypedDict):
    x: float
    y: float
    picture: str


class Layer(TypedDict):
    layerId: 'LayerId'
    offsetX: float
    offsetY: float
    width: float
    height: float
    paintCount: int
    drawsContent: bool
    parentLayerId: 'LayerId'
    backendNodeId: 'dom.BackendNodeId'
    transform: list
    anchorX: float
    anchorY: float
    anchorZ: float
    invisible: bool
    scrollRects: list
    stickyPositionConstraint: 'StickyPositionConstraint'

# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from typing import (
    Literal,
    TypedDict
)

GraphObjectId = str

NodeType = str

ParamType = str

ContextType = Literal[
    'realtime',
    'offline'
]

ContextState = Literal[
    'suspended',
    'running',
    'closed'
]

ChannelCountMode = Literal[
    'clamped-max',
    'explicit',
    'max'
]

ChannelInterpretation = Literal[
    'discrete',
    'speakers'
]

AutomationRate = Literal[
    'a-rate',
    'k-rate'
]


class ContextRealtimeData(TypedDict):
    currentTime: float
    renderCapacity: float
    callbackIntervalMean: float
    callbackIntervalVariance: float


class BaseAudioContext(TypedDict):
    contextId: 'GraphObjectId'
    contextType: 'ContextType'
    contextState: 'ContextState'
    callbackBufferSize: float
    maxOutputChannelCount: float
    sampleRate: float
    realtimeData: 'ContextRealtimeData'


class AudioListener(TypedDict):
    listenerId: 'GraphObjectId'
    contextId: 'GraphObjectId'


class AudioNode(TypedDict):
    nodeId: 'GraphObjectId'
    contextId: 'GraphObjectId'
    nodeType: 'NodeType'
    numberOfInputs: float
    numberOfOutputs: float
    channelCount: float
    channelCountMode: 'ChannelCountMode'
    channelInterpretation: 'ChannelInterpretation'


class AudioParam(TypedDict):
    paramId: 'GraphObjectId'
    nodeId: 'GraphObjectId'
    contextId: 'GraphObjectId'
    paramType: 'ParamType'
    rate: 'AutomationRate'
    defaultValue: float
    minValue: float
    maxValue: float

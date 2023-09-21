# DO NOT EDIT THIS FILE
#
# This file is generated by the generator. To make changes, edit the generator
# and run it again.

from cdp.types import (
    dom,
    page,
    runtime
)
from typing import (
    Literal,
    TypedDict
)

ContrastAlgorithm = Literal[
    'aa',
    'aaa',
    'apca'
]

ColorFormat = Literal[
    'rgb',
    'hsl',
    'hwb',
    'hex'
]

InspectMode = Literal[
    'searchForNode',
    'searchForUAShadowDOM',
    'captureAreaScreenshot',
    'showDistances',
    'none'
]


class SourceOrderConfig(TypedDict):
    parent_outline_color: 'dom.RGBA'
    child_outline_color: 'dom.RGBA'


class GridHighlightConfig(TypedDict):
    show_grid_extension_lines: bool
    show_positive_line_numbers: bool
    show_negative_line_numbers: bool
    show_area_names: bool
    show_line_names: bool
    show_track_sizes: bool
    grid_border_color: 'dom.RGBA'
    cell_border_color: 'dom.RGBA'
    row_line_color: 'dom.RGBA'
    column_line_color: 'dom.RGBA'
    grid_border_dash: bool
    cell_border_dash: bool
    row_line_dash: bool
    column_line_dash: bool
    row_gap_color: 'dom.RGBA'
    row_hatch_color: 'dom.RGBA'
    column_gap_color: 'dom.RGBA'
    column_hatch_color: 'dom.RGBA'
    area_border_color: 'dom.RGBA'
    grid_background_color: 'dom.RGBA'


class FlexContainerHighlightConfig(TypedDict):
    container_border: 'LineStyle'
    line_separator: 'LineStyle'
    item_separator: 'LineStyle'
    main_distributed_space: 'BoxStyle'
    cross_distributed_space: 'BoxStyle'
    row_gap_space: 'BoxStyle'
    column_gap_space: 'BoxStyle'
    cross_alignment: 'LineStyle'


class FlexItemHighlightConfig(TypedDict):
    base_size_box: 'BoxStyle'
    base_size_border: 'LineStyle'
    flexibility_arrow: 'LineStyle'


class LineStyle(TypedDict):
    color: 'dom.RGBA'
    pattern: str


class BoxStyle(TypedDict):
    fill_color: 'dom.RGBA'
    hatch_color: 'dom.RGBA'


class HighlightConfig(TypedDict):
    show_info: bool
    show_styles: bool
    show_rulers: bool
    show_accessibility_info: bool
    show_extension_lines: bool
    content_color: 'dom.RGBA'
    padding_color: 'dom.RGBA'
    border_color: 'dom.RGBA'
    margin_color: 'dom.RGBA'
    event_target_color: 'dom.RGBA'
    shape_color: 'dom.RGBA'
    shape_margin_color: 'dom.RGBA'
    css_grid_color: 'dom.RGBA'
    color_format: 'ColorFormat'
    grid_highlight_config: 'GridHighlightConfig'
    flex_container_highlight_config: 'FlexContainerHighlightConfig'
    flex_item_highlight_config: 'FlexItemHighlightConfig'
    contrast_algorithm: 'ContrastAlgorithm'
    container_query_container_highlight_config: 'ContainerQueryContainerHighlightConfig'


class GridNodeHighlightConfig(TypedDict):
    grid_highlight_config: 'GridHighlightConfig'
    node_id: 'dom.NodeId'


class FlexNodeHighlightConfig(TypedDict):
    flex_container_highlight_config: 'FlexContainerHighlightConfig'
    node_id: 'dom.NodeId'


class ScrollSnapContainerHighlightConfig(TypedDict):
    snapport_border: 'LineStyle'
    snap_area_border: 'LineStyle'
    scroll_margin_color: 'dom.RGBA'
    scroll_padding_color: 'dom.RGBA'


class ScrollSnapHighlightConfig(TypedDict):
    scroll_snap_container_highlight_config: 'ScrollSnapContainerHighlightConfig'
    node_id: 'dom.NodeId'


class HingeConfig(TypedDict):
    rect: 'dom.Rect'
    content_color: 'dom.RGBA'
    outline_color: 'dom.RGBA'


class ContainerQueryHighlightConfig(TypedDict):
    container_query_container_highlight_config: 'ContainerQueryContainerHighlightConfig'
    node_id: 'dom.NodeId'


class ContainerQueryContainerHighlightConfig(TypedDict):
    container_border: 'LineStyle'
    descendant_border: 'LineStyle'


class IsolatedElementHighlightConfig(TypedDict):
    isolation_mode_highlight_config: 'IsolationModeHighlightConfig'
    node_id: 'dom.NodeId'


class IsolationModeHighlightConfig(TypedDict):
    resizer_color: 'dom.RGBA'
    resizer_handle_color: 'dom.RGBA'
    mask_color: 'dom.RGBA'

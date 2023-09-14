from dataclasses import (
    dataclass
)
from cdp.domains.dom.types import (
    BackendNodeId,
    NodeId,
    Quad,
    RGBA
)
from cdp.domains.page.types import (
    FrameId
)
from cdp.domains.runtime.types import (
    RemoteObjectId
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)


@dataclass
class Overlay(BaseDomain):
    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Overlay.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Overlay.enable",
            params
        )

    def get_highlight_object_for_test(
        self,
        node_id: NodeId,
        include_distance: bool = UNDEFINED,
        include_style: bool = UNDEFINED,
        color_format: ColorFormat = UNDEFINED,
        show_accessibility_info: bool = UNDEFINED
    ):
        params = {
            ""nodeId"": node_id,
        }

        if is_defined(
            include_distance
        ):
            params["includeDistance"] = include_distance

        if is_defined(
            include_style
        ):
            params["includeStyle"] = include_style

        if is_defined(
            color_format
        ):
            params["colorFormat"] = color_format

        if is_defined(
            show_accessibility_info
        ):
            params["showAccessibilityInfo"] = show_accessibility_info

        return self._send_command(
            "Overlay.getHighlightObjectForTest",
            params
        )

    def get_grid_highlight_objects_for_test(
        self,
        node_ids: list
    ):
        params = {
            ""nodeIds"": node_ids,
        }

        return self._send_command(
            "Overlay.getGridHighlightObjectsForTest",
            params
        )

    def get_source_order_highlight_object_for_test(
        self,
        node_id: NodeId
    ):
        params = {
            ""nodeId"": node_id,
        }

        return self._send_command(
            "Overlay.getSourceOrderHighlightObjectForTest",
            params
        )

    def hide_highlight(
        self
    ):
        params = {}

        return self._send_command(
            "Overlay.hideHighlight",
            params
        )

    def highlight_frame(
        self,
        frame_id: FrameId,
        content_color: RGBA = UNDEFINED,
        content_outline_color: RGBA = UNDEFINED
    ):
        params = {
            ""frameId"": frame_id,
        }

        if is_defined(
            content_color
        ):
            params["contentColor"] = content_color

        if is_defined(
            content_outline_color
        ):
            params["contentOutlineColor"] = content_outline_color

        return self._send_command(
            "Overlay.highlightFrame",
            params
        )

    def highlight_node(
        self,
        highlight_config: HighlightConfig,
        node_id: NodeId = UNDEFINED,
        backend_node_id: BackendNodeId = UNDEFINED,
        object_id: RemoteObjectId = UNDEFINED,
        selector: str = UNDEFINED
    ):
        params = {
            ""highlightConfig"": highlight_config,
        }

        if is_defined(
            node_id
        ):
            params["nodeId"] = node_id

        if is_defined(
            backend_node_id
        ):
            params["backendNodeId"] = backend_node_id

        if is_defined(
            object_id
        ):
            params["objectId"] = object_id

        if is_defined(
            selector
        ):
            params["selector"] = selector

        return self._send_command(
            "Overlay.highlightNode",
            params
        )

    def highlight_quad(
        self,
        quad: Quad,
        color: RGBA = UNDEFINED,
        outline_color: RGBA = UNDEFINED
    ):
        params = {
            ""quad"": quad,
        }

        if is_defined(
            color
        ):
            params["color"] = color

        if is_defined(
            outline_color
        ):
            params["outlineColor"] = outline_color

        return self._send_command(
            "Overlay.highlightQuad",
            params
        )

    def highlight_rect(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: RGBA = UNDEFINED,
        outline_color: RGBA = UNDEFINED
    ):
        params = {
            ""x"": x,
            ""y"": y,
            ""width"": width,
            ""height"": height,
        }

        if is_defined(
            color
        ):
            params["color"] = color

        if is_defined(
            outline_color
        ):
            params["outlineColor"] = outline_color

        return self._send_command(
            "Overlay.highlightRect",
            params
        )

    def highlight_source_order(
        self,
        source_order_config: SourceOrderConfig,
        node_id: NodeId = UNDEFINED,
        backend_node_id: BackendNodeId = UNDEFINED,
        object_id: RemoteObjectId = UNDEFINED
    ):
        params = {
            ""sourceOrderConfig"": source_order_config,
        }

        if is_defined(
            node_id
        ):
            params["nodeId"] = node_id

        if is_defined(
            backend_node_id
        ):
            params["backendNodeId"] = backend_node_id

        if is_defined(
            object_id
        ):
            params["objectId"] = object_id

        return self._send_command(
            "Overlay.highlightSourceOrder",
            params
        )

    def set_inspect_mode(
        self,
        mode: InspectMode,
        highlight_config: HighlightConfig = UNDEFINED
    ):
        params = {
            ""mode"": mode,
        }

        if is_defined(
            highlight_config
        ):
            params["highlightConfig"] = highlight_config

        return self._send_command(
            "Overlay.setInspectMode",
            params
        )

    def set_show_ad_highlights(
        self,
        show: bool
    ):
        params = {
            ""show"": show,
        }

        return self._send_command(
            "Overlay.setShowAdHighlights",
            params
        )

    def set_paused_in_debugger_message(
        self,
        message: str = UNDEFINED
    ):
        params = {}

        if is_defined(
            message
        ):
            params["message"] = message

        return self._send_command(
            "Overlay.setPausedInDebuggerMessage",
            params
        )

    def set_show_debug_borders(
        self,
        show: bool
    ):
        params = {
            ""show"": show,
        }

        return self._send_command(
            "Overlay.setShowDebugBorders",
            params
        )

    def set_show_fps_counter(
        self,
        show: bool
    ):
        params = {
            ""show"": show,
        }

        return self._send_command(
            "Overlay.setShowFPSCounter",
            params
        )

    def set_show_grid_overlays(
        self,
        grid_node_highlight_configs: list
    ):
        params = {
            ""gridNodeHighlightConfigs"": grid_node_highlight_configs,
        }

        return self._send_command(
            "Overlay.setShowGridOverlays",
            params
        )

    def set_show_flex_overlays(
        self,
        flex_node_highlight_configs: list
    ):
        params = {
            ""flexNodeHighlightConfigs"": flex_node_highlight_configs,
        }

        return self._send_command(
            "Overlay.setShowFlexOverlays",
            params
        )

    def set_show_scroll_snap_overlays(
        self,
        scroll_snap_highlight_configs: list
    ):
        params = {
            ""scrollSnapHighlightConfigs"": scroll_snap_highlight_configs,
        }

        return self._send_command(
            "Overlay.setShowScrollSnapOverlays",
            params
        )

    def set_show_container_query_overlays(
        self,
        container_query_highlight_configs: list
    ):
        params = {
            ""containerQueryHighlightConfigs"": container_query_highlight_configs,
        }

        return self._send_command(
            "Overlay.setShowContainerQueryOverlays",
            params
        )

    def set_show_paint_rects(
        self,
        result: bool
    ):
        params = {
            ""result"": result,
        }

        return self._send_command(
            "Overlay.setShowPaintRects",
            params
        )

    def set_show_layout_shift_regions(
        self,
        result: bool
    ):
        params = {
            ""result"": result,
        }

        return self._send_command(
            "Overlay.setShowLayoutShiftRegions",
            params
        )

    def set_show_scroll_bottleneck_rects(
        self,
        show: bool
    ):
        params = {
            ""show"": show,
        }

        return self._send_command(
            "Overlay.setShowScrollBottleneckRects",
            params
        )

    def set_show_hit_test_borders(
        self,
        show: bool
    ):
        params = {
            ""show"": show,
        }

        return self._send_command(
            "Overlay.setShowHitTestBorders",
            params
        )

    def set_show_web_vitals(
        self,
        show: bool
    ):
        params = {
            ""show"": show,
        }

        return self._send_command(
            "Overlay.setShowWebVitals",
            params
        )

    def set_show_viewport_size_on_resize(
        self,
        show: bool
    ):
        params = {
            ""show"": show,
        }

        return self._send_command(
            "Overlay.setShowViewportSizeOnResize",
            params
        )

    def set_show_hinge(
        self,
        hinge_config: HingeConfig = UNDEFINED
    ):
        params = {}

        if is_defined(
            hinge_config
        ):
            params["hingeConfig"] = hinge_config

        return self._send_command(
            "Overlay.setShowHinge",
            params
        )

    def set_show_isolated_elements(
        self,
        isolated_element_highlight_configs: list
    ):
        params = {
            ""isolatedElementHighlightConfigs"": isolated_element_highlight_configs,
        }

        return self._send_command(
            "Overlay.setShowIsolatedElements",
            params
        )


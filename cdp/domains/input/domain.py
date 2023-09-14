from cdp.domains.base import (
    BaseDomain
)
from dataclasses import (
    dataclass
)
from cdp.domains.input.types import (
    DragData,
    GestureSourceType,
    MouseButton,
    TimeSinceEpoch
)
from cdp.utils import (
    is_defined,
    UNDEFINED
)


@dataclass
class Input(BaseDomain):
    def dispatch_drag_event(
        self,
        type_: str,
        x: float,
        y: float,
        data: DragData,
        modifiers: int = UNDEFINED
    ):
        params = {
            "type": type_,
            "x": x,
            "y": y,
            "data": data,
        }

        if is_defined(
            modifiers
        ):
            params["modifiers"] = modifiers

        return self._send_command(
            "Input.dispatchDragEvent",
            params
        )

    def dispatch_key_event(
        self,
        type_: str,
        modifiers: int = UNDEFINED,
        timestamp: TimeSinceEpoch = UNDEFINED,
        text: str = UNDEFINED,
        unmodified_text: str = UNDEFINED,
        key_identifier: str = UNDEFINED,
        code: str = UNDEFINED,
        key: str = UNDEFINED,
        windows_virtual_key_code: int = UNDEFINED,
        native_virtual_key_code: int = UNDEFINED,
        auto_repeat: bool = UNDEFINED,
        is_keypad: bool = UNDEFINED,
        is_system_key: bool = UNDEFINED,
        location: int = UNDEFINED,
        commands: list = UNDEFINED
    ):
        params = {
            "type": type_,
        }

        if is_defined(
            modifiers
        ):
            params["modifiers"] = modifiers

        if is_defined(
            timestamp
        ):
            params["timestamp"] = timestamp

        if is_defined(
            text
        ):
            params["text"] = text

        if is_defined(
            unmodified_text
        ):
            params["unmodifiedText"] = unmodified_text

        if is_defined(
            key_identifier
        ):
            params["keyIdentifier"] = key_identifier

        if is_defined(
            code
        ):
            params["code"] = code

        if is_defined(
            key
        ):
            params["key"] = key

        if is_defined(
            windows_virtual_key_code
        ):
            params["windowsVirtualKeyCode"] = windows_virtual_key_code

        if is_defined(
            native_virtual_key_code
        ):
            params["nativeVirtualKeyCode"] = native_virtual_key_code

        if is_defined(
            auto_repeat
        ):
            params["autoRepeat"] = auto_repeat

        if is_defined(
            is_keypad
        ):
            params["isKeypad"] = is_keypad

        if is_defined(
            is_system_key
        ):
            params["isSystemKey"] = is_system_key

        if is_defined(
            location
        ):
            params["location"] = location

        if is_defined(
            commands
        ):
            params["commands"] = commands

        return self._send_command(
            "Input.dispatchKeyEvent",
            params
        )

    def insert_text(
        self,
        text: str
    ):
        params = {
            "text": text,
        }

        return self._send_command(
            "Input.insertText",
            params
        )

    def ime_set_composition(
        self,
        text: str,
        selection_start: int,
        selection_end: int,
        replacement_start: int = UNDEFINED,
        replacement_end: int = UNDEFINED
    ):
        params = {
            "text": text,
            "selectionStart": selection_start,
            "selectionEnd": selection_end,
        }

        if is_defined(
            replacement_start
        ):
            params["replacementStart"] = replacement_start

        if is_defined(
            replacement_end
        ):
            params["replacementEnd"] = replacement_end

        return self._send_command(
            "Input.imeSetComposition",
            params
        )

    def dispatch_mouse_event(
        self,
        type_: str,
        x: float,
        y: float,
        modifiers: int = UNDEFINED,
        timestamp: TimeSinceEpoch = UNDEFINED,
        button: MouseButton = UNDEFINED,
        buttons: int = UNDEFINED,
        click_count: int = UNDEFINED,
        force: float = UNDEFINED,
        tangential_pressure: float = UNDEFINED,
        tilt_x: int = UNDEFINED,
        tilt_y: int = UNDEFINED,
        twist: int = UNDEFINED,
        delta_x: float = UNDEFINED,
        delta_y: float = UNDEFINED,
        pointer_type: str = UNDEFINED
    ):
        params = {
            "type": type_,
            "x": x,
            "y": y,
        }

        if is_defined(
            modifiers
        ):
            params["modifiers"] = modifiers

        if is_defined(
            timestamp
        ):
            params["timestamp"] = timestamp

        if is_defined(
            button
        ):
            params["button"] = button

        if is_defined(
            buttons
        ):
            params["buttons"] = buttons

        if is_defined(
            click_count
        ):
            params["clickCount"] = click_count

        if is_defined(
            force
        ):
            params["force"] = force

        if is_defined(
            tangential_pressure
        ):
            params["tangentialPressure"] = tangential_pressure

        if is_defined(
            tilt_x
        ):
            params["tiltX"] = tilt_x

        if is_defined(
            tilt_y
        ):
            params["tiltY"] = tilt_y

        if is_defined(
            twist
        ):
            params["twist"] = twist

        if is_defined(
            delta_x
        ):
            params["deltaX"] = delta_x

        if is_defined(
            delta_y
        ):
            params["deltaY"] = delta_y

        if is_defined(
            pointer_type
        ):
            params["pointerType"] = pointer_type

        return self._send_command(
            "Input.dispatchMouseEvent",
            params
        )

    def dispatch_touch_event(
        self,
        type_: str,
        touch_points: list,
        modifiers: int = UNDEFINED,
        timestamp: TimeSinceEpoch = UNDEFINED
    ):
        params = {
            "type": type_,
            "touchPoints": touch_points,
        }

        if is_defined(
            modifiers
        ):
            params["modifiers"] = modifiers

        if is_defined(
            timestamp
        ):
            params["timestamp"] = timestamp

        return self._send_command(
            "Input.dispatchTouchEvent",
            params
        )

    def cancel_dragging(
        self
    ):
        params = {}

        return self._send_command(
            "Input.cancelDragging",
            params
        )

    def emulate_touch_from_mouse_event(
        self,
        type_: str,
        x: int,
        y: int,
        button: MouseButton,
        timestamp: TimeSinceEpoch = UNDEFINED,
        delta_x: float = UNDEFINED,
        delta_y: float = UNDEFINED,
        modifiers: int = UNDEFINED,
        click_count: int = UNDEFINED
    ):
        params = {
            "type": type_,
            "x": x,
            "y": y,
            "button": button,
        }

        if is_defined(
            timestamp
        ):
            params["timestamp"] = timestamp

        if is_defined(
            delta_x
        ):
            params["deltaX"] = delta_x

        if is_defined(
            delta_y
        ):
            params["deltaY"] = delta_y

        if is_defined(
            modifiers
        ):
            params["modifiers"] = modifiers

        if is_defined(
            click_count
        ):
            params["clickCount"] = click_count

        return self._send_command(
            "Input.emulateTouchFromMouseEvent",
            params
        )

    def set_ignore_input_events(
        self,
        ignore: bool
    ):
        params = {
            "ignore": ignore,
        }

        return self._send_command(
            "Input.setIgnoreInputEvents",
            params
        )

    def set_intercept_drags(
        self,
        enabled: bool
    ):
        params = {
            "enabled": enabled,
        }

        return self._send_command(
            "Input.setInterceptDrags",
            params
        )

    def synthesize_pinch_gesture(
        self,
        x: float,
        y: float,
        scale_factor: float,
        relative_speed: int = UNDEFINED,
        gesture_source_type: GestureSourceType = UNDEFINED
    ):
        params = {
            "x": x,
            "y": y,
            "scaleFactor": scale_factor,
        }

        if is_defined(
            relative_speed
        ):
            params["relativeSpeed"] = relative_speed

        if is_defined(
            gesture_source_type
        ):
            params["gestureSourceType"] = gesture_source_type

        return self._send_command(
            "Input.synthesizePinchGesture",
            params
        )

    def synthesize_scroll_gesture(
        self,
        x: float,
        y: float,
        x_distance: float = UNDEFINED,
        y_distance: float = UNDEFINED,
        x_overscroll: float = UNDEFINED,
        y_overscroll: float = UNDEFINED,
        prevent_fling: bool = UNDEFINED,
        speed: int = UNDEFINED,
        gesture_source_type: GestureSourceType = UNDEFINED,
        repeat_count: int = UNDEFINED,
        repeat_delay_ms: int = UNDEFINED,
        interaction_marker_name: str = UNDEFINED
    ):
        params = {
            "x": x,
            "y": y,
        }

        if is_defined(
            x_distance
        ):
            params["xDistance"] = x_distance

        if is_defined(
            y_distance
        ):
            params["yDistance"] = y_distance

        if is_defined(
            x_overscroll
        ):
            params["xOverscroll"] = x_overscroll

        if is_defined(
            y_overscroll
        ):
            params["yOverscroll"] = y_overscroll

        if is_defined(
            prevent_fling
        ):
            params["preventFling"] = prevent_fling

        if is_defined(
            speed
        ):
            params["speed"] = speed

        if is_defined(
            gesture_source_type
        ):
            params["gestureSourceType"] = gesture_source_type

        if is_defined(
            repeat_count
        ):
            params["repeatCount"] = repeat_count

        if is_defined(
            repeat_delay_ms
        ):
            params["repeatDelayMs"] = repeat_delay_ms

        if is_defined(
            interaction_marker_name
        ):
            params["interactionMarkerName"] = interaction_marker_name

        return self._send_command(
            "Input.synthesizeScrollGesture",
            params
        )

    def synthesize_tap_gesture(
        self,
        x: float,
        y: float,
        duration: int = UNDEFINED,
        tap_count: int = UNDEFINED,
        gesture_source_type: GestureSourceType = UNDEFINED
    ):
        params = {
            "x": x,
            "y": y,
        }

        if is_defined(
            duration
        ):
            params["duration"] = duration

        if is_defined(
            tap_count
        ):
            params["tapCount"] = tap_count

        if is_defined(
            gesture_source_type
        ):
            params["gestureSourceType"] = gesture_source_type

        return self._send_command(
            "Input.synthesizeTapGesture",
            params
        )

from dataclasses import (
    dataclass
)
from cdp.domains.emulation.types import (
    ScreenOrientation
)
from cdp.utils import (
    is_defined,
    MaybeUndefined,
    UNDEFINED
)


@dataclass
class Page(BaseDomain):
    def add_script_to_evaluate_on_load(
        self,
        script_source: str
    ):
        params = {
            ""scriptSource"": script_source,
        }

        return self._send_command(
            "Page.addScriptToEvaluateOnLoad",
            params
        )

    def add_script_to_evaluate_on_new_document(
        self,
        source: str,
        world_name: str = UNDEFINED,
        include_command_line_api: bool = UNDEFINED,
        run_immediately: bool = UNDEFINED
    ):
        params = {
            ""source"": source,
        }

        if is_defined(
            world_name
        ):
            params["worldName"] = world_name

        if is_defined(
            include_command_line_api
        ):
            params["includeCommandLineAPI"] = include_command_line_api

        if is_defined(
            run_immediately
        ):
            params["runImmediately"] = run_immediately

        return self._send_command(
            "Page.addScriptToEvaluateOnNewDocument",
            params
        )

    def bring_to_front(
        self
    ):
        params = {}

        return self._send_command(
            "Page.bringToFront",
            params
        )

    def capture_screenshot(
        self,
        format_: str = UNDEFINED,
        quality: int = UNDEFINED,
        clip: Viewport = UNDEFINED,
        from_surface: bool = UNDEFINED,
        capture_beyond_viewport: bool = UNDEFINED,
        optimize_for_speed: bool = UNDEFINED
    ):
        params = {}

        if is_defined(
            format
        ):
            params["format"] = format

        if is_defined(
            quality
        ):
            params["quality"] = quality

        if is_defined(
            clip
        ):
            params["clip"] = clip

        if is_defined(
            from_surface
        ):
            params["fromSurface"] = from_surface

        if is_defined(
            capture_beyond_viewport
        ):
            params["captureBeyondViewport"] = capture_beyond_viewport

        if is_defined(
            optimize_for_speed
        ):
            params["optimizeForSpeed"] = optimize_for_speed

        return self._send_command(
            "Page.captureScreenshot",
            params
        )

    def capture_snapshot(
        self,
        format_: str = UNDEFINED
    ):
        params = {}

        if is_defined(
            format
        ):
            params["format"] = format

        return self._send_command(
            "Page.captureSnapshot",
            params
        )

    def clear_device_metrics_override(
        self
    ):
        params = {}

        return self._send_command(
            "Page.clearDeviceMetricsOverride",
            params
        )

    def clear_device_orientation_override(
        self
    ):
        params = {}

        return self._send_command(
            "Page.clearDeviceOrientationOverride",
            params
        )

    def clear_geolocation_override(
        self
    ):
        params = {}

        return self._send_command(
            "Page.clearGeolocationOverride",
            params
        )

    def create_isolated_world(
        self,
        frame_id: FrameId,
        world_name: str = UNDEFINED,
        grant_univeral_access: bool = UNDEFINED
    ):
        params = {
            ""frameId"": frame_id,
        }

        if is_defined(
            world_name
        ):
            params["worldName"] = world_name

        if is_defined(
            grant_univeral_access
        ):
            params["grantUniveralAccess"] = grant_univeral_access

        return self._send_command(
            "Page.createIsolatedWorld",
            params
        )

    def delete_cookie(
        self,
        cookie_name: str,
        url: str
    ):
        params = {
            ""cookieName"": cookie_name,
            ""url"": url,
        }

        return self._send_command(
            "Page.deleteCookie",
            params
        )

    def disable(
        self
    ):
        params = {}

        return self._send_command(
            "Page.disable",
            params
        )

    def enable(
        self
    ):
        params = {}

        return self._send_command(
            "Page.enable",
            params
        )

    def get_app_manifest(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getAppManifest",
            params
        )

    def get_installability_errors(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getInstallabilityErrors",
            params
        )

    def get_manifest_icons(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getManifestIcons",
            params
        )

    def get_app_id(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getAppId",
            params
        )

    def get_ad_script_id(
        self,
        frame_id: FrameId
    ):
        params = {
            ""frameId"": frame_id,
        }

        return self._send_command(
            "Page.getAdScriptId",
            params
        )

    def get_cookies(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getCookies",
            params
        )

    def get_frame_tree(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getFrameTree",
            params
        )

    def get_layout_metrics(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getLayoutMetrics",
            params
        )

    def get_navigation_history(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getNavigationHistory",
            params
        )

    def reset_navigation_history(
        self
    ):
        params = {}

        return self._send_command(
            "Page.resetNavigationHistory",
            params
        )

    def get_resource_content(
        self,
        frame_id: FrameId,
        url: str
    ):
        params = {
            ""frameId"": frame_id,
            ""url"": url,
        }

        return self._send_command(
            "Page.getResourceContent",
            params
        )

    def get_resource_tree(
        self
    ):
        params = {}

        return self._send_command(
            "Page.getResourceTree",
            params
        )

    def handle_java_script_dialog(
        self,
        accept: bool,
        prompt_text: str = UNDEFINED
    ):
        params = {
            ""accept"": accept,
        }

        if is_defined(
            prompt_text
        ):
            params["promptText"] = prompt_text

        return self._send_command(
            "Page.handleJavaScriptDialog",
            params
        )

    def navigate(
        self,
        url: str,
        referrer: str = UNDEFINED,
        transition_type: TransitionType = UNDEFINED,
        frame_id: FrameId = UNDEFINED,
        referrer_policy: ReferrerPolicy = UNDEFINED
    ):
        params = {
            ""url"": url,
        }

        if is_defined(
            referrer
        ):
            params["referrer"] = referrer

        if is_defined(
            transition_type
        ):
            params["transitionType"] = transition_type

        if is_defined(
            frame_id
        ):
            params["frameId"] = frame_id

        if is_defined(
            referrer_policy
        ):
            params["referrerPolicy"] = referrer_policy

        return self._send_command(
            "Page.navigate",
            params
        )

    def navigate_to_history_entry(
        self,
        entry_id: int
    ):
        params = {
            ""entryId"": entry_id,
        }

        return self._send_command(
            "Page.navigateToHistoryEntry",
            params
        )

    def print_to_pdf(
        self,
        landscape: bool = UNDEFINED,
        display_header_footer: bool = UNDEFINED,
        print_background: bool = UNDEFINED,
        scale: float = UNDEFINED,
        paper_width: float = UNDEFINED,
        paper_height: float = UNDEFINED,
        margin_top: float = UNDEFINED,
        margin_bottom: float = UNDEFINED,
        margin_left: float = UNDEFINED,
        margin_right: float = UNDEFINED,
        page_ranges: str = UNDEFINED,
        header_template: str = UNDEFINED,
        footer_template: str = UNDEFINED,
        prefer_css_page_size: bool = UNDEFINED,
        transfer_mode: str = UNDEFINED,
        generate_tagged_pdf: bool = UNDEFINED
    ):
        params = {}

        if is_defined(
            landscape
        ):
            params["landscape"] = landscape

        if is_defined(
            display_header_footer
        ):
            params["displayHeaderFooter"] = display_header_footer

        if is_defined(
            print_background
        ):
            params["printBackground"] = print_background

        if is_defined(
            scale
        ):
            params["scale"] = scale

        if is_defined(
            paper_width
        ):
            params["paperWidth"] = paper_width

        if is_defined(
            paper_height
        ):
            params["paperHeight"] = paper_height

        if is_defined(
            margin_top
        ):
            params["marginTop"] = margin_top

        if is_defined(
            margin_bottom
        ):
            params["marginBottom"] = margin_bottom

        if is_defined(
            margin_left
        ):
            params["marginLeft"] = margin_left

        if is_defined(
            margin_right
        ):
            params["marginRight"] = margin_right

        if is_defined(
            page_ranges
        ):
            params["pageRanges"] = page_ranges

        if is_defined(
            header_template
        ):
            params["headerTemplate"] = header_template

        if is_defined(
            footer_template
        ):
            params["footerTemplate"] = footer_template

        if is_defined(
            prefer_css_page_size
        ):
            params["preferCSSPageSize"] = prefer_css_page_size

        if is_defined(
            transfer_mode
        ):
            params["transferMode"] = transfer_mode

        if is_defined(
            generate_tagged_pdf
        ):
            params["generateTaggedPDF"] = generate_tagged_pdf

        return self._send_command(
            "Page.printToPDF",
            params
        )

    def reload(
        self,
        ignore_cache: bool = UNDEFINED,
        script_to_evaluate_on_load: str = UNDEFINED
    ):
        params = {}

        if is_defined(
            ignore_cache
        ):
            params["ignoreCache"] = ignore_cache

        if is_defined(
            script_to_evaluate_on_load
        ):
            params["scriptToEvaluateOnLoad"] = script_to_evaluate_on_load

        return self._send_command(
            "Page.reload",
            params
        )

    def remove_script_to_evaluate_on_load(
        self,
        identifier: ScriptIdentifier
    ):
        params = {
            ""identifier"": identifier,
        }

        return self._send_command(
            "Page.removeScriptToEvaluateOnLoad",
            params
        )

    def remove_script_to_evaluate_on_new_document(
        self,
        identifier: ScriptIdentifier
    ):
        params = {
            ""identifier"": identifier,
        }

        return self._send_command(
            "Page.removeScriptToEvaluateOnNewDocument",
            params
        )

    def screencast_frame_ack(
        self,
        session_id: int
    ):
        params = {
            ""sessionId"": session_id,
        }

        return self._send_command(
            "Page.screencastFrameAck",
            params
        )

    def search_in_resource(
        self,
        frame_id: FrameId,
        url: str,
        query: str,
        case_sensitive: bool = UNDEFINED,
        is_regex: bool = UNDEFINED
    ):
        params = {
            ""frameId"": frame_id,
            ""url"": url,
            ""query"": query,
        }

        if is_defined(
            case_sensitive
        ):
            params["caseSensitive"] = case_sensitive

        if is_defined(
            is_regex
        ):
            params["isRegex"] = is_regex

        return self._send_command(
            "Page.searchInResource",
            params
        )

    def set_ad_blocking_enabled(
        self,
        enabled: bool
    ):
        params = {
            ""enabled"": enabled,
        }

        return self._send_command(
            "Page.setAdBlockingEnabled",
            params
        )

    def set_bypass_csp(
        self,
        enabled: bool
    ):
        params = {
            ""enabled"": enabled,
        }

        return self._send_command(
            "Page.setBypassCSP",
            params
        )

    def get_permissions_policy_state(
        self,
        frame_id: FrameId
    ):
        params = {
            ""frameId"": frame_id,
        }

        return self._send_command(
            "Page.getPermissionsPolicyState",
            params
        )

    def get_origin_trials(
        self,
        frame_id: FrameId
    ):
        params = {
            ""frameId"": frame_id,
        }

        return self._send_command(
            "Page.getOriginTrials",
            params
        )

    def set_device_metrics_override(
        self,
        width: int,
        height: int,
        device_scale_factor: float,
        mobile: bool,
        scale: float = UNDEFINED,
        screen_width: int = UNDEFINED,
        screen_height: int = UNDEFINED,
        position_x: int = UNDEFINED,
        position_y: int = UNDEFINED,
        dont_set_visible_size: bool = UNDEFINED,
        screen_orientation: ScreenOrientation = UNDEFINED,
        viewport: Viewport = UNDEFINED
    ):
        params = {
            ""width"": width,
            ""height"": height,
            ""deviceScaleFactor"": device_scale_factor,
            ""mobile"": mobile,
        }

        if is_defined(
            scale
        ):
            params["scale"] = scale

        if is_defined(
            screen_width
        ):
            params["screenWidth"] = screen_width

        if is_defined(
            screen_height
        ):
            params["screenHeight"] = screen_height

        if is_defined(
            position_x
        ):
            params["positionX"] = position_x

        if is_defined(
            position_y
        ):
            params["positionY"] = position_y

        if is_defined(
            dont_set_visible_size
        ):
            params["dontSetVisibleSize"] = dont_set_visible_size

        if is_defined(
            screen_orientation
        ):
            params["screenOrientation"] = screen_orientation

        if is_defined(
            viewport
        ):
            params["viewport"] = viewport

        return self._send_command(
            "Page.setDeviceMetricsOverride",
            params
        )

    def set_device_orientation_override(
        self,
        alpha: float,
        beta: float,
        gamma: float
    ):
        params = {
            ""alpha"": alpha,
            ""beta"": beta,
            ""gamma"": gamma,
        }

        return self._send_command(
            "Page.setDeviceOrientationOverride",
            params
        )

    def set_font_families(
        self,
        font_families: FontFamilies,
        for_scripts: list = UNDEFINED
    ):
        params = {
            ""fontFamilies"": font_families,
        }

        if is_defined(
            for_scripts
        ):
            params["forScripts"] = for_scripts

        return self._send_command(
            "Page.setFontFamilies",
            params
        )

    def set_font_sizes(
        self,
        font_sizes: FontSizes
    ):
        params = {
            ""fontSizes"": font_sizes,
        }

        return self._send_command(
            "Page.setFontSizes",
            params
        )

    def set_document_content(
        self,
        frame_id: FrameId,
        html: str
    ):
        params = {
            ""frameId"": frame_id,
            ""html"": html,
        }

        return self._send_command(
            "Page.setDocumentContent",
            params
        )

    def set_download_behavior(
        self,
        behavior: str,
        download_path: str = UNDEFINED
    ):
        params = {
            ""behavior"": behavior,
        }

        if is_defined(
            download_path
        ):
            params["downloadPath"] = download_path

        return self._send_command(
            "Page.setDownloadBehavior",
            params
        )

    def set_geolocation_override(
        self,
        latitude: float = UNDEFINED,
        longitude: float = UNDEFINED,
        accuracy: float = UNDEFINED
    ):
        params = {}

        if is_defined(
            latitude
        ):
            params["latitude"] = latitude

        if is_defined(
            longitude
        ):
            params["longitude"] = longitude

        if is_defined(
            accuracy
        ):
            params["accuracy"] = accuracy

        return self._send_command(
            "Page.setGeolocationOverride",
            params
        )

    def set_lifecycle_events_enabled(
        self,
        enabled: bool
    ):
        params = {
            ""enabled"": enabled,
        }

        return self._send_command(
            "Page.setLifecycleEventsEnabled",
            params
        )

    def set_touch_emulation_enabled(
        self,
        enabled: bool,
        configuration: str = UNDEFINED
    ):
        params = {
            ""enabled"": enabled,
        }

        if is_defined(
            configuration
        ):
            params["configuration"] = configuration

        return self._send_command(
            "Page.setTouchEmulationEnabled",
            params
        )

    def start_screencast(
        self,
        format_: str = UNDEFINED,
        quality: int = UNDEFINED,
        max_width: int = UNDEFINED,
        max_height: int = UNDEFINED,
        every_nth_frame: int = UNDEFINED
    ):
        params = {}

        if is_defined(
            format
        ):
            params["format"] = format

        if is_defined(
            quality
        ):
            params["quality"] = quality

        if is_defined(
            max_width
        ):
            params["maxWidth"] = max_width

        if is_defined(
            max_height
        ):
            params["maxHeight"] = max_height

        if is_defined(
            every_nth_frame
        ):
            params["everyNthFrame"] = every_nth_frame

        return self._send_command(
            "Page.startScreencast",
            params
        )

    def stop_loading(
        self
    ):
        params = {}

        return self._send_command(
            "Page.stopLoading",
            params
        )

    def crash(
        self
    ):
        params = {}

        return self._send_command(
            "Page.crash",
            params
        )

    def close(
        self
    ):
        params = {}

        return self._send_command(
            "Page.close",
            params
        )

    def set_web_lifecycle_state(
        self,
        state: str
    ):
        params = {
            ""state"": state,
        }

        return self._send_command(
            "Page.setWebLifecycleState",
            params
        )

    def stop_screencast(
        self
    ):
        params = {}

        return self._send_command(
            "Page.stopScreencast",
            params
        )

    def produce_compilation_cache(
        self,
        scripts: list
    ):
        params = {
            ""scripts"": scripts,
        }

        return self._send_command(
            "Page.produceCompilationCache",
            params
        )

    def add_compilation_cache(
        self,
        url: str,
        data: str
    ):
        params = {
            ""url"": url,
            ""data"": data,
        }

        return self._send_command(
            "Page.addCompilationCache",
            params
        )

    def clear_compilation_cache(
        self
    ):
        params = {}

        return self._send_command(
            "Page.clearCompilationCache",
            params
        )

    def set_spc_transaction_mode(
        self,
        mode: AutoResponseMode
    ):
        params = {
            ""mode"": mode,
        }

        return self._send_command(
            "Page.setSPCTransactionMode",
            params
        )

    def set_rph_registration_mode(
        self,
        mode: AutoResponseMode
    ):
        params = {
            ""mode"": mode,
        }

        return self._send_command(
            "Page.setRPHRegistrationMode",
            params
        )

    def generate_test_report(
        self,
        message: str,
        group: str = UNDEFINED
    ):
        params = {
            ""message"": message,
        }

        if is_defined(
            group
        ):
            params["group"] = group

        return self._send_command(
            "Page.generateTestReport",
            params
        )

    def wait_for_debugger(
        self
    ):
        params = {}

        return self._send_command(
            "Page.waitForDebugger",
            params
        )

    def set_intercept_file_chooser_dialog(
        self,
        enabled: bool
    ):
        params = {
            ""enabled"": enabled,
        }

        return self._send_command(
            "Page.setInterceptFileChooserDialog",
            params
        )

    def set_prerendering_allowed(
        self,
        is_allowed: bool
    ):
        params = {
            ""isAllowed"": is_allowed,
        }

        return self._send_command(
            "Page.setPrerenderingAllowed",
            params
        )


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
from cdp.domains.page.types import (
    AddScriptToEvaluateOnLoadReturnT,
    AddScriptToEvaluateOnNewDocumentReturnT,
    AutoResponseMode,
    CaptureScreenshotReturnT,
    CaptureSnapshotReturnT,
    CreateIsolatedWorldReturnT,
    FontFamilies,
    FontSizes,
    FrameId,
    GetAdScriptIdReturnT,
    GetAppIdReturnT,
    GetAppManifestReturnT,
    GetCookiesReturnT,
    GetFrameTreeReturnT,
    GetInstallabilityErrorsReturnT,
    GetLayoutMetricsReturnT,
    GetManifestIconsReturnT,
    GetNavigationHistoryReturnT,
    GetOriginTrialsReturnT,
    GetPermissionsPolicyStateReturnT,
    GetResourceContentReturnT,
    GetResourceTreeReturnT,
    NavigateReturnT,
    PrintToPDFReturnT,
    ReferrerPolicy,
    ScriptIdentifier,
    SearchInResourceReturnT,
    TransitionType,
    Viewport
)
from cdp.domains.emulation.types import (
    ScreenOrientation
)
if TYPE_CHECKING:
    from cdp.target.connection import (
        IResult
    )


@dataclass
class Page(BaseDomain):
    def add_script_to_evaluate_on_load(
            self,
            script_source: str
    ) -> IResult['AddScriptToEvaluateOnLoadReturnT']:
        params = {
            'scriptSource': script_source,
        }

        return self._send_command(
            'Page.addScriptToEvaluateOnLoad',
            params,
            True
        )

    def add_script_to_evaluate_on_new_document(
            self,
            source: str,
            world_name: str = UNDEFINED,
            include_command_line_api: bool = UNDEFINED,
            run_immediately: bool = UNDEFINED
    ) -> IResult['AddScriptToEvaluateOnNewDocumentReturnT']:
        params = {
            'source': source,
        }

        if is_defined(world_name):
            params['worldName'] = world_name

        if is_defined(include_command_line_api):
            params['includeCommandLineAPI'] = include_command_line_api

        if is_defined(run_immediately):
            params['runImmediately'] = run_immediately

        return self._send_command(
            'Page.addScriptToEvaluateOnNewDocument',
            params,
            True
        )

    def bring_to_front(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.bringToFront',
            params,
            False
        )

    def capture_screenshot(
            self,
            format_: str = UNDEFINED,
            quality: int = UNDEFINED,
            clip: Viewport = UNDEFINED,
            from_surface: bool = UNDEFINED,
            capture_beyond_viewport: bool = UNDEFINED,
            optimize_for_speed: bool = UNDEFINED
    ) -> IResult['CaptureScreenshotReturnT']:
        params = {}

        if is_defined(format):
            params['format'] = format

        if is_defined(quality):
            params['quality'] = quality

        if is_defined(clip):
            params['clip'] = clip

        if is_defined(from_surface):
            params['fromSurface'] = from_surface

        if is_defined(capture_beyond_viewport):
            params['captureBeyondViewport'] = capture_beyond_viewport

        if is_defined(optimize_for_speed):
            params['optimizeForSpeed'] = optimize_for_speed

        return self._send_command(
            'Page.captureScreenshot',
            params,
            True
        )

    def capture_snapshot(
            self,
            format_: str = UNDEFINED
    ) -> IResult['CaptureSnapshotReturnT']:
        params = {}

        if is_defined(format):
            params['format'] = format

        return self._send_command(
            'Page.captureSnapshot',
            params,
            True
        )

    def clear_device_metrics_override(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.clearDeviceMetricsOverride',
            params,
            False
        )

    def clear_device_orientation_override(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.clearDeviceOrientationOverride',
            params,
            False
        )

    def clear_geolocation_override(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.clearGeolocationOverride',
            params,
            False
        )

    def create_isolated_world(
            self,
            frame_id: FrameId,
            world_name: str = UNDEFINED,
            grant_univeral_access: bool = UNDEFINED
    ) -> IResult['CreateIsolatedWorldReturnT']:
        params = {
            'frameId': frame_id,
        }

        if is_defined(world_name):
            params['worldName'] = world_name

        if is_defined(grant_univeral_access):
            params['grantUniveralAccess'] = grant_univeral_access

        return self._send_command(
            'Page.createIsolatedWorld',
            params,
            True
        )

    def delete_cookie(
            self,
            cookie_name: str,
            url: str
    ) -> IResult[None]:
        params = {
            'cookieName': cookie_name,
            'url': url,
        }

        return self._send_command(
            'Page.deleteCookie',
            params,
            False
        )

    def disable(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.disable',
            params,
            False
        )

    def enable(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.enable',
            params,
            False
        )

    def get_app_manifest(
            self
    ) -> IResult['GetAppManifestReturnT']:
        params = {}

        return self._send_command(
            'Page.getAppManifest',
            params,
            True
        )

    def get_installability_errors(
            self
    ) -> IResult['GetInstallabilityErrorsReturnT']:
        params = {}

        return self._send_command(
            'Page.getInstallabilityErrors',
            params,
            True
        )

    def get_manifest_icons(
            self
    ) -> IResult['GetManifestIconsReturnT']:
        params = {}

        return self._send_command(
            'Page.getManifestIcons',
            params,
            True
        )

    def get_app_id(
            self
    ) -> IResult['GetAppIdReturnT']:
        params = {}

        return self._send_command(
            'Page.getAppId',
            params,
            True
        )

    def get_ad_script_id(
            self,
            frame_id: FrameId
    ) -> IResult['GetAdScriptIdReturnT']:
        params = {
            'frameId': frame_id,
        }

        return self._send_command(
            'Page.getAdScriptId',
            params,
            True
        )

    def get_cookies(
            self
    ) -> IResult['GetCookiesReturnT']:
        params = {}

        return self._send_command(
            'Page.getCookies',
            params,
            True
        )

    def get_frame_tree(
            self
    ) -> IResult['GetFrameTreeReturnT']:
        params = {}

        return self._send_command(
            'Page.getFrameTree',
            params,
            True
        )

    def get_layout_metrics(
            self
    ) -> IResult['GetLayoutMetricsReturnT']:
        params = {}

        return self._send_command(
            'Page.getLayoutMetrics',
            params,
            True
        )

    def get_navigation_history(
            self
    ) -> IResult['GetNavigationHistoryReturnT']:
        params = {}

        return self._send_command(
            'Page.getNavigationHistory',
            params,
            True
        )

    def reset_navigation_history(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.resetNavigationHistory',
            params,
            False
        )

    def get_resource_content(
            self,
            frame_id: FrameId,
            url: str
    ) -> IResult['GetResourceContentReturnT']:
        params = {
            'frameId': frame_id,
            'url': url,
        }

        return self._send_command(
            'Page.getResourceContent',
            params,
            True
        )

    def get_resource_tree(
            self
    ) -> IResult['GetResourceTreeReturnT']:
        params = {}

        return self._send_command(
            'Page.getResourceTree',
            params,
            True
        )

    def handle_java_script_dialog(
            self,
            accept: bool,
            prompt_text: str = UNDEFINED
    ) -> IResult[None]:
        params = {
            'accept': accept,
        }

        if is_defined(prompt_text):
            params['promptText'] = prompt_text

        return self._send_command(
            'Page.handleJavaScriptDialog',
            params,
            False
        )

    def navigate(
            self,
            url: str,
            referrer: str = UNDEFINED,
            transition_type: TransitionType = UNDEFINED,
            frame_id: FrameId = UNDEFINED,
            referrer_policy: ReferrerPolicy = UNDEFINED
    ) -> IResult['NavigateReturnT']:
        params = {
            'url': url,
        }

        if is_defined(referrer):
            params['referrer'] = referrer

        if is_defined(transition_type):
            params['transitionType'] = transition_type

        if is_defined(frame_id):
            params['frameId'] = frame_id

        if is_defined(referrer_policy):
            params['referrerPolicy'] = referrer_policy

        return self._send_command(
            'Page.navigate',
            params,
            True
        )

    def navigate_to_history_entry(
            self,
            entry_id: int
    ) -> IResult[None]:
        params = {
            'entryId': entry_id,
        }

        return self._send_command(
            'Page.navigateToHistoryEntry',
            params,
            False
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
    ) -> IResult['PrintToPDFReturnT']:
        params = {}

        if is_defined(landscape):
            params['landscape'] = landscape

        if is_defined(display_header_footer):
            params['displayHeaderFooter'] = display_header_footer

        if is_defined(print_background):
            params['printBackground'] = print_background

        if is_defined(scale):
            params['scale'] = scale

        if is_defined(paper_width):
            params['paperWidth'] = paper_width

        if is_defined(paper_height):
            params['paperHeight'] = paper_height

        if is_defined(margin_top):
            params['marginTop'] = margin_top

        if is_defined(margin_bottom):
            params['marginBottom'] = margin_bottom

        if is_defined(margin_left):
            params['marginLeft'] = margin_left

        if is_defined(margin_right):
            params['marginRight'] = margin_right

        if is_defined(page_ranges):
            params['pageRanges'] = page_ranges

        if is_defined(header_template):
            params['headerTemplate'] = header_template

        if is_defined(footer_template):
            params['footerTemplate'] = footer_template

        if is_defined(prefer_css_page_size):
            params['preferCSSPageSize'] = prefer_css_page_size

        if is_defined(transfer_mode):
            params['transferMode'] = transfer_mode

        if is_defined(generate_tagged_pdf):
            params['generateTaggedPDF'] = generate_tagged_pdf

        return self._send_command(
            'Page.printToPDF',
            params,
            True
        )

    def reload(
            self,
            ignore_cache: bool = UNDEFINED,
            script_to_evaluate_on_load: str = UNDEFINED
    ) -> IResult[None]:
        params = {}

        if is_defined(ignore_cache):
            params['ignoreCache'] = ignore_cache

        if is_defined(script_to_evaluate_on_load):
            params['scriptToEvaluateOnLoad'] = script_to_evaluate_on_load

        return self._send_command(
            'Page.reload',
            params,
            False
        )

    def remove_script_to_evaluate_on_load(
            self,
            identifier: ScriptIdentifier
    ) -> IResult[None]:
        params = {
            'identifier': identifier,
        }

        return self._send_command(
            'Page.removeScriptToEvaluateOnLoad',
            params,
            False
        )

    def remove_script_to_evaluate_on_new_document(
            self,
            identifier: ScriptIdentifier
    ) -> IResult[None]:
        params = {
            'identifier': identifier,
        }

        return self._send_command(
            'Page.removeScriptToEvaluateOnNewDocument',
            params,
            False
        )

    def screencast_frame_ack(
            self,
            session_id: int
    ) -> IResult[None]:
        params = {
            'sessionId': session_id,
        }

        return self._send_command(
            'Page.screencastFrameAck',
            params,
            False
        )

    def search_in_resource(
            self,
            frame_id: FrameId,
            url: str,
            query: str,
            case_sensitive: bool = UNDEFINED,
            is_regex: bool = UNDEFINED
    ) -> IResult['SearchInResourceReturnT']:
        params = {
            'frameId': frame_id,
            'url': url,
            'query': query,
        }

        if is_defined(case_sensitive):
            params['caseSensitive'] = case_sensitive

        if is_defined(is_regex):
            params['isRegex'] = is_regex

        return self._send_command(
            'Page.searchInResource',
            params,
            True
        )

    def set_ad_blocking_enabled(
            self,
            enabled: bool
    ) -> IResult[None]:
        params = {
            'enabled': enabled,
        }

        return self._send_command(
            'Page.setAdBlockingEnabled',
            params,
            False
        )

    def set_bypass_csp(
            self,
            enabled: bool
    ) -> IResult[None]:
        params = {
            'enabled': enabled,
        }

        return self._send_command(
            'Page.setBypassCSP',
            params,
            False
        )

    def get_permissions_policy_state(
            self,
            frame_id: FrameId
    ) -> IResult['GetPermissionsPolicyStateReturnT']:
        params = {
            'frameId': frame_id,
        }

        return self._send_command(
            'Page.getPermissionsPolicyState',
            params,
            True
        )

    def get_origin_trials(
            self,
            frame_id: FrameId
    ) -> IResult['GetOriginTrialsReturnT']:
        params = {
            'frameId': frame_id,
        }

        return self._send_command(
            'Page.getOriginTrials',
            params,
            True
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
    ) -> IResult[None]:
        params = {
            'width': width,
            'height': height,
            'deviceScaleFactor': device_scale_factor,
            'mobile': mobile,
        }

        if is_defined(scale):
            params['scale'] = scale

        if is_defined(screen_width):
            params['screenWidth'] = screen_width

        if is_defined(screen_height):
            params['screenHeight'] = screen_height

        if is_defined(position_x):
            params['positionX'] = position_x

        if is_defined(position_y):
            params['positionY'] = position_y

        if is_defined(dont_set_visible_size):
            params['dontSetVisibleSize'] = dont_set_visible_size

        if is_defined(screen_orientation):
            params['screenOrientation'] = screen_orientation

        if is_defined(viewport):
            params['viewport'] = viewport

        return self._send_command(
            'Page.setDeviceMetricsOverride',
            params,
            False
        )

    def set_device_orientation_override(
            self,
            alpha: float,
            beta: float,
            gamma: float
    ) -> IResult[None]:
        params = {
            'alpha': alpha,
            'beta': beta,
            'gamma': gamma,
        }

        return self._send_command(
            'Page.setDeviceOrientationOverride',
            params,
            False
        )

    def set_font_families(
            self,
            font_families: FontFamilies,
            for_scripts: list = UNDEFINED
    ) -> IResult[None]:
        params = {
            'fontFamilies': font_families,
        }

        if is_defined(for_scripts):
            params['forScripts'] = for_scripts

        return self._send_command(
            'Page.setFontFamilies',
            params,
            False
        )

    def set_font_sizes(
            self,
            font_sizes: FontSizes
    ) -> IResult[None]:
        params = {
            'fontSizes': font_sizes,
        }

        return self._send_command(
            'Page.setFontSizes',
            params,
            False
        )

    def set_document_content(
            self,
            frame_id: FrameId,
            html: str
    ) -> IResult[None]:
        params = {
            'frameId': frame_id,
            'html': html,
        }

        return self._send_command(
            'Page.setDocumentContent',
            params,
            False
        )

    def set_download_behavior(
            self,
            behavior: str,
            download_path: str = UNDEFINED
    ) -> IResult[None]:
        params = {
            'behavior': behavior,
        }

        if is_defined(download_path):
            params['downloadPath'] = download_path

        return self._send_command(
            'Page.setDownloadBehavior',
            params,
            False
        )

    def set_geolocation_override(
            self,
            latitude: float = UNDEFINED,
            longitude: float = UNDEFINED,
            accuracy: float = UNDEFINED
    ) -> IResult[None]:
        params = {}

        if is_defined(latitude):
            params['latitude'] = latitude

        if is_defined(longitude):
            params['longitude'] = longitude

        if is_defined(accuracy):
            params['accuracy'] = accuracy

        return self._send_command(
            'Page.setGeolocationOverride',
            params,
            False
        )

    def set_lifecycle_events_enabled(
            self,
            enabled: bool
    ) -> IResult[None]:
        params = {
            'enabled': enabled,
        }

        return self._send_command(
            'Page.setLifecycleEventsEnabled',
            params,
            False
        )

    def set_touch_emulation_enabled(
            self,
            enabled: bool,
            configuration: str = UNDEFINED
    ) -> IResult[None]:
        params = {
            'enabled': enabled,
        }

        if is_defined(configuration):
            params['configuration'] = configuration

        return self._send_command(
            'Page.setTouchEmulationEnabled',
            params,
            False
        )

    def start_screencast(
            self,
            format_: str = UNDEFINED,
            quality: int = UNDEFINED,
            max_width: int = UNDEFINED,
            max_height: int = UNDEFINED,
            every_nth_frame: int = UNDEFINED
    ) -> IResult[None]:
        params = {}

        if is_defined(format):
            params['format'] = format

        if is_defined(quality):
            params['quality'] = quality

        if is_defined(max_width):
            params['maxWidth'] = max_width

        if is_defined(max_height):
            params['maxHeight'] = max_height

        if is_defined(every_nth_frame):
            params['everyNthFrame'] = every_nth_frame

        return self._send_command(
            'Page.startScreencast',
            params,
            False
        )

    def stop_loading(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.stopLoading',
            params,
            False
        )

    def crash(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.crash',
            params,
            False
        )

    def close(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.close',
            params,
            False
        )

    def set_web_lifecycle_state(
            self,
            state: str
    ) -> IResult[None]:
        params = {
            'state': state,
        }

        return self._send_command(
            'Page.setWebLifecycleState',
            params,
            False
        )

    def stop_screencast(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.stopScreencast',
            params,
            False
        )

    def produce_compilation_cache(
            self,
            scripts: list
    ) -> IResult[None]:
        params = {
            'scripts': scripts,
        }

        return self._send_command(
            'Page.produceCompilationCache',
            params,
            False
        )

    def add_compilation_cache(
            self,
            url: str,
            data: str
    ) -> IResult[None]:
        params = {
            'url': url,
            'data': data,
        }

        return self._send_command(
            'Page.addCompilationCache',
            params,
            False
        )

    def clear_compilation_cache(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.clearCompilationCache',
            params,
            False
        )

    def set_spc_transaction_mode(
            self,
            mode: AutoResponseMode
    ) -> IResult[None]:
        params = {
            'mode': mode,
        }

        return self._send_command(
            'Page.setSPCTransactionMode',
            params,
            False
        )

    def set_rph_registration_mode(
            self,
            mode: AutoResponseMode
    ) -> IResult[None]:
        params = {
            'mode': mode,
        }

        return self._send_command(
            'Page.setRPHRegistrationMode',
            params,
            False
        )

    def generate_test_report(
            self,
            message: str,
            group: str = UNDEFINED
    ) -> IResult[None]:
        params = {
            'message': message,
        }

        if is_defined(group):
            params['group'] = group

        return self._send_command(
            'Page.generateTestReport',
            params,
            False
        )

    def wait_for_debugger(
            self
    ) -> IResult[None]:
        params = {}

        return self._send_command(
            'Page.waitForDebugger',
            params,
            False
        )

    def set_intercept_file_chooser_dialog(
            self,
            enabled: bool
    ) -> IResult[None]:
        params = {
            'enabled': enabled,
        }

        return self._send_command(
            'Page.setInterceptFileChooserDialog',
            params,
            False
        )

    def set_prerendering_allowed(
            self,
            is_allowed: bool
    ) -> IResult[None]:
        params = {
            'isAllowed': is_allowed,
        }

        return self._send_command(
            'Page.setPrerenderingAllowed',
            params,
            False
        )

# -*- coding: utf-8 -*-
"""
EBONY CHRONOS: NATIVE OBS STUDIO BROADCAST BRIDGE
Classification: RESTRICTED // HVF PRIVATE ENCLAVE // LEVEL 5 CEO AUTHORITY
Contracting Entity: Humphrey Virtual Farms LLC (CAGE: 1AHA8)
System Designation: Ebony Chronos Sovereign Sentinel Platform
"""

import os
import sys
import json
import subprocess
from typing import Dict, Any, Optional

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

class ChronosOBSBridge:
    """
    Bare-metal broadcast pipeline manager.
    Injects pre-configured scene collections into OBS Studio, provisions the
    DoD Quad Chart display pipeline, and engages the OBS Virtual Camera for
    seamless, high-fidelity presentation directly inside Microsoft Teams.
    """

    def __init__(self, cage_code: str = "1AHA8", presenter: str = "CEO Jeffery Humphrey"):
        self.cage_code = cage_code
        self.presenter = presenter
        self.obs_bin = r"C:\Program Files\obs-studio\bin\64bit\obs64.exe"
        self.appdata = os.environ.get("APPDATA", "")
        self.obs_scenes_dir = os.path.join(self.appdata, "obs-studio", "basic", "scenes")
        self.scene_collection_name = "Ebony_Chronos_Studio"
        self.scene_file_path = os.path.join(self.obs_scenes_dir, f"{self.scene_collection_name}.json")

    def is_obs_installed(self) -> bool:
        return os.path.exists(self.obs_bin)

    def generate_scene_manifest(self) -> Dict[str, Any]:
        quad_chart_path = os.path.join(REPO_ROOT, "CHRONOS_DEFENSE_QUAD_CHART.html").replace("\\", "/")
        quad_chart_url = f"file:///{quad_chart_path}"

        return {
            "current_program_scene": "Scene 1: Master Briefing Deck",
            "current_scene": "Scene 1: Master Briefing Deck",
            "name": self.scene_collection_name,
            "scene_order": [
                {"name": "Scene 1: Master Briefing Deck"},
                {"name": "Scene 2: Fullscreen Defense Quad Chart"},
                {"name": "Scene 3: Fullscreen Sovereign Presenter"}
            ],
            "sources": [
                {
                    "id": "scene",
                    "name": "Scene 1: Master Briefing Deck",
                    "settings": {
                        "custom_size": False,
                        "id_counter": 2,
                        "items": [
                            {
                                "align": 5,
                                "bounds": {"x": 1920.0, "y": 1080.0},
                                "bounds_align": 0,
                                "bounds_type": 2,
                                "id": 1,
                                "locked": True,
                                "name": "DoD Quad Chart",
                                "pos": {"x": 0.0, "y": 0.0},
                                "rot": 0.0,
                                "scale": {"x": 1.0, "y": 1.0},
                                "visible": True
                            }
                        ]
                    }
                },
                {
                    "id": "scene",
                    "name": "Scene 2: Fullscreen Defense Quad Chart",
                    "settings": {
                        "custom_size": False,
                        "id_counter": 1,
                        "items": [
                            {
                                "align": 5,
                                "bounds": {"x": 1920.0, "y": 1080.0},
                                "bounds_align": 0,
                                "bounds_type": 2,
                                "id": 1,
                                "locked": True,
                                "name": "DoD Quad Chart",
                                "pos": {"x": 0.0, "y": 0.0},
                                "rot": 0.0,
                                "scale": {"x": 1.0, "y": 1.0},
                                "visible": True
                            }
                        ]
                    }
                },
                {
                    "id": "scene",
                    "name": "Scene 3: Fullscreen Sovereign Presenter",
                    "settings": {
                        "custom_size": False,
                        "id_counter": 0,
                        "items": []
                    }
                },
                {
                    "id": "browser_source",
                    "name": "DoD Quad Chart",
                    "settings": {
                        "url": quad_chart_url,
                        "width": 1920,
                        "height": 1080,
                        "fps": 60,
                        "restart_when_active": True
                    }
                }
            ]
        }

    def provision_scene_collection(self) -> str:
        """Deploys the Ebony Chronos scene manifest directly to OBS config store."""
        if not self.appdata:
            raise RuntimeError("APPDATA environment variable not resolved.")
        os.makedirs(self.obs_scenes_dir, exist_ok=True)
        manifest = self.generate_scene_manifest()
        with open(self.scene_file_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        return self.scene_file_path

    def launch_virtual_cam(self) -> Dict[str, Any]:
        """Launches OBS Studio with Virtual Camera active and scene loaded."""
        if not self.is_obs_installed():
            return {
                "status": "OBS_NOT_INSTALLED",
                "error": "OBS Studio binary not detected on bare metal."
            }
        
        self.provision_scene_collection()

        cmd = [
            self.obs_bin,
            "--collection", self.scene_collection_name,
            "--startvirtualcam",
            "--minimize-to-tray",
            "--disable-updater"
        ]

        obs_cwd = os.path.dirname(self.obs_bin)
        proc = subprocess.Popen(cmd, cwd=obs_cwd)

        return {
            "status": "VIRTUAL_CAMERA_ENGAGED",
            "obs_pid": proc.pid,
            "scene_collection": self.scene_collection_name,
            "virtual_camera": "OBS Virtual Camera (DirectShow Driver)",
            "output_target": "Microsoft Teams Camera Ingest",
            "authority": self.presenter,
            "cage_code": self.cage_code
        }

if __name__ == "__main__":
    bridge = ChronosOBSBridge()
    path = bridge.provision_scene_collection()
    print("=" * 80)
    print("  EBONY CHRONOS: OBS BROADCAST SCENE PROVISIONED")
    print(f"  * Authority: {bridge.presenter} // CAGE: {bridge.cage_code}")
    print(f"  * Scene File: {path}")
    print(f"  * OBS Binary: {bridge.obs_bin} (Found: {bridge.is_obs_installed()})")
    print("=" * 80)

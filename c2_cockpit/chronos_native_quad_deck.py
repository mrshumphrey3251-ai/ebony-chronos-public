# -*- coding: utf-8 -*-
"""
EBONY CHRONOS: NATIVE 4-WINDOW BARE-METAL C2 COMMAND DECK
Classification: RESTRICTED // HVF PRIVATE ENCLAVE // LEVEL 5 CEO AUTHORITY
Contracting Entity: Humphrey Virtual Farms LLC (CAGE: 1AHA8)
System Designation: Ebony Chronos Sovereign Sentinel Platform
"""

import os
import sys
import time
import subprocess
import ctypes
from ctypes import wintypes
from typing import Dict, Any, Optional

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from c2_cockpit.chronos_native_c2_orchestrator import ChronosNativeC2Orchestrator

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

class ChronosNativeQuadDeck:
    """
    Bare-Metal Sovereign 4-Window Desktop Command Center.
    Orchestrates real physical desktop application windows into a locked 4-quadrant layout:
      * Q1 (Top-Left)    : Microsoft Teams / Active Meeting App (Interactive click, mute, video)
      * Q2 (Bottom-Left) : Audience Broadcast Surface (DoD Quad Chart)
      * Q3 (Top-Right)   : Executive Speech Teleprompter & Port 8502 Ingress Feed
      * Q4 (Bottom-Right): Sovereign C2 Dispatch & Research Console (PowerShell CLI)
    """

    def __init__(self, cage_code: str = "1AHA8", presenter: str = "CEO Jeffery Humphrey"):
        self.cage_code = cage_code
        self.presenter = presenter
        self.orchestrator = ChronosNativeC2Orchestrator(cage_code=cage_code, presenter=presenter)
        self.geom = self.orchestrator.get_quadrant_geometry()

    def snap_console(self) -> bool:
        """Snaps the active terminal console to Quadrant 4 (Bottom-Right)."""
        hwnd = kernel32.GetConsoleWindow()
        if hwnd:
            x, y, w, h = self.geom["Q4_BOTTOM_RIGHT"]
            return self.orchestrator.tile_window(hwnd, x, y, w, h)
        return False

    def launch_and_tile_deck(self, launch_q1_browser: bool = True) -> Dict[str, Any]:
        """Spawns and snaps all 4 live interactive application surfaces on bare metal."""
        edge_x86 = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        edge_x64 = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
        edge_bin = edge_x86 if os.path.exists(edge_x86) else edge_x64

        q1 = self.geom["Q1_TOP_LEFT"]
        q2 = self.geom["Q2_BOTTOM_LEFT"]
        q3 = self.geom["Q3_TOP_RIGHT"]
        q4 = self.geom["Q4_BOTTOM_RIGHT"]

        # 1. Snap Console to Q4 (Bottom-Right)
        self.snap_console()

        # 2. Launch Q2 (Audience Broadcast Surface)
        quad_chart_url = "file:///" + os.path.join(REPO_ROOT, "CHRONOS_DEFENSE_QUAD_CHART.html").replace("\\", "/")
        subprocess.Popen([
            edge_bin,
            f"--app={quad_chart_url}",
            f"--window-position={q2[0]},{q2[1]}",
            f"--window-size={q2[2]},{q2[3]}"
        ])

        # 3. Launch Q3 (Teleprompter & Q&A HUD)
        teleprompter_url = "file:///" + os.path.join(REPO_ROOT, "c2_cockpit", "chronos_teleprompter_hud.html").replace("\\", "/")
        subprocess.Popen([
            edge_bin,
            f"--app={teleprompter_url}",
            f"--window-position={q3[0]},{q3[1]}",
            f"--window-size={q3[2]},{q3[3]}"
        ])

        # 4. Handle Q1 (Top-Left: Teams.exe or Fallback Workspace)
        teams_hwnds = self.orchestrator.find_windows_by_title("Teams")
        if teams_hwnds:
            self.orchestrator.tile_window(teams_hwnds[0], q1[0], q1[1], q1[2], q1[3])
            q1_status = "SNAPPED_EXISTING_TEAMS_APP"
        elif launch_q1_browser:
            teams_web = "https://teams.microsoft.com"
            subprocess.Popen([
                edge_bin,
                f"--app={teams_web}",
                f"--window-position={q1[0]},{q1[1]}",
                f"--window-size={q1[2]},{q1[3]}"
            ])
            q1_status = "LAUNCHED_TEAMS_WORKSPACE_WINDOW"
        else:
            q1_status = "STANDBY_WAITING_FOR_TEAMS"

        time.sleep(1.0)

        return {
            "status": "NATIVE_QUAD_DECK_ENGAGED",
            "authority": self.presenter,
            "cage_code": self.cage_code,
            "q1_teams": q1_status,
            "q2_broadcast": "TILED_BOTTOM_LEFT",
            "q3_teleprompter": "TILED_TOP_RIGHT",
            "q4_console": "TILED_BOTTOM_RIGHT",
            "quad_metrics": self.geom
        }

if __name__ == "__main__":
    deck = ChronosNativeQuadDeck()
    res = deck.launch_and_tile_deck()
    print("=" * 80)
    print("  EBONY CHRONOS: NATIVE 4-WINDOW SOVEREIGN C2 DECK ENGAGED")
    print(f"  * Authority: {res['authority']} // CAGE: {res['cage_code']}")
    print(f"  * Q1 (Top-Left)    : {res['q1_teams']}")
    print(f"  * Q2 (Bottom-Left) : {res['q2_broadcast']}")
    print(f"  * Q3 (Top-Right)   : {res['q3_teleprompter']}")
    print(f"  * Q4 (Bottom-Right): {res['q4_console']}")
    print("=" * 80)

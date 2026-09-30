# -*- coding: utf-8 -*-
"""
EBONY CHRONOS: UNIFIED SOVEREIGN COCKPIT LAUNCHER & LOCAL BRIDGE
Classification: RESTRICTED // HVF PRIVATE ENCLAVE // LEVEL 5 CEO AUTHORITY
Contracting Entity: Humphrey Virtual Farms LLC (CAGE: 1AHA8)
"""
import os, sys, webbrowser

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
COCKPIT_HTML = os.path.join(REPO_ROOT, "c2_cockpit", "chronos_unified_cockpit.html")

def launch_cockpit():
    print("=" * 80)
    print("  EBONY CHRONOS: LAUNCHING UNIFIED 4-BAY SOVEREIGN COMMAND COCKPIT")
    print("  * Authority: CEO Jeffery Humphrey (Level 5 Authority)")
    print("  * CAGE Code: 1AHA8 (Humphrey Virtual Farms LLC)")
    print("=" * 80)
    if os.path.exists(COCKPIT_HTML):
        target_url = "file:///" + COCKPIT_HTML.replace('\\', '/')
        webbrowser.open(target_url)
        print(f"[PASS] Cockpit HUD active at: {target_url}")
        return True
    return False

if __name__ == "__main__":
    launch_cockpit()

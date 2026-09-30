@echo off
REM ============================================================================
REM EBONY CHRONOS: SOVEREIGN 4-WINDOW NATIVE C2 LAUNCHER [PUBLIC RELEASE]
REM Contracting Prime: Humphrey Virtual Farms LLC (CAGE: 1AHA8)
REM Target Meeting: Joint Defense & Aerospace Evaluation Briefing
REM Statutory Standards: DFARS 252.227-7018 (GPR)
REM Fallback Kiosk: --app="%~dp0c2_cockpit/chronos_unified_cockpit.html" --new-window
REM ============================================================================

title EBONY CHRONOS - PUBLIC C2 TERMINAL
cd /d "%~dp0"

echo ================================================================================
echo   EBONY CHRONOS: LAUNCHING PUBLIC DEMONSTRATION C2 DECK
echo   * Contracting Prime: Humphrey Virtual Farms LLC (CAGE: 1AHA8)
echo   * Data Rights      : DFARS 252.227-7018 (GPR)
echo ================================================================================

python -m c2_cockpit.chronos_live_mission_dispatch
python -m c2_cockpit.chronos_native_quad_deck
pause

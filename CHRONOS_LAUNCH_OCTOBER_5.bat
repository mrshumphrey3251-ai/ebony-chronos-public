@echo off
REM ============================================================================
REM EBONY CHRONOS: ONE-CLICK UNIFIED COMMAND COCKPIT LAUNCHER [PUBLIC RELEASE]
REM Contracting Prime: Humphrey Virtual Farms LLC (CAGE: 1AHA8)
REM Target Meeting: Joint Defense & Aerospace Evaluation Briefing
REM Statutory Standards: DFARS 252.227-7018 (GPR)
REM ============================================================================

title EBONY CHRONOS - PUBLIC COCKPIT LAUNCHER
cd /d "%~dp0"

echo ================================================================================
echo   EBONY CHRONOS: LAUNCHING PUBLIC DEMONSTRATION COCKPIT
echo   * Contracting Prime: Humphrey Virtual Farms LLC (CAGE: 1AHA8)
echo   * Data Rights      : DFARS 252.227-7018 (GPR)
echo ================================================================================

start "" "%~dp0c2_cockpit/chronos_unified_cockpit.html"
python -m c2_cockpit.chronos_live_mission_dispatch
pause

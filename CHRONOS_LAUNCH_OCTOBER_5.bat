@echo off
REM ============================================================================
REM EBONY CHRONOS: ONE-CLICK MISSION DEMONSTRATION LAUNCHER [PUBLIC RELEASE]
REM Contracting Prime: Humphrey Virtual Farms LLC (CAGE: 1AHA8)
REM Target Meeting: Joint Defense & Aerospace Evaluation Briefing
REM Statutory Standards: DFARS 252.227-7018 (GPR)
REM ============================================================================

title EBONY CHRONOS - PUBLIC DEMONSTRATION LAUNCHER
cd /d "%~dp0"

echo ================================================================================
echo   EBONY CHRONOS: PUBLIC DEMONSTRATION SUITE LAUNCHER
echo   * Contracting Prime: Humphrey Virtual Farms LLC (CAGE: 1AHA8)
echo   * Data Rights      : DFARS 252.227-7018 (GPR)
echo ================================================================================

start "" "CHRONOS_DEFENSE_QUAD_CHART.html"
python -m c2_cockpit.chronos_live_mission_dispatch
pause

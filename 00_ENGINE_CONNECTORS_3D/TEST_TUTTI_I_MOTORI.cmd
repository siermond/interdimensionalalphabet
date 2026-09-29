@echo off
chcp 65001 >nul 2>&1
title DIAGNOSTICA COMPLETA CONNETTORI 3D (BLENDER - UNITY - UNREAL - NEXUS)
color 0F

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0verifica_motori.ps1"

pause

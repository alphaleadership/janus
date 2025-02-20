@echo off
setlocal
title Applio
echo rmdir /S /q zluda
curl -s -L https://github.com/lshqqytiger/ZLUDA/releases/download/rel.c0804ca624963aab420cb418412b1c7fbae3454b/ZLUDA-windows-rocm6-amd64.zip > zluda.zip
tar -xf zluda.zip

set HIP_VISIBLE_DEVICES="0"
set ZLUDA_COMGR_LOG_LEVEL=5
zluda\zluda.exe -- python.exe test_sample.py 
echo.
pause
@echo off

cd %~dp0

for %%i in (%1\*) do batch_render %%i

@pause
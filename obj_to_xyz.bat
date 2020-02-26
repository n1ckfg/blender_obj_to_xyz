@echo off

rem https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html

cd %~dp0
"C:\Program Files\blender\blender" --background template.blend --python batch_render.py -o //render/%~nx1#.exr -a -- %1  

rem @pause
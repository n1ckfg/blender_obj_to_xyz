import bpy
import sys

bpy.ops.wm.addon_enable(module="latk_blender")
from latk_blender import *

def main():
    latk_settings=bpy.context.scene.latk_settings

    argv = sys.argv
    argv = argv[argv.index("--") + 1:] # get all args after "--"
    filepath = argv[0]

    readBrushStrokes(filepath=filepath, resizeTimeline=False)
    goToFrame(4)
    gpMesh(_singleFrame=True, _animateFrames=False, _thickness=latk_settings.thickness, _remesh=latk_settings.remesh_mode.lower(), _resolution=latk_settings.resolution, _bevelResolution=latk_settings.bevelResolution, _decimate=latk_settings.decimate, _bakeMesh=latk_settings.bakeMesh, _joinMesh=True, _saveLayers=False, _vertexColorName=latk_settings.vertexColorName, _useHull=False)

    temp = filepath.split(".")
    saveFile(temp[0] + ".blend", format=False)
    projectAllToCamera(usePixelCoords=True, discardDepth=True)
    writeBrushStrokes(filepath=temp[0] + "_flat.json")

if __name__ == '__main__':
    main()
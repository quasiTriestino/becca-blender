"""Default properties."""

import bpy


class becca_props(bpy.types.PropertyGroup):
    """khblend default property group."""

    cell_dir: bpy.props.StringProperty(

        name='',
        subtype='FILE_PATH',
        default='Enter dae directory'

    )

    cell_class: bpy.props.StringProperty(

        name='',
        default='Enter cell class'

    )
    

classes = [
    becca_props
]

def register():

    # Register classes
    for cls in classes:
        bpy.utils.register_class(cls)

    # Assign property groups
    bpy.types.Scene.becca_props = bpy.props.PointerProperty(type=becca_props)


def unregister():

    # Unregister classes
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # Delete property groups
    del bpy.types.Scene.becca_props

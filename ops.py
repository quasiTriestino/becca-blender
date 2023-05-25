import bpy
from . import scripts

class importCells(bpy.types.Operator):
    """Import cells."""

    bl_label = 'Import'
    bl_idname = 'becca.cell_import'

    @classmethod
    def poll(cls, context):
        """Restrict class to 3D viewport."""
        return(context.area.type == 'VIEW_3D')

    def execute(self, context):
        """Execute operation."""

        directory = bpy.context.scene.becca_props.cell_dir
        scripts.CellsImport.run(directory)
        
        print("Cells imported")
        return {'FINISHED'}


class importCellsNames(bpy.types.Operator):
    """Import cells with names."""

    bl_label = 'Import with names'
    bl_idname = 'becca.cell_import_names'

    @classmethod
    def poll(cls, context):
        """Restrict class to 3D viewport."""
        return(context.area.type == 'VIEW_3D')

    def execute(self, context):
        """Execute operation."""

        directory = bpy.context.scene.becca_props.cell_dir
        scripts.CellsImport_wNames.run(directory)
        
        print("Cells imported with names")
        return {'FINISHED'}


class createClassCollection(bpy.types.Operator):
    """Create cell class collection."""

    bl_label = 'Import'
    bl_idname = 'becca.create_class_collection'

    @classmethod
    def poll(cls, context):
        """Restrict class to 3D viewport."""
        return(context.area.type == 'VIEW_3D')

    def execute(self, context):
        """Execute operation."""

        directory = bpy.context.scene.becca_props.cell_class
        scripts.ClassCollectorCreator.run(directory)
        
        print("Class created.")
        return {'FINISHED'}


class moveClass(bpy.types.Operator):
    """Create cell class collection."""

    bl_label = 'Move'
    bl_idname = 'becca.move_class'

    @classmethod
    def poll(cls, context):
        """Restrict class to 3D viewport."""
        return(context.area.type == 'VIEW_3D')

    def execute(self, context):
        """Execute operation."""

        directory = bpy.context.scene.becca_props.cell_class
        scripts.MoveClass.run(directory)
        
        print("Class moved.")
        return {'FINISHED'}


classes = [
    importCells,
    importCellsNames,
    createClassCollection,
    moveClass
]

def register():
    """Register classes."""

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    """Unregister classes."""

    for cls in classes:
        bpy.utils.unregister_class(cls)

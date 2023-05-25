"""Scene panel."""


import bpy


class VIEW3D_PT_Cells(bpy.types.Panel):
    """Scene panel."""

    bl_label = 'Cells'
    bl_idname = 'KHBLEND_PT_Cells'
    bl_space_type = 'VIEW_3D'  # space where panel will be used
    bl_region_type = 'UI'  # region where panel will be used
    bl_category = 'Becca'  # tab where panel will be displayed
    bl_description = 'Becca blender'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        """Create panel."""

        props = bpy.context.scene.becca_props
        
        box = self.layout.box()
        col = box.column()
        col.label(text='Import cells')
        col.prop(props, 'cell_dir')
        col.operator('becca.cell_import')
        col.operator('becca.cell_import_names')
        col.label(text='Colections')
        col.prop(props, 'cell_class')
        row = col.row()
        row.operator('becca.create_class_collection')
        row.operator('becca.move_class')
        

classes = [
    
    VIEW3D_PT_Cells
    
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

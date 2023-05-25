bl_info = {
    'name': 'Becca Blend',
    'author': 'Becca Pfeiffer',
    'version': (0, 0),
    'blender': (3, 6, 0),
    'location': 'View3D > Tool panel',
    'description': 'Blend the Becca!',
    'wiki_url': '',
    'category': 'Scientific'
}

from . import ops
from . import props
from . import ui

from importlib import reload

reload(ops)
reload(props)
reload(ui)


def register():
    """Run on enable."""
    props.register()
    ops.register()
    ui.register()


def unregister():
    """Run on disable."""
    props.unregister()
    ops.unregister()
    ui.unregister()


# Only necessary if running from editor (not if running as addon)
if __name__ == '__main__':
    register()


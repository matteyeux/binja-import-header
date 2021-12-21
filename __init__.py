from binaryninja import *

def import_header(binaryview):
    """Import content from C header file to types."""
    header = OpenFileNameField("Import header file (.h)")
    form_input = get_form_input([header], "")

    if form_input is False:
        return -1

    if header.result == '':
        print("[i] No file selected")
        return -1

    types = binaryview.platform.parse_types_from_source_file(header.result)

    for name, _type in types.types.items():
        binaryview.define_user_type(name, _type)

PluginCommand.register("Import header file", "Import C header file (.h) to types", import_header)

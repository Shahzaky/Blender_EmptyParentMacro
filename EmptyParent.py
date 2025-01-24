# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <https://www.gnu.org/licenses/>.

import bpy

bl_info = {
    "name": "Empty Parent Macro",
    "blender": (4, 2, 0),
    "category": "Object",
}

class OBJECT_OT_empty_parent_macro(bpy.types.Operator):
    bl_idname = "object.empty_parent_macro"
    bl_label = "Empty Parent Macro"
    bl_description = ("Create an empty object, parent the active object to it, and rename the empty to match the active object.")
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if not context.selected_objects:
            self.report({'WARNING'}, "No objects selected.")
            return {'CANCELLED'}

        active_object = context.view_layer.objects.active

        if not active_object:
            self.report({'WARNING'}, "No active object.")
            return {'CANCELLED'}

        empty = bpy.data.objects.new(f"{active_object.name}_empty", None)
        empty.location = active_object.location

        context.collection.objects.link(empty)

        active_object.parent = empty

        empty.name = active_object.name

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_empty_parent_macro.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_empty_parent_macro)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_empty_parent_macro)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
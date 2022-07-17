"""

Use python & opengl(or moderngl) shader realizes reading an image to extract the domain colors 
(including the position coordinates of the picture,

The general idea is to use the glsl shader to implement a bar noise grayscale image (refer to the image below). Then, by accepting the color information passed in by python, it is processed to form the final output image. Please be sure to use the shader nor just python to process the image, because the related shader will need to be modified later.

"""

# file structure:
# main.py
# vertex_shader.glsl
# fragment_shader.glsl

import resource
import moderngl_window as mglw
import pyglet
import pyglet.window.key

# # width of window
# width = 1600
 
# # height of window
# height = 900
# window = pyglet.window.Window(width, height)
# window_size = 1600, 900

class MyWindow(mglw.WindowConfig):
    window_size = 1600, 900
    resource_dir = "resources"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prog = self.ctx.program(
            vertex_shader=self.load_program("vertex_shader.glsl"),
            fragment_shader=self.load_program("fragment_shader.glsl"),
        )
        self.vbo = self.ctx.buffer(reserve=4 * 4 * 4)
        self.vbo.bind_to_buffer(self.prog["a_position"])
        self.vbo.write(self.vbo_data)
        self.vao = self.ctx.simple_vertex_array(self.prog, self.vbo, "a_position")

    def render(self, time, frame_time):
        self.ctx.clear(1.0, 1.0, 1.0, 1.0)
        self.vao.render()

    def on_resize(self, width, height):
        self.prog["u_size"] = width, height

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.vbo_data[:] = x, y, x + dx, y + dy
        self.vbo.write(self.vbo_data)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.vbo_data[:] = x, y, x + scroll_x, y + scroll_y
        self.vbo.write(self.vbo_data)

    def on_key_press(self, key, modifiers):
        if key == mglw.keys.ESCAPE:
            self.close()


if __name__ == "__main__":
    # pyglet.app.run()
    mglw.run_window_config(MyWindow)



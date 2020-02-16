import bpy
import numpy as np

class Util:
    """generate location utility class"""
    @staticmethod
    def default():
        return (0, 0, 0)

    @staticmethod
    def random_space(min, max):
        return (max - min) * np.random.rand(3) + min

    @staticmethod
    def radian_list(num):
        return np.linspace(0, 2 * np.pi, num)

    @staticmethod
    def circle_x_list(num, r=1):
        radian_list = Util.radian_list(num)
        return [r * np.cos(i) for i in radian_list]

    @staticmethod
    def circle_y_list(num, r=1):
        radian_list = Util.radian_list(num)
        return [r * np.sin(i) for i in radian_list]

    @staticmethod
    def loop_radian_list(num, loop_count):
        return np.linspace(0, 2 * np.pi * loop_count, num)

    @staticmethod
    def loop_circle_x_list(num, loop_count, r=1):
        radian_list = Util.loop_radian_list(num, loop_count)
        return [r * np.cos(i) for i in radian_list]

    @staticmethod
    def loop_circle_y_list(num, loop_count, r=1):
        radian_list = Util.loop_radian_list(num, loop_count)
        return [r * np.sin(i) for i in radian_list]

    @staticmethod
    def height_uniformity_list(num, height):
        return [height for i in range(num)]

    @staticmethod
    def height_wave_list(num, frequency, amp):
        return [amp * np.sin(frequency * i) for i in Util.radian_list(num)]

class Location:
    @staticmethod
    def circlar(num, r=1, height=0):
        return zip(Util.circle_x_list(num, r),
                   Util.circle_y_list(num, r),
                   Util.height_uniformity_list(num))

    @staticmethod
    def wave_circlar(num, r, frequency=8, amp=1):
        return zip(Util.circle_x_list(num, r),
                   Util.circle_y_list(num, r),
                   Util.height_wave_list(num, frequency, amp))

    @staticmethod
    def spiral(num, bottom, top, loop_count, r=1):
        height_list = np.linspace(bottom, top, num)
        return zip(Util.loop_circle_x_list(num, loop_count, r),
                   Util.loop_circle_y_list(num, loop_count, r),
                   height_list)

class Rotation:
    """generate rotation utility class"""
    @staticmethod
    def default():
        return (0, 0, 0)

    @staticmethod
    def random():
        return 360 * np.random.rand(3)


class Generate:
    """generat 3d models utility class"""
    @staticmethod
    def generate_model(location, rotation, generate_func):
        generata_func(location=location, rotation=rotation)

    @staticmethod
    def random_cube(min, max):
        random_location = Location.random_space(min, max)
        default_rotation = Rotation.default()
        generate_model(location=random_location, rotation=default_rotation, generate_func=bpy.ops.mesh.primitive_cube_add)

    @staticmethod
    def random_ico_sphere(min, max):
        random_location = Location.random_space(min, max)
        default_rotation = Rotation.default()
        random_division = np.random.randint(0, 3)
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=random_division, location=random_location, rotaion=default_rotation)

    @staticmethod
    def random_torus(min, max):
        random_location = Location.random_space(min, max)
        bpy.ops.mesh.primitive_torus_add(location=random_location)

    @staticmethod
    def random_rotate_cubes(min, max, num):
        for i in range(num):
            generate_random_cube(min, max)
            bpy.context.object.rotation_euler = Rotation.random()

    @staticmethod
    def random_rotate_torus(min, max, num):
        for i in range(num):
            random_torus(min, max)
            random_rotation = Rotation.random()
            bpy.context.object.rotation_euler = random_rotation

    @staticmethod
    def random_cubes(min, max, num):
        for i in range(num):
            random_cube(min, max)

    @staticmethod
    def generate_random_ico_spheres(min, max, num):
        for i in range(num):
            random_ico_sphere(min, max)
            bpy.context.object.rotation_euler = Rotation.random()

    @staticmethod
    def circlar_cubes(num, r, z):
        size = r / num / 10
        location_list = Location.circlar(num, r, z)
        for location in location_list:
            bpy.ops.mesh.primitive_cube_add(location=location, size=size)

    @staticmethod
    def sin_circlar_cubes(num, r=1, frequency=8, amp=1, size=0.1):
        location_list = Location.wave_circlar(num, r, frequency, amp)
        for location in location_list:
            bpy.ops.mesh.primitive_cube_add(location=location, size=size)

    @staticmethod
    def sin_circlar_ico_spheres(num, r=1, frequency=8, amp=1, size=0.1):
        location_list = Location.wave_circar(num, r, frequency, amp)
        for location in location_list:
            random_division = np.random.randint(0, 3)
            bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=random_division, location=location, radius=size)

    @staticmethod
    def spiral_staircase(num, r, min, max, loop_count, size=0.1, z_scale=0.4):
        location_list = Location.spiral(num, r, min, max, loop_count)
        for location in location_list:
            bpy.ops.mesh.primitive_cube_add(location=location, size=size)
            bpy.context.object.scale[2] = z_scale

# Example of generate 3D models
class Example:
    def generate_wave_ring_cube():
        Generate.sin_circlar_cubes(num=80, r=8, frequency=8, amp=1, size=1)

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("triangle_boi_v8.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "triangle_program",
    options = options,
    version = "8.0",
    description = 'triangle stuff',
    executables = executables
)
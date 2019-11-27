from cx_Freeze import setup, Executable

setup(name = "Pollos copacabana",
    version = "0.1",
    description = "menu pollos copacabana",
    executables = [Executable("navegador.py"),])
import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Tetris",
    options={"build_exe":{"packages":["pygame", "settings", "tetriminos", "board", "draw", "game", "assets", "os"],
                          "include_files":["C:\\Users\\weich\\Desktop\\Coding Projects\\Tetris\\img","C:\\Users\\weich\\Desktop\\Coding Projects\\Tetris\\audio_src"]}},

    executables=executables
)

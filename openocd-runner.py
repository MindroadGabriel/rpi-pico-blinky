import os
import sys

program = f'-c "program {sys.argv[1]} verify reset"'

# interface = "interface/picoprobe.cfg"
# target = "target/rp2040.cfg"
# cmd = f'-f {interface} -f {target} {program}'

board = "board/pico-debug.cfg"
cmd = f'-f {board} {program}'

os.system(f'openocd {cmd}')  # execute openocd
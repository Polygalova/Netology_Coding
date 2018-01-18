import subprocess
import os


def resize():
    source = 'Source'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    result = 'Result'
    if os.path.exists(os.path.join(current_dir, result)) is False:
        os.mkdir(os.path.join(current_dir, result))
    for root, dirs, files in os.walk(os.path.join(current_dir, source)):
        for filename in files:
            pic_in = os.path.join(current_dir, source, filename)
            pic_out = os.path.join(current_dir, result, filename)
            with open(pic_out, 'w') as f:
                f.write(pic_in)
            subprocess.run(['convert.exe', pic_in, '-resize', '200', pic_out])


resize()

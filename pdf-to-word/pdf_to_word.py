import os
import subprocess

for top, dirs, files in os.walk(r'C:\Users\tmccl\OneDrive\Documents\GitHub\fun-projects\pdf-to-word'):
    for filename in files:
        if filename.endswith('.pdf'):
            abspath = os.path.join(top, filename)
            subprocess.call('lowriter --invisible --convert-to doc "test.pdf"'
                            .format(abspath), shell=True)
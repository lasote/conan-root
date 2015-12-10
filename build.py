import os
import platform
import sys

if __name__ == "__main__":
    os.system('conan export lasote/testing')
   
    def test(settings):
        argv =  " ".join(sys.argv[1:])
        command = "conan test %s %s" % (settings, argv)
        retcode = os.system(command)
        if retcode != 0:
            exit("Error while executing:\n\t %s" % command)

    compiler = " "
    if platform.system() == "Windows":
        compiler = '-s compiler="Visual Studio" -s compiler.version=12 '
        test(compiler + '-s build_type=Release -s arch=x86')
        test(compiler + '-s build_type=Debug -s arch=x86')
        
        compiler = '-s compiler="Visual Studio" -s compiler.version=10 '
        test(compiler + '-s build_type=Release -s arch=x86')
        test(compiler + '-s build_type=Debug -s arch=x86')
    else:
        # x86_64
        test(compiler + '-s build_type=Release -s arch=x86_64')

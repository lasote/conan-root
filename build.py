import os
import platform
import sys

if __name__ == "__main__":
    os.system('conan export lasote/stable')
   
    def test(settings):
        argv =  " ".join(sys.argv[1:])
        command = "conan test %s %s" % (settings, argv)
        retcode = os.system(command)
        if retcode != 0:
            exit("Error while executing:\n\t %s" % command)

    compiler = " "

    # x86_64
    test(compiler + '-s build_type=Release -s arch=x86_64 -o root:shared=False')
    #test(compiler + '-s build_type=Debug -s arch=x86_64 -o root:shared=False')
   
    #test(compiler + '-s build_type=Debug -s arch=x86_64 -o root:shared=True')
    test(compiler + '-s build_type=Release -s arch=x86_64 -o root:shared=True')

    # x86
    #test(compiler + '-s build_type=Debug -s arch=x86 -o root:shared=False')
    test(compiler + '-s build_type=Release -s arch=x86 -o root:shared=False')
    
    #test(compiler + '-s build_type=Debug -s arch=x86 -o root:shared=True')
    test(compiler + '-s build_type=Release -s arch=x86 -o root:shared=True')

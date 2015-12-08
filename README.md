# conan-root

[Conan.io](https://conan.io) package for [Root CERN](https://root.cern.ch) framework

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/root/6.04.12/lasote/stable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.
    
## Upload packages to server

    $ conan upload root/6.04.12@lasote/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install root/6.04.12@lasote/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    root/6.04.12@lasote/stable

    [options]
    root:shared=True # False
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

# conan-root

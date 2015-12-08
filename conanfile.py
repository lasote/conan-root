from conans import ConanFile
from conans.tools import download, unzip
import os
import shutil
from conans import CMake

class CernRootConan(ConanFile):
    name = "root"
    version = "6.04.12"
    folder = "root-%s" % version
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    exports = "CMakeLists.txt"
    generators = "cmake"
    url="http://github.com/lasote/conan-root"    

    def config(self):
        pass
    
    def source(self):
        
        zip_name = "root_v%s.source.tar.gz" % self.version
        download("https://root.cern.ch/download/%s" % zip_name, zip_name)
        unzip(zip_name)
        os.unlink(zip_name)
        shutil.move("%s/CMakeLists.txt" % self.folder, "%s/CMakeListsOriginal.cmake" % self.folder)
        shutil.move("CMakeLists.txt", "%s/CMakeLists.txt" % self.folder)

    def build(self):
        """ https://root.cern.ch/building-root
            https://root.cern.ch/build-prerequisites """
        cmake = CMake(self.settings)
         # Build
        if self.settings.os == "Macos":
            self.output.warn("Detected OSX. Please execute:  'xcode-select --install' if your build fails in configure")
        self.run("cd %s &&  mkdir _build" % self.folder)
        configure_command = 'cd %s/_build && cmake .. %s' % (self.folder, cmake.command_line)
        self.output.warn("Configure with: %s" % configure_command)
        self.run(configure_command)
        self.run("cd %s/_build && cmake --build . %s" % (self.folder, cmake.build_config))

    def package(self):
        """ Define your conan structure: headers, libs and data. After building your
            project, this method is called to create a defined structure:
        """
        # Tools
        self.copy(pattern="*", dst="bin", src="%s/_build/bin" % self.folder, keep_path=False)
        
        # Icons
        self.copy(pattern="*", dst="icons", src="%s/_build/icons" % self.folder, keep_path=True)
        
        # Fonts
        self.copy(pattern="*", dst="fonts", src="%s/_build/fonts" % self.folder, keep_path=True)
        
        # etc
        self.copy(pattern="*", dst="etc", src="%s/_build/etc" % self.folder, keep_path=True)
        
        # Headers
        self.copy(pattern="*.h", dst="include", src="%s/_build/include" % self.folder, keep_path=True)
        
        # Win
        self.copy(pattern="*.dll", dst="bin", src="%s/_build/" % self.folder, keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="%s/_build/" % self.folder, keep_path=False)
        
        # UNIX

        if not self.options.shared:
            self.copy(pattern="*.a", dst="lib", src="%s/_build/lib/" % self.folder, keep_path=False)   
        else:
            self.copy(pattern="*.so*", dst="lib", src="%s/_build/lib/" % self.folder, keep_path=False)
            self.copy(pattern="*.dylib*", dst="lib", src="%s/_build/lib/" % self.folder, keep_path=False)

    def package_info(self):  
        
#         self.cpp_info.libs = ["ASImage", "ASImageGui", "Cling", "complexDict", "Core", "dequeDict", "EG", "Eve",
#                               "FitPanel", "Foam", "forward_listDict", "FTGL", "Fumili", "Ged", "Genetic", "GenVector", 
#                               "Geom", "GeomBuilder", "GeomPainter", "GLEW", "Gpad", "Graf", "Graf3d", "Gui", "GuiBld",
#                               "GuiHtml", "Gviz3d", "GX11", "GX11TTF", "Hist", "HistPainter", "Html", "listDict", "map2Dict", 
#                               "mapDict", "MathCore", "Matrix", "MemStat", "Minuit", "MLP", "multimap2Dict", "multimapDict", 
#                               "multisetDict", "Net", "New", "Physics", "Postscript", "Proof", "ProofBench", "ProofDraw", 
#                               "ProofPlayer", "PyROOT", "Quadp", "Recorder", "RGL", "Rint", "RIO", "RootAuth", "RPgSQL",
#                               "SessionViewer", "setDict", "Smatrix", "Spectrum", "SpectrumPainter", "SPlot", "SQLIO", 
#                               "SrvAuth", "Thread", "TMVA", "TMVAGui", "Tree", "TreePlayer", "TreeViewer", "unordered_mapDict", 
#                               "unordered_multimapDict", "unordered_multisetDict", "unordered_setDict", "valarrayDict", 
#                               "vectorDict", "VMC", "X3d", "XMLIO", "XMLParser"]
#         
        # ./root-config --cflags --glibs
        self.cpp_info.libs = ["Gui", "Core", "RIO", "Net", "Hist", "Graf", "Graf3d", "Gpad", 
                              "Tree", "Rint", "Postscript", "Matrix", "Physics", "MathCore", "Thread"]
        if self.settings.os == "Linux":
            self.cpp_info.libs.extend(["m", "dl"])
            self.cpp_info.cppflags.extend(["-std=c++11", "-pthread", "-rdynamic"]) 

        elif self.settings.os == "Macos":
            self.cpp_info.libs.extend(["m", "dl", "pthread"])
            self.cpp_info.cppflags.extend(["-pthread", "-stdlib=libc++", "-std=c++11"])

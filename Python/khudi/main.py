#!/usr/bin/env python
""" generated source for module main """
from __future__ import print_function
# package: khudi
import time
from khudi.World import World

from khudi.define import def_


class main(object):
    """ generated source for class main """
    @classmethod
    def main(cls, argv):
        """ generated source for method main """
        try:
            world = World()
            if len(argv):
                print("Scene file: " + argv[0])
                print("Images dir: " + argv[1])
                if world.Build(argv[0]) == 0:
                    if def_.__NO_ANIMATION__:
                        filename = argv[1] + "/test.tga"
                        world.RenderScene(filename)
                    else:
                        # 
                        #  TIMING
                        # 
                        time_start = time.time()
                        world.RenderAnimation(argv[1])
                        # 
                        #  TIMING
                        # 
                        time_end = time.time()
                        print((time_end - time_start) / 1000000)
                    print("Finished Rendering images")
            else:
                print("Error reading the scene file or images dir")
        except Exception as e:
            print("Error in the main program")
            e.printStackTrace()


if __name__ == '__main__':
    import sys
    main.main(sys.argv)


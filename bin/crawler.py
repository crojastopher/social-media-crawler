#!/usr/bin/python
'''
Copyright 2010-2013 DIMA Research Group, TU Berlin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
 
Created on Oct 7, 2011

@author: Alexander Alexandrov <alexander.alexandrov@tu-berlin.de>
'''

import sys, os

# append ./lib/python to path 
try:
    fileName = os.readlink(__file__)
except:
    fileName = __file__
    
basePath = os.path.dirname(os.path.dirname((os.path.abspath(fileName))))
sys.path.append("%s/src/python" % (basePath))

for name in os.listdir("%s/vendor" % (basePath)):
    if os.path.isdir(os.path.join("%s/vendor" % (basePath), name)):
        sys.path.append(os.path.join("%s/vendor" % (basePath), name))

from eu.stratosphere.frontend import Frontend

def main(*args):
    try:
        # run script
        pass
        frontend = Frontend(os.path.abspath(basePath), os.path.basename(fileName), sys.argv[1:])
        frontend.run()
    except:
        return 1 # something went wrong
    else:
        return 0 # exit normally
 
if __name__ == '__main__':
    sys.exit(main(*sys.argv))


#-----------------------------------------------------------------------------
#  Copyright (c) 2013, Daniel Stouffer. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#    o Redistributions of source code must retain the above copyright notice,
#      this list of conditions, and the disclaimer that follows.
#
#    o Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions, and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    o Neither the name of the copyright holders nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
#-----------------------------------------------------------------------------

__all__ = [
    'axis',
    'colors',
    'dataset',
    'drawing_objects',
    'fonts',
    'grace',
    'graph',
    'parser',
	]
 
from . import axis
from . import colors
from . import dataset
from . import drawing_objects
from . import fonts
from . import graph
from . import parser
 
# dealing with backward compatibility
if __name__ == 'PyGrace':
       # backward compatibility for PyGrace
       from PyGrace import grace
       try: del plot
       except: pass
       try: del project
       except: pass
 
elif __name__ == 'pygrace':
       __all__.append('project')
       __all__.append('interactive')

       from . import project
       from . import interactive

       # backward compatibility for pygrace
       def grace(*args, **kwds):
               from pygrace import interactive
               return interactive.session()
       grace.__doc__ = interactive.session.__doc__

# EOF

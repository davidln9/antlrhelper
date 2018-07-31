This project will take an ANTLR generated listener in Python and insert eventTrace statements for
debugging with.

This project assumes the listener file was created by ANTLR 4.x and that no other
code has been added since the automatically generated listener was created.
This project is 100% open source and is meant to be modified to suit any purpose.

creates __init__(self, trace, log) as well as if eventTraceEnabled: self._log.write()
This project depends on the creation of a file in write mode to be passed in 
during creation of the object.

sample:

log = open("logfile.txt", "w")
eventTrace = 1
listener = SampleListener(log, eventTrace)

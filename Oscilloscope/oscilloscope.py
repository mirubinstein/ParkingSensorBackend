#!/usr/bin/env python

import sys
import tos
import datetime
from xml.dom.minidom import Document

AM_OSCILLOSCOPE = 0x93
data = {}

class OscilloscopeMsg(tos.Packet):
    def __init__(self, packet = None):
        tos.Packet.__init__(self,
                            [('version',  'int', 2),
                             ('interval', 'int', 2),
                             ('id',       'int', 2),
                             ('count',    'int', 2),
                             ('readings', 'blob', None)],
                            packet)
if '-h' in sys.argv:
    print "Usage:", sys.argv[0], "serial@/dev/ttyUSB0:57600"
    sys.exit()

am = tos.AM()

def writeXML():
	doc = Document()
	readings = doc.createElement("readings")
	doc.appendChild(readings)

	for nodes in data:
		node = doc.createElement("node")
		node.setAttribute("id",nodes)
		for read in data[nodes]:
			reading = doc.createElement("reading")
			reading.setAttribute("time",read[0])
			payload = doc.createTextNode(read[1])
			reading.appendChild(payload)
			node.appendChild(reading)
		readings.appendChild(node)

	f = open("data.xml","w")
	try:
		f.write(doc.toprettyxml(indent="	"))
	finally:
		f.close()
	print "XML File Written"

while True:
    p = am.read()
    if p and p.type == AM_OSCILLOSCOPE:
        msg = OscilloscopeMsg(p.data)
        #print msg.id, msg.count, [i<<8 | j for (i,j) in zip(msg.readings[::2], msg.readings[1::2])]
        #print msg.id, str(value)

	total = 0
	dataReadings = [i<<8 | j for (i,j) in zip(msg.readings[::2], msg.readings[1::2])]
	for reading in dataReadings:
		total += int(str(reading),16)
	value = total / len(dataReadings)
	#value = int(str(msg.readings[len(msg.readings)-1]),16)
	time = datetime.datetime.now()
	timeString = time.strftime("%Y-%m-%d %H:%M:%S")
	if str(msg.id) in data:
		data[str(msg.id)].insert(0,(timeString,str(value)))
	else:
		data[str(msg.id)] = [(timeString,str(value))]
	
	print "Data received from node:",str(msg.id),"with value:",str(value),"at time:",timeString
	writeXML()


PYTHONPATH=$PYTHONPATH:$TOSROOT/support/sdk/python

COMPONENT=OscilloscopeAppC
SENSORBOARD=mts300
BUILD_EXTRA_DEPS = MyMsg.py

MyMsg.py: Oscilloscope.h
	mig python -target=$(PLATFORM) $(CFLAGS) -python-classname=MyMsg Oscilloscope.h oscilloscope -o $@

include $(MAKERULES)


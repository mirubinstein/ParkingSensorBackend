MyMsg.py: Oscilloscope.h
	mig python -target=$(PLATFORM) $(CFLAGS) -python-classname=MyMsg Oscilloscope.h oscilloscope -o $@

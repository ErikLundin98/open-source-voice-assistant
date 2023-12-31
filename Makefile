DYLIB_FILES = libespeak-ng.1.dylib libpiper_phonemize.1.dylib libonnxruntime.1.14.1.dylib
CWD = $(shell pwd)
fix_piper_tts_mac:
	softwareupdate --install-rosetta
#	Need to add some .dylib files to make it work 
	wget https://github.com/rhasspy/piper-phonemize/releases/download/2023.11.14-4/piper-phonemize_macos_x64.tar.gz -O bin/piper-phonemize.tar.gz
	
	cd bin && tar -xvzf piper-phonemize.tar.gz && cd ..
	
	$(foreach var,$(DYLIB_FILES),install_name_tool -change @rpath/$(var) ${CWD}/bin/piper-phonemize/lib/$(var) ${CWD}/bin/piper/piper;)

install_mac:
	mkdir -p data
	pip install -r requirements.txt
	brew update
	brew install ffmpeg
	port install espeak-ng
	brew install sox
	make whisper_cpp
install_linux:
	mkdir -p data
	pip install -r requirements.txt
	sudo apt update
	sudo apt install ffmpeg
	sudo apt install espeak-ng
	sudo apt install libsdl2-dev
	make whisper_cpp

whisper_cpp:
	git submodule init && git submodule update
	cd whisper.cpp && make -j stream
	cd whisper.cpp && ./models/download-ggml-model.sh small


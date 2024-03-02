DIFF_ARGS = --strip-trailing-cr

now:
	echo "Empty.  Use me."

notoo:
	python3 Drivers/not_ooxyz.py
	python3 comparepng.py Output/driver04_not_ooxyz.png Expected/expected04.png

push:
	git commit -a
	git push

install:
	sudo apt-get update
	sudo apt-get install python3-matplotlib
	sudo apt-get install python3-pip
	pip install pillow
	pip install pixelmatch

clean:
# For MacOS
	-rm .DS_Store
	-rm -r __pycache__
	-rm -r Drivers/__pycache__
# For all OSes
	-mkdir Output
	-rm Output/*.out
	-rm Output/*.png

test:
	@echo "*** If all 5 tests complete, then program is correct."
	@echo "***   Only errors are reported and testing stops."
	make clean
	make text
	make plot

text:
	@echo "*** Test 1: driver01"
	python3 Drivers/driver01.py > Output/test01.out
	diff $(DIFF_ARGS) Output/test01.out Expected/test01.txt
	@echo "****** Passed Test 1: driver01"

plot:
	@echo "*** Test 2: driver02"
	python3 Drivers/driver02.py
	python3 comparepng.py Output/driver02.png Expected/expected02.png
	@echo "****** Passed Test 2: driver02"
#
	@echo "*** Test 3: driver03"
	python3 Drivers/driver03.py
	python3 comparepng.py Output/driver03.png Expected/expected03.png
	@echo "****** Passed Test 3: driver03"
#
	@echo "*** Test 4: driver04"
	python3 Drivers/driver04.py
	python3 comparepng.py Output/driver04.png Expected/expected04.png
	@echo "****** Passed Test 4: driver04"
#
	@echo "*** Test 5: driver05"
	python3 Drivers/driver05.py
	python3 comparepng.py Output/driver05.png Expected/expected05.png
	@echo "****** Passed Test 5: driver05"

compare:
	python3 comparepng.py Output/driver02.png Expected/expected02.png
	python3 comparepng.py Output/driver03.png Expected/expected03.png
	python3 comparepng.py Output/driver04.png Expected/expected04.png
	python3 comparepng.py Output/driver05.png Expected/expected05.png

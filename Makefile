all: Feature_Selection

Feature_Selection:
	g++ main.cpp
	
run:
	./a.out
	
test:
	./a.out data.txt
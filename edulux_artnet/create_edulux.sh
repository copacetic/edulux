g++ -fPIC -Wl,export-dynamic -c edulux.cpp 
g++ -shared  -Wl,-export-dynamic,-soname, -o libedulux.so -lartnet edulux.o 
sudo cp libedulux.so /usr/local/lib/
sudo ldconfig -n
export LD_LIBRARY_PATH=/usr/local/lib
g++ edulux_test.cpp  -o test -L. -ledulux -lartnet edulux.o

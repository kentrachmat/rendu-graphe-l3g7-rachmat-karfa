DELETE = code/*answer.txt

gsm:
	cd code && python3 gsm.py

carte:
	cd code && python3 carte.py

sudoku:
	cd code && python3 sudoku.py

clean:
	rm -rf $(DELETE)

.PHONY: clean
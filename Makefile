DELETE = code/*_output.txt code/__pycache__

gsm:
	cd code && python3 gsm.py -i data/gsm_data.txt -o gsm_output.txt

carte:
	cd code && python3 carte.py -i data/carte_data.txt -o carte_output.txt

sudoku:
	cd code && python3 sudoku.py -i data/sudoku_data.txt -o sudoku_output.txt

clean:
	rm -rf $(DELETE)

.PHONY: clean
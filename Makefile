.PHONY: install paper clean

install:
	pip install -r requirements.txt

paper:
	cd exports/23_full_paper_generator_outputs/paper && make

clean:
	find . -name "*.aux" -delete
	find . -name "*.log" -delete
	find . -name "*.out" -delete
	find . -name "*.pdf" -delete

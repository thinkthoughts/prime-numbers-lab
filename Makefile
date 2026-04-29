.PHONY: install paper clean

install:
	pip install -r requirements.txt

paper:
	@if [ ! -d "exports/23_full_paper_generator_outputs/paper" ]; then \
		echo "Paper not generated yet. Run Notebook 23 first."; \
	else \
		cd exports/23_full_paper_generator_outputs/paper && make; \
	fi

clean:
	find . -name "*.aux" -delete
	find . -name "*.log" -delete
	find . -name "*.out" -delete
	find . -name "*.pdf" -delete

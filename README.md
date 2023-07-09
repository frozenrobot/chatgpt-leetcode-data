This is a supporting repository that contains data used and produced in the research paper, **Empirical Evaluation of ChatGPT's Ability to Solve Coding Problems on Leetcode**.

It contains the following contents:

* `statistics.ipynb`: Python notebook with calculations of different statistics pertaining to code quality metrics such as Cyclomatic Complexity, Token Count, Lines of Code, Time Complexity and Space Complexity. Most results are presented as cell output in human-readable format, but the data structures used allow it to easily be manipulated and formatted as CSV output if needed.
* `metrics_data.csv` and `number_matched_complexity_data.csv`: Input data files used in `statistics.ipynb`
* `solutions/`: Contains files with individual solutions for problems which had at least two correct solutions. This format is chosen so that Lizard (https://github.com/terryyin/lizard) can be used on each solution to automate the calculation of Cyclomatic Complexity, Token Count and Lines of Code.
* `Spreadsheets/`: (In different formats) Data around Solutions and Error Output, Acceptance Rates, Error Distribution, Raw Metrics Data and Metrics Statistics. This data can also be found at https://docs.google.com/spreadsheets/d/1H1M5xZdUb6bMrHb51eGAu80IVezWattz0GA9qfWVaI4/edit?usp=sharing
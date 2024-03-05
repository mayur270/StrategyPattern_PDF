# PDF Operations

In main.py file, strategy design pattern was used to define operations related 
to PDF manipulation.

It includes abstract and concrete classes for performing various operations
on PDF files, such as merging multiple PDFs into a single file and splitting a
PDF into multiple files.

#### Classes:
- <b>PDFOperation:</b> An abstract base class for defining PDF operations.
- <b>MergeStrategy:</b> A concrete implementation for merging PDF files.
- <b>SplitStrategy:</b> A concrete implementation for splitting PDF files.
- <b>PDFEditor:</b> Class for executing PDF operations.

### Usage: <br></b>
#### Example 1: Merge PDF
1. Initialize the merge strategy with the paths of PDF files to merge
```
pdf_paths_to_merge = ['path/to/first.pdf', 'path/to/second.pdf', 'path/to/third.pdf']
merge_strategy = MergeStrategy()
```

2. Create a PDF editor instance with the merge strategy <br>
```
pdf_editor = PDFEditor(merge_strategy)
```

3. Specify the output path for the merged PDF <br>
```
output_merge_path = 'path/to/output.pdf'
```

4. Execute the merge operation <br>
```
pdf_editor.execute_operation(pdf_paths_to_merge, output_merge_path)
print("Merged PDF created at:", output_merge_path)
```

#### Example 2: Split PDF

1. Initialize the split strategy
```
split_strategy = SplitStrategy()
```

2. Create a PDF editor instance with the split strategy
```
pdf_editor = PDFEditor(split_strategy)
```

3. Define the path to the PDF to split and the output directory
```
pdf_path_to_split = 'path/to/file.pdf'
output_split_path_template = 'path/to/output_page_{page}.pdf'
```

4. Assuming we want to split the first 5 pages
```
# Adjust `start_page` and `end_page` accordingly
start_page = 0
end_page = 5
```
```
# Execute the split operation for each page
for page in range(start_page, end_page):
    output_path = output_split_path_template.format(page=page + 1)  # +1 for human-readable page numbering
    split_strategy.execute(pdf_path_to_split, output_path, start_page=page, end_page=page + 1)

    print(f"Page {page + 1} saved to:", output_path)
```

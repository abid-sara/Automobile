import nbmerge

# List all your notebook filenames
notebooks = [
    "automobile.ipynb",
    "svm.ipynb",
]

# Merge the notebooks
merged_nb = nbmerge.merge_notebooks(file_paths=notebooks, base_dir=".")

# Write the merged notebook to a UTF-8 file
with open("automobile.ipynb", "w", encoding="utf-8") as f:
    nbmerge.write_notebook(merged_nb, f)

print("Merging completed: automobile.ipynb")

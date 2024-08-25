import nbformat

# Define the paths to your notebooks
notebook_paths = [
    r"C:\Users\saim\Just_one_for_all\Desktop\Compiled\gaurav.ipynb",
    r"C:\Users\saim\Just_one_for_all\Desktop\Compiled\stuti.ipynb",
    r"C:\Users\saim\Just_one_for_all\Desktop\Compiled\shubham.ipynb"
]

# Load the first notebook
with open(notebook_paths[0], 'r') as f:
    combined_nb = nbformat.read(f, as_version=4)

# Append cells from the other notebooks
for path in notebook_paths[1:]:
    with open(path, 'r') as f:
        nb = nbformat.read(f, as_version=4)
        combined_nb.cells.extend(nb.cells)

# Save the combined notebook
combined_notebook_path = r"C:\Users\saim\Just_one_for_all\Desktop\Compiled\combined_notebook.ipynb"
with open(combined_notebook_path, 'w') as f:
    nbformat.write(combined_nb, f)

print(f"Combined notebook saved to {combined_notebook_path}")

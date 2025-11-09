# 🔍 Directory Loader: Glob Pattern Quick Reference

Glob patterns are used to specify exactly which files a directory loader should find and process.

| Pattern | Description | Example Files Included |
| :--- | :--- | :--- |
| **`*.pdf`** | Matches **all $\text{.pdf}$ files** located only in the **root directory** (the starting directory of the loader). | `root/document.pdf`, `root/report.pdf` |
| **`data/*.csv`** | Matches **all $\text{.csv}$ files** located exactly inside the **`data/` folder** (a direct child of the root directory). | `root/data/sheet1.csv`, `root/data/records.csv` |
| **`**/*.txt`** | Matches **all $\text{.txt}$ files** located in **any subfolder** of the starting directory, as well as the root itself. | `root/file.txt`, `root/sub/data.txt`, `root/other/doc.txt` |
| **`**/*`** | Matches **all files** of **any type** in **all subfolders** and the root directory. This is the **most inclusive** pattern. | Matches every single file: $\text{.txt, .pdf, .csv, .jpg}$, etc., everywhere. |

---

### Key Takeaways for Glob Patterns:

* **`*` (Asterisk)**: Matches **zero or more characters** in a single directory component (path segment).
* **`**` (Double Asterisk)**: Matches **zero or more directories** (recursively), allowing you to search through subfolders.
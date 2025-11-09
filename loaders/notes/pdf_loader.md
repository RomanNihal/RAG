# 📄 PDF Loader Comparison in LangChain

Choosing the right PDF loader is essential for accurate data extraction, as different tools are optimized for different document complexities and structures.

| Use Case | Recommended PDF Loader(s) | Key Feature / Output |
| :--- | :--- | :--- |
| **Simple, Clean PDFs** (Standard text structure) | `PyPDFLoader` | Basic text extraction, fast and reliable for simple documents. |
| **PDFs with Tables/Columns** (Complex layouts) | `PDFPlumberLoader` | Specifically designed for parsing tabular and column-based data accurately. |
| **Scanned/Image PDFs** (Text is not selectable) | `UnstructuredPDFLoader` **or** `AmazonTextractPDFLoader` | Uses OCR (Optical Character Recognition) to convert images/scans into selectable text. |
| **Need Layout and Image Data** (Precise positioning and metadata) | `PyMuPDFLoader` | Provides robust layout information, coordinates, and can handle images within the PDF. |
| **Want Best Structure Extraction** (Headers, lists, sections) | `UnstructuredPDFLoader` | Excellent for hierarchical document analysis and general cleanup, yielding the most structured output. |

---

*Reference documentation: [LangChain Document Loaders](https://docs.langchain.com/oss/python/integrations/document_loaders)*
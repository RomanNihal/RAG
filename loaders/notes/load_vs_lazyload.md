# 📚 Document Loading Strategies: `load()` vs. `lazy_load()`

When working with document sources, understanding the difference between eager and lazy loading is crucial for optimizing memory and performance.

---

## 1. `load()` (Eager Loading)

This method loads all documents into memory immediately upon execution.

| Detail | Description |
| :--- | :--- |
| **Loading Style** | **Eager Loading** - Loads everything at once. |
| **Return Type** | Returns a **list** of `Document` objects. |
| **Memory Usage** | All documents are loaded **immediately into memory**. |
| **Best Used When** | The number of documents is **small** and you need to access all of them upfront, or if you prefer a single-step, predictable load time. |
| **Performance Note**| Can have a **higher initial load time** (latency) as it processes all files before returning. |

## 2. `lazy_load()` (Lazy Loading)

This method only loads documents when they are explicitly requested, allowing for streaming and lower memory overhead.

| Detail | Description |
| :--- | :--- |
| **Loading Style** | **Lazy Loading** - Loads on demand. |
| **Return Type** | Returns a **generator** of `Document` objects. |
| **Memory Usage** | Documents are fetched **one at a time** as needed, avoiding high memory usage. |
| **Best Used When** | Dealing with a **large number of documents** or very large individual documents where you want to **stream processing** (e.g., chunking, embedding) without consuming lots of memory. |
| **Performance Note**| Has a **faster initial return**, but introduces a slight delay each time the next document is requested from the generator. |
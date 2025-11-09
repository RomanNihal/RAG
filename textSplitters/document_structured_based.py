from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
public class MethodExample {
    public static void main(String[] args) {
        greet("Bob");
        int sum = add(5, 7);
        System.out.println("Sum: " + sum);
    }

    public static void greet(String name) {
        System.out.println("Hello, " + name + "!");
    }

    public static int add(int a, int b) {
        return a + b;
    }
}
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.JAVA,
    chunk_size=200,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[1])
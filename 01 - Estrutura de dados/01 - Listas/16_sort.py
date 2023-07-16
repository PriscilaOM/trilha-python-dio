linguagens = ["python", "js", "c", "java", "csharp"] 
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)#ordena alfabeticamente

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)#ordena alfabeticamente ao contrario

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens) #ordena por tamanho da palavra função anônima que não tem nome
#len tira o tamanho de uma string
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

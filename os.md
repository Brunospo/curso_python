# Módulo `os.path` em Python

O módulo `os.path` em Python fornece funções para manipulação de caminhos de arquivos e diretórios. Ele é especialmente útil para verificar, combinar e modificar caminhos de forma portátil entre sistemas operacionais.

## Funções comuns do `os.path`

### 1. `os.path.join()` – Junta partes de um caminho corretamente

```python
import os

caminho = os.path.join("pasta", "arquivo.txt")
print(caminho)  # 'pasta/arquivo.txt' (Windows usa '\')

```

### 2. `os.path.exists()` – Verifica se um arquivo ou pasta existe

```python
print(os.path.exists("arquivo.txt"))  # True se existir, False caso contrário
```

### 3. `os.path.isfile()` e `os.path.isdir()` – Verifica se é um arquivo ou diretório

```python
print(os.path.isfile("arquivo.txt"))  # True se for arquivo
print(os.path.isdir("pasta"))  # True se for diretório
```

### 4. `os.path.abspath()` – Obtém o caminho absoluto

```python
print(os.path.abspath("arquivo.txt"))  # Retorna o caminho completo do arquivo
```

### 5. ``os.path.basename()`` e ``os.path.dirname()`` – Obtém o nome do arquivo ou diretório

```python
caminho = "/home/user/arquivo.txt"
print(os.path.basename(caminho))  # 'arquivo.txt'
print(os.path.dirname(caminho))  # '/home/user'
```

### 6. ``os.path.splitext()`` – Separa o nome do arquivo da extensão

`

```python
print(os.path.splitext("foto.jpg"))  # ('foto', '.jpg')
```

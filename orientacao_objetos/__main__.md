# if __name__ == '__main__'

Em Python, if __name__ == '__main__': é uma verificação usada para determinar se o script está sendo executado diretamente ou importado como um módulo em outro código.
Por que usar isso?
Quando um arquivo Python é executado, a variável especial __name__ recebe o valor '__main__'. Se o arquivo for importado em outro script, essa variável terá o nome do próprio módulo. Isso permite que você escreva código que:

- Só execute certas partes quando o script for rodado diretamente.
- Evite execução indesejada ao ser importado em outro programa.
Exemplo prático:

```python
def saudacao():
    print("Olá, mundo!")

if __name__ == '__main__':
    saudacao()  # Só será executado se este arquivo for rodado diretamente.

```

Se esse arquivo for importado em outro código (import meu_script), a função saudacao() estará disponível, mas não será executada automaticamente.
Você já usou essa estrutura em algum projeto? 😃

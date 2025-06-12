# Diferença entre atributos de instância e atributos de classe no Python

Em Python, os atributos podem pertencer a **instâncias individuais** de uma classe ou à própria **classe**. Aqui está a diferença entre eles:

## Atributos de Instância

- São **específicos para cada objeto** criado a partir da classe.
- São definidos dentro do método `__init__()` usando `self`.
- Cada instância pode ter valores diferentes para esses atributos.

### Exemplo

```python
class Carro:
    def __init__(self, cor):
        self.cor = cor  # Atributo de instância

carro1 = Carro("vermelho")
carro2 = Carro("azul")

print(carro1.cor)  # Saída: vermelho
print(carro2.cor)  # Saída: azul
```

## Atributos de Classe

- São compartilhados por todas as instâncias da classe.
- São definidos diretamente na classe, sem o uso de self.
- Se um atributo de classe for alterado, a mudança afetará todas as instâncias (a menos que o atributo seja sobrescrito na instância).

### Exemplo

```python
class Carro:
    cor_padrao = "branco"  # Atributo de classe

carro1 = Carro()
carro2 = Carro()

print(carro1.cor_padrao)  # Saída: branco
print(carro2.cor_padrao)  # Saída: branco

Carro.cor_padrao = "preto"  # Alterando o atributo de classe

print(carro1.cor_padrao)  # Saída: preto
print(carro2.cor_padrao)  # Saída: preto
```

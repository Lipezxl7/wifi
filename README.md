# Consulta de senhas Wi-Fi salvas

Script em Python que lista os perfis de redes Wi-Fi salvos no Windows e tenta consultar a senha armazenada em cada perfil por meio do comando `netsh`.

## Requisitos

- Windows
- Python 3
- Permissão para consultar os perfis de rede do computador

## Como executar

No PowerShell ou no Prompt de Comando, dentro da pasta do projeto, execute:

```bash
python senha.py
```

Em alguns ambientes, o comando pode ser:

```bash
py senha.py
```

## Exemplo de saída

```text
Rede: MinhaRede                 | Senha: minha-senha
Rede: RedeAberta                | Senha: (Sem Senha / Aberta)
```

Se nenhum perfil for encontrado, o programa exibe:

```text
Nenhuma rede achada
```

## Estrutura

```text
.
├── senha.py    # Script principal
└── README.md   # Documentação do projeto
```

## Observações

- O programa consulta apenas perfis Wi-Fi já salvos no computador.
- A saída contém informações sensíveis. Não compartilhe o resultado publicamente.
- Use este script somente em computadores e redes para os quais você tem autorização.
- O funcionamento depende do `netsh` e do idioma/formato de saída configurado no Windows.

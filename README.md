# Consulta de senhas Wi-Fi salvas

Script que lista os perfis de redes Wi-Fi salvos no Windows e tenta consultar a senha armazenada em cada perfil por meio do comando `netsh`.

## Exemplo de saída

```text
Rede: MinhaRede                 | Senha: minha-senha
Rede: RedeAberta                | Senha: (Sem Senha / Aberta)
```

Se nenhum perfil for encontrado:

```text
Nenhuma rede achada
```

## Observações

- O programa consulta apenas perfis Wi-Fi já salvos no computador,sendo uma ferramenta de cybersecurity
- O funcionamento depende do `netsh` e do idioma/formato de saída configurado no Windows.

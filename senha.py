import subprocess
import re

def user():
    
    saida = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode()
    redes = []
    
    for linha in saida.splitlines():
        if ":" in linha and not "Perfil de grupo" in linha:
            nome = linha.split(":")[-1].strip()
            if nome and "Interfaces" not in linha:
                redes.append(nome)
                
    return redes

def senha(rede):
    try:
        saida = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', rede, 'key=clear']).decode()
        senha = re.search(r":\s*(.*)", [l for l in saida.splitlines() if "Conte" in l or "Key Content" in l][0])
        return senha.group(1).strip() if senha else "(Sem Senha / Aberta)"
    except Exception:
        return "(Sem Senha / Aberta)"

# main
redes = user()

if not redes:
    print("Nenhuma rede achada")
else:
    for rede in redes:
        print(f"Rede: {rede:<25} | Senha: {senha(rede)}")
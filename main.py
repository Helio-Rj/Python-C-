import subprocess

resultado = subprocess.check_output(["./hello"])

print("Python recebeu:")
print(resultado.decode())
print("Fim do programa Python.")

while True:
    email_usuario = input("Digite seu e-mail: ")
    
    email_confirmacao = input("Confirme seu e-mail: ")
    
    if email_usuario != email_confirmacao:
        print("E-mail incorreto. Tente novamente.")
        continue
    
    senha = input("Digite sua senha: ")
    
    senha_confirmacao = input("Confirme sua senha: ")
    
    if senha != senha_confirmacao:
        print("Senha incorreta. Tente novamente.")
        continue
    
    if senha == senha_confirmacao:
        print("Login bem-sucedido!")
        break
    else:
        print("Senha incorreta. Tente novamente.")
        
        
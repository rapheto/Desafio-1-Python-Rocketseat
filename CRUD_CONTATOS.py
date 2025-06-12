"""
### Regras da aplicação
- A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
- Deve ser possível adicionar um contato
    - O contato pode ter os dados:
    - Nome
    - Telefone
    - Email
    - Favorito (está opção é para poder marcar um contato como favorito)
- Deve ser possível visualizar a lista de contatos cadastrados
- Deve ser possível editar um contato
- Deve ser possível marcar/desmarcar um contato como favorito
- Deve ser possível ver uma lista de contatos favoritos
- Deve ser possível apagar um contato
"""
# quebrar linha \n
agenda = []
def add_contact(cont_list, cont_name, cont_number, cont_email):
    agenda = {"cont_name": cont_name, "cont_number": cont_number, "cont_email": cont_email, "is_starred": False}
    cont_list.append(agenda)
    print("Contact added!")
    return

def list_contacts(cont_list):
    print("\nYour contacts:")
    for index, contact in enumerate(cont_list, start=1):
        if contact["is_starred"]:
            cont_status = "✪"
        else:
            cont_status = " "
        cont_name = contact["cont_name"]
        cont_number = contact["cont_number"]
        cont_email = contact["cont_email"]
        print(f" \n{index} - {cont_name}")
        print(f"Number - {cont_number}")
        print(f"Email - {cont_email}")
        print(f"Favorito - [{cont_status}]")
    return

def list_favorite_contacts(cont_list):
    print("\nYour favorite contacts:")
    for index, contact in enumerate(cont_list, start=1):
        if contact["is_starred"]:
            cont_name = contact["cont_name"]
            cont_number = contact["cont_number"]
            cont_email = contact["cont_email"]
            cont_status = "✪"
            print(f"{index} - {cont_name}")
            print(f"Number - {cont_number}")
            print(f"Email - {cont_email}")
            print(f"Favorito - [{cont_status}]")
    return

def update_contact(cont_list, index, new_cont_name, new_cont_number,  new_cont_email ):
    if index >= 0 and index <= len(cont_list):
        cont_list[index - 1]["cont_name"] = new_cont_name
        cont_list[index - 1]["cont_number"] = new_cont_number
        cont_list[index - 1]["cont_email"] = new_cont_email
        print("Contato atualizado")
        print(f"{index} New name - {new_cont_name}")
        print(f"{index} New number - {new_cont_number}")
        print(f"{index} New email - {new_cont_email}")
    else:
        print("Invalid Contact!")
    return

def favorite_contact(cont_list, index):
    if index >= 0 and index <= len(cont_list):
        cont_list[index - 1]["is_starred"] = True
        cont_name = cont_list[index - 1]["cont_name"]
        print(f"{index} - {cont_name} is now favorited")
    else:
        print("Invalid contact!")
    return

def delete_contact(cont_list, index):
    if index >= 0 and index <= len(cont_list):
        cont_name = cont_list[index - 1]["cont_name"]
        del cont_list[index -1]
        print(f"Deleted contact: {index} - {cont_name}")
    else:
        print("Invalid contact!")
    return

while True: 
    print("\nContacts Agenda")
    print("1 - New Contact")
    print("2 - View Contacts")
    print("3 - Edit Contacts")
    print("4 - Favorit Contact")
    print("5 - View Favorit List")
    print("6 - Delete Contact")
    print("7 - Quit")

    op = int(input("Choose an option: "))

    if op == 1:
        cont_name = input("Contact name: ")
        cont_number = input("Contact number: ")
        cont_email = input("Contact email: ")
        add_contact(agenda, cont_name, cont_number, cont_email)
    elif op == 2:
        list_contacts(agenda)
    elif op ==3:
        list_contacts(agenda)
        index = int(input("Which contact do you want to edit: "))
        new_cont_name = input("New name: ")
        new_cont_number = input("New number: ")
        new_cont_email = input("New email: ")
        update_contact(agenda, index, new_cont_name, new_cont_number, new_cont_email)
    elif op == 4:
        list_contacts(agenda)
        index = int(input("Which contact you want to favorite: "))
        favorite_contact(agenda, index)
    elif op == 5:
        list_favorite_contacts(agenda)
    elif op == 6:
        list_contacts(agenda)
        index = int(input("Which contact do you want to delete: "))
        delete_contact(agenda, index)
    elif op == 7:
        print("Quiting")
        break
    else:
        print("Invalid option")


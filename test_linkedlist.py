from MyLinkedList import LinkedList

lista = LinkedList()

lista.append(10)
lista.append(20)
lista.append(30)

lista.display()  

print(lista.search(20))  
print(lista.search(50))  

lista.delete(20)
lista.display()  

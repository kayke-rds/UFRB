/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.datastructures.listasimplesmenteencadeada;


/**
 *
 * @author Kayke
 */
public class Main {
    
    
    public static void main(String args[]){    
        
        System.out.println("Testando lista simplesmente encadeada:");
        ListaSimplesmenteEncadeada lista = new ListaSimplesmenteEncadeada();
                
        System.out.println("Adicionando valores:");
        lista.adicionarNodo(new Nodo(2));
        lista.printLista();        
        
        lista.adicionarNodo(new Nodo(4));
        lista.printLista();
        
        lista.adicionarNodo(new Nodo(3));
        lista.printLista();
        
        lista.adicionarNodo(new Nodo(8));
        lista.printLista();
        
        lista.adicionarNodo(new Nodo(7));
        lista.printLista();
        
        
        
        System.out.println("Removendo valores: ");
        
        lista.removerLista(4);
        lista.printLista();
        
        lista.removerLista(10);
        lista.printLista();
        
        lista.removerLista(3);
        lista.printLista();
        
        lista.removerLista(8);
        lista.printLista();
        
        lista.removerLista(2);
        lista.printLista();
        
        lista.removerLista(7);
        lista.printLista();
        
        lista.removerLista(2);
        lista.printLista();
        System.out.println("Fim do teste de lista;");
        System.out.println("");
        
        System.out.println("Testando Pilha:");
        Pilha pilha = new Pilha();
        
        System.out.println("Adicionando valores");
        
        pilha.addNodo(new Nodo(1));
        pilha.printPilha();
        
        pilha.addNodo(new Nodo(2));
        pilha.printPilha();
        
        pilha.addNodo(new Nodo(3));
        pilha.printPilha();
        
        pilha.addNodo(new Nodo(4));
        pilha.printPilha();
        
        pilha.addNodo(new Nodo(5));
        pilha.printPilha();
        
        pilha.addNodo(new Nodo(6));
        pilha.printPilha();
        
        System.out.println("Removendo valores:");
        
        pilha.removeNodo();
        pilha.printPilha();
        
        pilha.removeNodo();
        pilha.printPilha();
        
        pilha.removeNodo();
        pilha.printPilha();
        
        pilha.removeNodo();
        pilha.printPilha();
        
        pilha.removeNodo();
        pilha.printPilha();
        
        pilha.removeNodo();
        pilha.printPilha();
        
        pilha.removeNodo();
        pilha.printPilha();
    
    }    
}

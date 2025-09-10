/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.datastructures.listasimplesmenteencadeada;


/**
 *
 * @author pagano
 */
public class Main {
    
    
    public Main(){    
        
        ListaSimplesmenteEncadeada lista = new ListaSimplesmenteEncadeada();
                
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
        
    
    }    
    
    public static void main(String args[]){
    
        Main main = new Main();
    
    }
    
    
}

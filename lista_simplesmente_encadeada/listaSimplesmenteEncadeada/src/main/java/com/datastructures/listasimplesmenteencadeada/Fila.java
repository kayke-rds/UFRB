/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.datastructures.listasimplesmenteencadeada;

/**
 *
 * @author kayke
 */
public class Fila {

    /**
     * @return the primeiro
     */
    public Nodo getPrimeiro() {
        return primeiro;
    }

    /**
     * @return the ultimo
     */
    public Nodo getUltimo() {
        return ultimo;
    }
    private Nodo primeiro;
    private Nodo ultimo;
    
    public Fila(){
        primeiro = null;
        ultimo = null;
    }
    
    public void addNodo(Nodo novo){
        if(primeiro == null){
            primeiro = novo;
            ultimo = novo;
            //novo é o Raul Seixas
        }
        else if(primeiro == ultimo){
            primeiro.prox = novo;
            ultimo = novo;
        }
        else{
            ultimo.prox = novo;
            ultimo = novo;
        }
    }
    
    public void removeNodo(){
        if(primeiro == null){
            System.out.println("Fila vazia!");
        }
        else if(primeiro == ultimo){
            primeiro = null;
            ultimo = null;
        }
        else{
            Nodo aux = primeiro;
            primeiro = primeiro.prox;
            aux.prox = null;
        }
    }
    
    public void printFila(){
        if(primeiro == null){
            System.out.println("Fila vazia!");
        }
        else{
            printRec(primeiro);
        }
    }
    
    private void printRec(Nodo nodo){
        System.out.print(nodo.val + " ");
        if(nodo.prox != null){
            printRec(nodo.prox);
        }
        else{
            System.out.println("");
        }
    }
    
}

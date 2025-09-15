/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.datastructures.listasimplesmenteencadeada;

/**
 *
 * @author Kayke
 */
public class ListaSimplesmenteEncadeada {
    
    
    Nodo inicio;
    Nodo fim;
    
    public ListaSimplesmenteEncadeada(){
    
        inicio = null;
        fim = null;
    }
    
    
    public void adicionarNodo(Nodo novo)
    {
    
        if(inicio == null && fim == null)
        {            
            inicio = novo;
            fim = novo;  
        }
        else if(inicio.val > novo.val)
        {
            novo.prox = inicio;
            inicio = novo;
        }
        else if(fim.val < novo.val)
        {
            fim.prox = novo;
            fim = novo;
        }
        else    
        {
            addNodoRec(inicio, null, novo);
        }
    }

    

    private void addNodoRec(Nodo aux, Nodo aux1, Nodo novo){
        if(aux != null){
            if(aux.val > novo.val){
                aux1.prox = novo;
                novo.prox = aux;
            }
        else {
            addNodoRec(aux.prox, aux, novo);
            }
        }
    }
    
    
    
    public void removerLista(int val){
        if(inicio == null && fim == null){            
            System.out.println("Lista vazia");
        }
        else if(inicio.val == val)
        {
            inicio = inicio.prox;
            if(inicio == null){
                fim = null;
            }
        }
        else{
            remListaRec(inicio, null, val);
        }
    }
    
    private void remListaRec(Nodo aux, Nodo aux1, int val) {
        if(aux != null){
                
            if(aux.val == val){
                               
                aux1.prox = aux.prox;                

                if(aux1.prox == null){                
                    fim = aux1;
                }

                aux = null;
            }               
                
            else {
                remListaRec(aux.prox, aux, val);
            }
        }
        else {
            System.out.println("Valor nao encontrado");
        }
    }
    
    public void printLista(){
        printRec(inicio);
    }
    
    private void printRec(Nodo aux){
        if(aux != null){
            System.out.print(aux.val + " ");
            printRec(aux.prox);
        }
        else{
        System.out.println("");
        }
    }
}

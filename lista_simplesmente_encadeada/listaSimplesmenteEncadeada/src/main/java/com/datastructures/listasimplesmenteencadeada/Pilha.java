/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.datastructures.listasimplesmenteencadeada;

/**
 *
 * @author kayke
 */
public class Pilha {
    private Nodo topo;
    
    public Pilha() {
        topo = null;
    }

    /**
     * @return the topo
     */
    public Nodo getTopo() {
        return topo;
    }

    
    public void addNodo(Nodo novo){
        if(topo == null) {
            topo = novo;
        }
        else {
            novo.prox = topo;
            topo = novo;
        }
    }
    
    public void removeNodo(){
        if(topo == null){
            System.out.println("Pilha vazia!");
        }
        else if(topo.prox == null){
            topo = null;
        }
        else{
            Nodo aux = topo;
            topo = topo.prox;
            aux.prox = null;
        }
    }
    
    public void printPilha(){
        if(topo == null){
            System.out.println("Pilha vazia!");
        }
        else{
            printRec(topo);
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

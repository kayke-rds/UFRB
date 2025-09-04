/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ListaSimplesmenteEncadeada;

/**
 *
 * @author pagano
 */
public class ListaSimplesmenteEncadeada {


    Nodo inicio;
    Nodo fim;

    public ListaSimplesmenteEncadeada() {

        inicio = null;
        fim = null;
    }


    public void adicionarNodo(Nodo novo) {

        if (inicio == null && fim == null) {
            inicio = novo;
            fim = novo;
        } else if (inicio.val > novo.val) {
            novo.prox = inicio;
            inicio = novo;
        } else if (fim.val < novo.val) {
            fim.prox = novo;
            fim = novo;
        } else {

            Nodo aux = inicio;
            Nodo aux1 = null;

            while (aux != null) {

                if (aux.val > novo.val) {
                    break;
                }

                aux1 = aux;
                aux = aux.prox;
            }

            aux1.prox = novo;
            novo.prox = aux;

        }

    }


    public void removerLista(int val) {
        if (inicio == null && fim == null) {
            System.out.println("Lista vazia");
        } else if (inicio.val == val) {
            inicio = inicio.prox;
            if (inicio == null) {
                fim = null;
            }
        } else {

            Nodo aux = inicio;
            Nodo aux1 = null;

            while (aux != null) {

                if (aux.val == val) {
                    break;
                }

                aux1 = aux;
                aux = aux.prox;
            }

            if (aux == null) {
                System.out.println("Valor nao encontrado");
            } else {
                aux1.prox = aux.prox;

                if (aux1.prox == null) {
                    fim = aux1;
                }

                aux = null;
            }


        }

    }


    public void printLista() {

        Nodo aux = inicio;

        while (aux != null) {
            System.out.print(aux.val + " ");
            aux = aux.prox;
        }
        System.out.println("");

    }


    public void remover_por_indice(int index) {
        if(index < 0) {
            System.out.println("Indice deve ser inteiro positivo");
            return;
        }

        if(inicio == null){
            System.out.println("Lista vazia");
            return;
        }
        if(inicio == fim && index !=0){
            System.out.println("Indice fora da lista");
            return;
        }
        Nodo aux = inicio;
        Nodo aux1 = null;
        for (int i = 0; i < index; i++) {
            aux1 = aux;
            aux = aux.prox;
            if (aux.prox == null && i != index-1) {
                System.out.println("Index fora da lista");
                return;
            }
        }


        if (aux == inicio) {
            inicio = inicio.prox;
        }
        else if (aux == fim) {
            fim = aux1;
            fim.prox = null;
        }
        else {
            aux1.prox = aux.prox;
            aux.prox = null;
        }

    }
}

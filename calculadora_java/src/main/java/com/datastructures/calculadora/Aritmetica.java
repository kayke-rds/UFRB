/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.datastructures.calculadora;

/**
 *
 * @author kayke
 */
public class Aritmetica {
    
    public static int main (int n1, int n2, char op) {
        switch(op){
            case('+') -> {
                Aritmetica arit = new Aritmetica();
                return arit.soma(n1, n2);
            }
            case('-') -> {
                    Aritmetica arit = new Aritmetica();
                    return arit.subtracao(n1, n2);
                }
            case('*') -> {
                    Aritmetica arit = new Aritmetica();
                    return arit.multiplicacao(n1, n2);
                }
            case('/') -> {
                    Aritmetica arit = new Aritmetica();
                    return arit.divisao(n1, n2);
                }
            }
        return 0;
    }
    public int soma(int n1, int n2) {
        return n1 + n2;
    }
    public int subtracao(int n1, int n2) {
        return n1 - n2;
    }
    public int multiplicacao(int n1, int n2) {
        return n1 * n2;
    }
    public int divisao(int n1, int n2) {
        if (n2 != 0) {
            return n1 / n2;
        }
        else
            return 0;
    }
}

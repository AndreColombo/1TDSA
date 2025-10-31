package br.com.fiap.main;

import javax.swing.*;

public class TesteExcecao {

    public static void main(String[] args) {

        try {
            double valor = Double.parseDouble(JOptionPane.showInputDialog("Digite o valor"));
            System.out.println(valor);
        }catch (NumberFormatException e){
            System.out.println("Digitado Letra em campo para entrada de numero");
            e.printStackTrace();
        }catch (ArithmeticException e) {
            System.out.println("Falha aritmetica na tentativa de dividir por zero");
            e.printStackTrace();
        }
        finally {
            System.out.println("OK");
        }




    }



}

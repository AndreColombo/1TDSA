package br.com.fiap.main;

import br.com.fiap.beans.Colaborador;

import javax.swing.*;
import java.util.ArrayList;

public class TesteArrayList {
    // String
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    // int
    static int inteiro(String j) {
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    // double
    static double real(String j) {
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        // Preparar lista
        ArrayList<Colaborador> listaColaborador = new ArrayList<Colaborador>();

        // Preparar objeto
        Colaborador objColaborador = null;

        // Laço de Repetição
        //                    do   / while
        //                    faça / enquanto
        do {
            // Entradas
            objColaborador = new Colaborador();
            objColaborador.setNome(texto("Nome:"));
            objColaborador.setCargo(texto("Cargo:"));
            objColaborador.setIdade(inteiro("Idade"));
            objColaborador.setSalario(real("Salário:"));

            listaColaborador.add(objColaborador);
        } while (JOptionPane.showConfirmDialog(null, "add mais colaboradores?", "CADASTRO DE COLABORADORES", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == 0);

        // Saídas utilizando o foreach
        for (Colaborador colaborador : listaColaborador) {
            System.out.println("\nNome: " + colaborador.getNome() + "\nCargo: " + colaborador.getCargo() + "\nIdade: " + colaborador.getIdade() + "\nSalário: " + colaborador.getSalario());
        }
    }
}

package br.com.fiap.main;

import br.com.fiap.beans.Colaborador;

import javax.swing.*;

public class TesteSistema {
    public static void main(String[] args) {
        // instanciar objetos
        Colaborador objColaborador = new Colaborador();

        // entradas
        objColaborador.setNome(JOptionPane.showInputDialog("Digite o nome do colaborador:"));
        objColaborador.setEmail(JOptionPane.showInputDialog("Digite o email:"));
        objColaborador.setCargo(JOptionPane.showInputDialog("Digite o cargo:"));
        objColaborador.setIdade(Integer.parseInt(JOptionPane.showInputDialog("Digite a idade:")));
        objColaborador.setQuantidadeHoras(Double.parseDouble(JOptionPane.showInputDialog("Informe a quantidade de horas:")));
        objColaborador.setValorHora(Double.parseDouble(JOptionPane.showInputDialog("Informe o valor da hora :")));

        // saídas
        System.out.println(
                objColaborador
        );

        System.out.println(
                "\n\nSALÁRIO DO COLABORADOR: " + objColaborador.calcularSalario()
        );

        System.out.println(
                "\nINFORMAÇÃO: " + objColaborador.informacaoSalario()
        );
    }
}

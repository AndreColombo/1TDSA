package br.com.fiap.main;

import br.com.fiap.beans.Aluno;
import br.com.fiap.beans.Endereco;
import br.com.fiap.beans.Professor;

import javax.swing.*;

public class TesteSistema {
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    static int inteiro(String j) {
        return Integer.parseInt(JOptionPane.showInputDialog(j));
    }

    static double real(String j) {
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        Aluno objAluno = new Aluno(
                texto("Nome"),
                inteiro("Idade"),
                texto("CPF"),
                texto("RG"),
                texto("Turma"),
                texto("RM"),
                real("Nota")
        );

        Endereco objEnderecoAluno = new Endereco(
                texto("Logradouro"),
                inteiro("Número"),
                texto("Complemento"),
                texto("Bairro"),
                texto("Cidade"),
                texto("CEP")
        );

        objAluno.setEndereco(objEnderecoAluno);

        Professor objProfessor = new Professor(
                texto("Nome"),
                inteiro("Idade"),
                texto("CPF"),
                texto("RG"),
                inteiro("Quantidade de Turmas")
        );
        Endereco objEnderecoProfessor = new Endereco(
                texto("Logradouro"),
                inteiro("Número"),
                texto("Complemento"),
                texto("Bairro"),
                texto("Cidade"),
                texto("CEP")
        );

        objProfessor.setEndereco(objEnderecoProfessor);

        System.out.println(objAluno + "" + objProfessor);
    }
}

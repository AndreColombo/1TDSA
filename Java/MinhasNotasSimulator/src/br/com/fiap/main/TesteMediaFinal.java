package br.com.fiap.main;

import br.com.fiap.beans.MediaFinal;

import javax.swing.*;

public class TesteMediaFinal {
    // double
    static double real(String j) {
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        MediaFinal mediaFinal = new MediaFinal();

        mediaFinal.setMediaSemestre1(real("Média do 1° Semestre"));
        mediaFinal.setMediaSemestre2(real("Média do 2° Semestre"));

        System.out.println(mediaFinal);
    }
}

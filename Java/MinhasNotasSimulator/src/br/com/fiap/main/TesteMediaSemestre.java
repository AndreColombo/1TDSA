package br.com.fiap.main;

import br.com.fiap.beans.MediaSemestre;

import javax.swing.*;

public class TesteMediaSemestre {
    // double
    static double real(String j) {
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        // Instanciar objeto
        MediaSemestre mediaSemestre = new MediaSemestre();

        mediaSemestre.setCp1(real("Nota da CP1"));
        mediaSemestre.setCp2(real("Nota da CP3"));
        mediaSemestre.setSprint1(real("Sprint 1"));
        mediaSemestre.setSprint2(real("Sprint 2"));
        mediaSemestre.setGs(real("Global Solution"));

        // Saídas CPs
        System.out.println(
                "CHECKPOINTS" + "\nCP1: " + mediaSemestre.getCp1() + "\nCP2: " + mediaSemestre.getCp2() + "\nMinha média das CPs " + mediaSemestre.calcularMediaCps() + "\nCom " + mediaSemestre.pontosCps() + " pontos alcançados do total de 2 possíveis"
        );

        // Saídas Sprints
        System.out.println(
                "\n\nCHALLENGE SPRINTS" + "\nSprint1 " + mediaSemestre.getSprint1() + "\nSprint2 " + mediaSemestre.getSprint2() + "\nMinha média das Sprints " + mediaSemestre.calcularMediaSprints() + "\nCom " + mediaSemestre.pontosSprints() + " pontos alcançados do total de 2 possíveis"
        );

        // Saídas CPs e Sprints
        System.out.println(
                "\n\nMédia de nota de CPs e Sprints: " + mediaSemestre.mediaCpsSprints() + "\nCom " + mediaSemestre.pontosCpsSprints() + " pontos alcançados do total de 4 possíveis"
        );

        // Saídas GS e média semestral
        System.out.println(
                "\n\nNota da Global Solution: " + mediaSemestre.getGs() + "\nPontuação da Global Solution: " + mediaSemestre.pontosGs() + " de 6 pontos possíveis" + "\nSUA MÉDIA DE NOTA SEMESTRAL É ... " + mediaSemestre.mediaSemestral()
        );
    }
}

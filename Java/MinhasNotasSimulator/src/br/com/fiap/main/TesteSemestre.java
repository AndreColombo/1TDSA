package br.com.fiap.main;

import br.com.fiap.beans.MediaSemestre;

import javax.swing.*;

public class TesteSemestre {
    // double
    static double real(String j) {
        return Double.parseDouble(JOptionPane.showInputDialog(j));
    }

    public static void main(String[] args) {
        // Instanciar objeto
        MediaSemestre ms = new MediaSemestre();

        ms.setCp1(real("Nota da CP1"));
        ms.setCp2(real("Nota da CP3"));
        ms.setSprint1(real("Sprint 1"));
        ms.setSprint2(real("Sprint 2"));
        ms.setGs(real("Global Solution"));

        // Saídas CPs
        System.out.println(
                "CHECKPOINTS" + "\nCP1: " + ms.getCp1() + "\nCP2: " + ms.getCp2() + "\nMinha média das CPs " + ms.calcularMediaCps() + "\nCom " + ms.pontosCps() + " pontos alcançados do total de 2 possíveis"
        );

        // Saídas Sprints
        System.out.println(
                "\n\nCHALLENGE SPRINTS" + "\nSprint1 " + ms.getSprint1() + "\nSprint2 " + ms.getSprint2() + "\nMinha média das Sprints " + ms.calcularMediaSprints() + "\nCom " + ms.pontosSprints() + " pontos alcançados do total de 2 possíveis"
        );

        // Saídas CPs e Sprints
        System.out.println(
                "\n\nMédia de nota de CPs e Sprints: " + ms.mediaCpsSprints() + "\nCom " + ms.pontosCpsSprints() + " pontos alcançados do total de 4 possíveis"
        );

        // Saídas GS e média semestral
        System.out.println(
                "\n\nNota da Global Solution: " + ms.getGs() + "\nPontuação da Global Solution: " + ms.pontosGs() + " de 6 pontos possíveis" + "\nSUA MÉDIA DE NOTA SEMESTRAL É ... " + ms.mediaSemestral()
        );
    }
}

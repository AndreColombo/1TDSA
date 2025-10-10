package br.com.fiap.main;

import br.com.fiap.api.Endereco;
import br.com.fiap.api.Planeta;
import br.com.fiap.services.SwPlanetaServices;

import javax.swing.*;
import java.io.IOException;

public class TesteSwPlaneta {
    static String texto(String j) {
        return JOptionPane.showInputDialog(j);
    }

    public static void main(String[] args) throws IOException {
        SwPlanetaServices swPlanetaServices = new SwPlanetaServices();

        String p = texto("Informe o número do Planeta");

        Planeta objPlaneta = swPlanetaServices.getPlaneta(p);

        System.out.println(objPlaneta);
    }
}

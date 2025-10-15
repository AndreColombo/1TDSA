package br.com.fiap.main;

import br.com.fiap.api.Planeta;
import br.com.fiap.services.SwPlanetaService;

import javax.swing.*;
import java.io.IOException;

public class TesteSwPlaneta {

    static String texto(String j){
        return JOptionPane.showInputDialog(j);
    }

    public static void main(String[] args) throws IOException {

        SwPlanetaService swPlanetaServices = new SwPlanetaService();

        String p = texto("Informe o numero do Planeta");

        Planeta objPlaneta = swPlanetaServices.getPlaneta(p);

        System.out.println(objPlaneta);
    }

}

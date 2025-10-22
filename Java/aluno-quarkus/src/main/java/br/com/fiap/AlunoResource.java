package br.com.fiap;

import br.com.fiap.beans.Aluno;
import br.com.fiap.bo.AlunoBO;
import jakarta.ws.rs.GET;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;

import java.sql.SQLException;
import java.util.ArrayList;

@Path("/aluno")
public class AlunoResource {
    AlunoBO alunoBO = new AlunoBO();

    // Selecionar
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public ArrayList<Aluno> selecionarRs() throws SQLException, ClassNotFoundException {
        return (ArrayList<Aluno>) alunoBO.selecionarB0();
    }
}

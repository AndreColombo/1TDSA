package br.com.fiap;

import br.com.fiap.beans.Aluno;
import br.com.fiap.bo.AlunoBO;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.*;
import jakarta.ws.rs.ext.Provider;

import java.sql.SQLException;
import java.util.ArrayList;


@Provider

@Path("/aluno")
public class AlunoResource {

    private AlunoBO alunoBO = new AlunoBO();

    // Selecionar
    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public ArrayList<Aluno> selecionarRs() throws ClassNotFoundException, SQLException, SQLException {
        return  (ArrayList<Aluno>)  alunoBO.selecionarBo();
    }

    // Inserir
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response inserirRs(Aluno aluno, @Context UriInfo uriInfo ) throws ClassNotFoundException, SQLException {
        alunoBO.inserirBo(aluno);
        UriBuilder builder = uriInfo.getAbsolutePathBuilder();
        builder.path(Integer.toString(aluno.getRm()));
        return Response.created(builder.build()).build();
    }

    // Atualizar
    @PUT
    @Consumes(MediaType.APPLICATION_JSON)
    public Response atualizarRs(Aluno aluno, @PathParam("rm") int rm) throws ClassNotFoundException, SQLException {
        alunoBO.atualizarBo(aluno);
        return Response.ok().build();
    }

    // Deletar
    @DELETE
    @Path("/{rm}")
    @Consumes(MediaType.APPLICATION_JSON)
    public Response deletarRs(@PathParam("rm") int rm) throws ClassNotFoundException, SQLException {
        alunoBO.deletarBo(rm);
        return Response.ok().build();
    }

}

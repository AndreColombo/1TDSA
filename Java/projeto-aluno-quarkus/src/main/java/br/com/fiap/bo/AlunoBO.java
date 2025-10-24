package br.com.fiap.bo;

import java.sql.SQLException;
import java.util.ArrayList;

import br.com.fiap.beans.Aluno;
import br.com.fiap.dao.AlunoDAO;

public class AlunoBO {

	AlunoDAO alunoDAO;

	// Selecionar
	public ArrayList<Aluno> selecionarBo() throws ClassNotFoundException, SQLException {
		alunoDAO = new AlunoDAO();
		// Regra de negocios
		
		return (ArrayList<Aluno>) alunoDAO.selecionar();
	}

	// Inserir 
	public void inserirBo(Aluno aluno) throws ClassNotFoundException, SQLException {
		AlunoDAO alunoDao = new AlunoDAO();			
		// Regra de negocios		
		alunoDao.inserir(aluno);		
	}
	
	// Atualizar
	public void atualizarBo (Aluno aluno) throws ClassNotFoundException, SQLException {
		AlunoDAO alunoDao = new AlunoDAO();			
		// Regra de negocios		
		alunoDao.atualizar(aluno);
	}
	
	// Deletar 
	public void deletarBo (int rm) throws ClassNotFoundException, SQLException {
		AlunoDAO alunoDao = new AlunoDAO();

		// Regra de negocios

		alunoDao.deletar(rm);
	}
	

}

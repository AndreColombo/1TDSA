package br.com.fiap.services;

import br.com.fiap.api.Endereco;
import br.com.fiap.api.Pessoa;
import com.google.gson.Gson;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

public class SwPessoaService {
    public Pessoa getPessoa(String p) throws IOException {
        Pessoa pessoa = null;

        // Request
        HttpGet request = new HttpGet("https://swapi.dev/api/people/" + p);

        // Client
        CloseableHttpClient httpClient = HttpClientBuilder.create().disableRedirectHandling().build();

        // Response
        CloseableHttpResponse response = httpClient.execute(request);

        // entity
        HttpEntity entity = response.getEntity();

        if (entity != null) {
            String result = EntityUtils.toString(entity);

            Gson gson = new Gson();

            pessoa = gson.fromJson(result, Pessoa.class);
        }

        return pessoa;
    }
}

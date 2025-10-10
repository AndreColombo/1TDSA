package br.com.fiap.services;

import br.com.fiap.api.Cartoon2D;
import com.google.gson.Gson;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

public class Cartoon2DService {
    // metodo para consumir a API
    public Cartoon2D getCartoon(String c) throws IOException {
        Cartoon2D cartoon2D = null;

        // request
        HttpGet request = new HttpGet("https://api.sampleapis.com/cartoons/cartoons2D/" + c);

        // client
        CloseableHttpClient httpClient = HttpClientBuilder.create().disableRedirectHandling().build();

        // response
        CloseableHttpResponse response = httpClient.execute(request);

        // entity
        HttpEntity entity = response.getEntity();

        if (entity != null) {
            // String Json
            String result = EntityUtils.toString(entity);

            // Gson para converter em um objeto Java
            Gson gson = new Gson();

            cartoon2D = gson.fromJson(result, Cartoon2D.class);
        }

        return cartoon2D;
    }
}

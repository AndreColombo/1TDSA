package br.com.fiap.services;

import br.com.fiap.api.Cartoon3D;
import com.google.gson.Gson;
import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClientBuilder;
import org.apache.http.util.EntityUtils;

import java.io.IOException;

public class Cartoon3DService {
    // metodo para consumir a API
    public Cartoon3D getCartoon(String c) throws IOException {
        Cartoon3D cartoon3D = null;

        // request
        HttpGet request = new HttpGet("https://api.sampleapis.com/cartoons/cartoons3D/" + c);

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

            cartoon3D = gson.fromJson(result, Cartoon3D.class);
        }

        return cartoon3D;
    }
}

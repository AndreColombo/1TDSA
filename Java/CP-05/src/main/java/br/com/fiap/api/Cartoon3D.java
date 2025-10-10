package br.com.fiap.api;

import java.util.List;

public class Cartoon3D {
    private String title;
    private int year;
    private int episodes;
    private List<String> creator;
    private List<String> genre;
    private String rating;

    public Cartoon3D() {
    }

    public Cartoon3D(String title, int year, int episodes, List<String> creator, List<String> genre, String rating) {
        this.title = title;
        this.year = year;
        this.episodes = episodes;
        this.creator = creator;
        this.genre = genre;
        this.rating = rating;
    }

    public String getTitle() {
        return title;
    }
    public void setTitle(String title) {
        this.title = title;
    }

    public int getYear() {
        return year;
    }
    public void setYear(int year) {
        this.year = year;
    }

    public int getEpisodes() {
        return episodes;
    }
    public void setEpisodes(int episodes) {
        this.episodes = episodes;
    }

    public List<String> getCreator() {
        return creator;
    }
    public void setCreator(List<String> creator) {
        this.creator = creator;
    }

    public List<String> getGenre() {
        return genre;
    }
    public void setGenre(List<String> genre) {
        this.genre = genre;
    }

    public String getRating() {
        return rating;
    }
    public void setRating(String rating) {
        this.rating = rating;
    }

    @Override
    public String toString() {
        return "DESENHO 3D" +
                "\nTítulo: '" + title + '\'' +
                "\nAno Lançamento: " + year +
                "\nNum. Episódios: " + episodes +
                "\nCriador(es): " + creator +
                "\nGênero(s): " + genre +
                "\nClassificação: '" + rating + '\'';
    }
}

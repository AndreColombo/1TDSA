import { useEffect, useState } from "react";

export default function Home() {
  const [currentWeather, setCurrentWeather] = useState({
    name: "",
    temp_c: null,
    temp_f: null,
    wind_mph: null,
    wind_kph: null,
    humidity: null,
    condition: "",
    icon: "",
  });

  const [forecastDays, setForecastDays] = useState([]);

  useEffect(() => {
    const fetchCurrentWeather = async () => {
      try {
        const response = await fetch("https://api.weatherapi.com/v1/current.json?key=a9d905b08ba54dc697c135011250311&q=auto:ip");
        if (!response.ok) {
          throw new Error("Erro na resposta da API");
        }
        const dados = await response.json();

        setCurrentWeather({
          name: dados.location?.name,
          temp_c: dados.current?.temp_c,
          temp_f: dados.current?.temp_f,
          wind_mph: dados.current?.wind_mph,
          wind_kph: dados.current?.wind_kph,
          humidity: dados.current?.humidity,
          condition: dados.current?.condition?.text,
          icon: dados.current?.condition?.icon,
        });
      } catch (error) {
        console.error("Erro ao buscar o tempo atual: ", error);
      }
    };

    const fetchForecast = async () => {
      try {
        const response = await fetch("https://api.weatherapi.com/v1/forecast.json?key=a9d905b08ba54dc697c135011250311&q=auto:ip&days=6");
        if (!response.ok) {
          throw new Error("Erro na resposta da API");
        }
        const dados = await response.json();

        setForecastDays(dados.forecast?.forecastday || []);
      } catch (error) {
        console.error("Erro ao buscar a previsão: ", error);
      }
    };

    fetchCurrentWeather();
    fetchForecast();
  }, []);

  return (
    <>
      <div className='h-screen w-full bg-blue-100'>
        <section className='flex flex-col text-xl'>
          <h1 className='bg-blue-400 text-4xl font-semibold text-white p-3'>Clima Atual</h1>
          <div className='px-7 py-5'>
            <p>Cidade: {currentWeather.name}</p>
            <p>Temperatura: {currentWeather.temp_c} °C</p>
            <p>Temperatura: {currentWeather.temp_f} °F</p>
            <p>Vento: {currentWeather.wind_mph} mph</p>
            <p>Vento: {currentWeather.wind_kph} kph</p>
            <p>Umidade: {currentWeather.humidity}%</p>
            <div className='flex gap-2 items-center'>
              <p>Condição: {currentWeather.condition}</p>
              <img src={currentWeather.icon} className='h-7 w-7' />
            </div>
          </div>
        </section>

        <section className='flex flex-col text-xl'>
          <h1 className='bg-blue-400 text-4xl font-semibold text-white p-3'>Previsão</h1>
          <div className='grid grid-cols-6 gap-5 px-7 py-5'>
            {forecastDays.map((day) => (
              <div key={day.date} className='flex flex-col gap-2 bg-white rounded-2xl p-3'>
                <p>Data: {day.date}</p>
                <p>Min: {day.day.mintemp_c} °C</p>
                <p>Máx: {day.day.maxtemp_c} °C</p>
                <div className='flex gap-2 items-center'>
                  <p>Condição: {day.day.condition.text}</p>
                  <img src={day.day.condition.icon} className='h-7 w-7' />
                </div>
              </div>
            ))}
          </div>
        </section>
      </div>
    </>
  );
}

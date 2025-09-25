import Card from "../../components/Card/Card";

const Home = () => {
  return (
    <>
      <h2 className='text-2xl font-bold mb-4'>Página Home</h2>
      <main className='flex-1 container mx-auto p-6'>
        <div className='grid grid-cols-3 gap-6'>
          <Card>
            <h2 className='font-semibold'>Coluna 1</h2>
            <p>
              Lorem XPTO ipsum dolor sit amet consectetur adipisicing elit. Quod est dicta ipsa magni repudiandae eligendi consectetur enim, velit voluptatibus
              repellendus ex maiores porro tempora, distinctio optio. Consequatur tempore iste ipsa!
            </p>
          </Card>
          <Card>
            <h2 className='font-semibold'>Coluna 2</h2>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quod est dicta ipsa magni repudiandae eligendi consectetur enim, velit voluptatibus repellendus ex
              maiores porro tempora, distinctio optio. Consequatur tempore iste ipsa!
            </p>
          </Card>
          <Card>
            <h2 className='font-semibold'>Coluna 3</h2>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quod est dicta ipsa magni repudiandae eligendi consectetur enim, velit voluptatibus repellendus ex
              maiores porro tempora, distinctio optio. Consequatur tempore iste ipsa!
            </p>
          </Card>
          <Card>
            <h2 className='font-semibold'>Coluna 4</h2>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quod est dicta ipsa magni repudiandae eligendi consectetur enim, velit voluptatibus repellendus ex
              maiores porro tempora, distinctio optio. Consequatur tempore iste ipsa!
            </p>
          </Card>
          <Card>
            <h2 className='font-semibold'>Coluna 5</h2>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quod est dicta ipsa magni repudiandae eligendi consectetur enim, velit voluptatibus repellendus ex
              maiores porro tempora, distinctio optio. Consequatur tempore iste ipsa!
            </p>
          </Card>
          <Card>
            <h2 className='font-semibold'>Coluna 6</h2>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quod est dicta ipsa magni repudiandae eligendi consectetur enim, velit voluptatibus repellendus ex
              maiores porro tempora, distinctio optio. Consequatur tempore iste ipsa!
            </p>
          </Card>
        </div>
      </main>
    </>
  );
};

export default Home;

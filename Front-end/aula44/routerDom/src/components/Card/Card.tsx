type CardProps = {
  children: React.ReactNode;
};
const Card = ({ children }: CardProps) => {
  return (
    <>
      <div className='bg-gray-100 p-4 rounded shadow-md'>{children}</div>
    </>
  );
};

export default Card;

import styles from "./Home.module.scss";
import Hero from "../../sections/home/hero";

const Home = () => {
  return (
    <div className={styles.home}>
      <Hero />
    </div>
  );
};

export default Home;

import styles from "./hero.module.scss";

const Hero = () => {
  return (
    <section className={styles.hero}>
      <div className={`container ${styles.heroContainer}`}>
        <div className={styles.heroHeading}>
          <h1>Let AI write your project documentation for you</h1>
          <h2>Save time on documentation and focus on coding</h2>
        </div>
        <div className={styles.inputWrapper}>
          <input
            type="url"
            placeholder="Try now! Insert your repo link here;)"
            className={styles.repoInput}
          />
        </div>
      </div>
      <div className="container">
        <article className={styles.cardsFlexbox}>
          <section className={styles.card}>
            <span className={styles.cardHeading}>
              <span className={styles.cardIcon} data-icon="file-alt"></span>
              <h3>Generate README</h3>
            </span>
            <p>
              Get a polished README in seconds. AI writes it, you tweak it, your
              project shines.
            </p>
          </section>
          <section className={styles.card}>
            <span className={styles.cardHeading}>
              <span className={styles.cardIcon} data-icon="code"></span>
              <h3>Generate README</h3>
            </span>
            <p>
              Get a polished README in seconds. AI writes it, you tweak it, your
              project shines.
            </p>
          </section>
          <section className={styles.card}>
            <span className={styles.cardHeading}>
              <span className={styles.cardIcon} data-icon="robot"></span>
              <h3>Generate README</h3>
            </span>
            <p>
              Get a polished README in seconds. AI writes it, you tweak it, your
              project shines.
            </p>
          </section>
        </article>
      </div>
    </section>
  );
};

export default Hero;

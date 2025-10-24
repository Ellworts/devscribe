import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.scss";
import App from "./App";

// global styles setup
import './styles/globals.scss';
import './styles/mixins.scss';
import './styles/variables.scss';

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <App />
  </StrictMode>
);

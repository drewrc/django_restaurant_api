import "./components/App.css";
import { useState } from "react";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import Button from "react-bootstrap/Button";
import Order from "./components/Order";
import MenuList from "./components/MenuList";
import Home from "./components/Home";

function App() {
  const [selection, setSelection] = useState("a");
  return (
    <div>
      <header>
        <div className="header-content">
          <Navbar variant="dark" bg="dark" expand="lg">
            <Container className="site-nav">
              <img
                className="image-logo"
                src={require("./components/pizzalogo.png")}
              />
              <Navbar.Brand href="#home">Vic's Pizza</Navbar.Brand>
              <Navbar.Toggle aria-controls="basic-navbar-nav" />
              <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="me-auto">
                  <Button
                    onClick={() => setSelection("a")}
                    className="btn btn-link"
                    type="button"
                  >
                    Home
                  </Button>
                  <Button
                    onClick={() => setSelection("b")}
                    className="btn btn-link"
                    type="button"
                  >
                    Menu
                  </Button>
                </Nav>
              </Navbar.Collapse>
            </Container>
          </Navbar>
        </div>
      </header>

      {selection === "a" && <Home />}
      {selection === "b" && <MenuList />}
    </div>
  );
}

export default App;
